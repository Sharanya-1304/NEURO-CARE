"""
Flask Application for MindCare AI
Main web application file
"""

from flask import Flask, render_template, request, jsonify, send_file
import json
import numpy as np
import pandas as pd
import os
from datetime import datetime
from model import StressModel
from data_preprocessing import DataPreprocessor
from src.realtime.runtime import assess as multimodal_assess
from config import (
    DATASET_FILE, FEATURE_NAMES, STRESS_LEVELS, 
    DEPRESSION_RISK_THRESHOLD, SUGGESTIONS
)

# Initialize Flask app
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
app.config['SECRET_KEY'] = 'mindcare-ai-secret-key'

# Initialize model and preprocessor
stress_model = StressModel()
preprocessor = DataPreprocessor()

# Global variable to store model metrics
model_metrics = {}
ASSESSMENT_HISTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'assessment_history.json')


def load_assessment_history():
    if not os.path.exists(ASSESSMENT_HISTORY_FILE):
        return []
    try:
        with open(ASSESSMENT_HISTORY_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_assessment_history(history):
    os.makedirs(os.path.dirname(ASSESSMENT_HISTORY_FILE), exist_ok=True)
    with open(ASSESSMENT_HISTORY_FILE, 'w', encoding='utf-8') as file:
        json.dump(history[-100:], file, indent=2)


def record_assessment(result, payload):
    history = load_assessment_history()
    entry = {
        'timestamp': datetime.now().isoformat(),
        'stress_score': result['stress_score'],
        'depression_score': result['depression_score'],
        'anxiety_score': result['anxiety_score'],
        'stress_level': result['stress_level'],
        'flags': result.get('flags', []),
        'text_provider': result.get('detail', {}).get('text_emotion', {}).get('provider', 'none'),
        'sleep_hours': payload.get('Sleep_Hours') or payload.get('questionnaire', {}).get('sleep_hours'),
        'typing_cpm': payload.get('typing', {}).get('chars_per_min'),
        'reaction_time_ms': payload.get('cognitive', {}).get('reaction_time_ms'),
        'face_signal': result.get('detail', {}).get('neural_models', {}).get('cnn_depression', 0),
        'summary': result.get('assistant_message', ''),
    }
    history.append(entry)
    save_assessment_history(history)
    return entry


def build_model_features(data):
    """Map the web form fields to the 17-column trained dataset format."""
    age = float(data.get('Age', 25))
    gender = float(data.get('Gender', 0))
    sleep_hours = float(data.get('Sleep_Hours', 7))
    study_pressure = float(data.get('Study_Pressure', 3))
    work_pressure = float(data.get('Work_Pressure', 0))
    financial_stress = float(data.get('Financial_Stress', 3))
    anxiety = float(data.get('Anxiety', 5))
    social_activity = float(data.get('Social_Activity', 3))

    if sleep_hours < 5:
        sleep_duration = 2
    elif sleep_hours < 7:
        sleep_duration = 0
    elif sleep_hours <= 8:
        sleep_duration = 1
    else:
        sleep_duration = 3

    return [
        0,                  # id placeholder
        gender,
        age,
        0,                  # City placeholder
        0,                  # Profession placeholder
        study_pressure,
        work_pressure,
        7.0,                # CGPA neutral default
        max(1, min(5, 6 - study_pressure)),
        0,                  # Job Satisfaction default
        sleep_duration,
        1 if social_activity >= 3 else 2,
        0,                  # Degree placeholder
        1 if anxiety >= 7 else 0,
        max(0, min(12, 12 - sleep_hours + study_pressure)),
        financial_stress,
        0,                  # Family History placeholder
    ]


def stress_label(score):
    if score < 35:
        return "Low Stress"
    if score < 70:
        return "Medium Stress"
    return "High Stress"


def build_assistant_message(result):
    stress = result["stress_score"]
    depression = result["depression_score"]
    anxiety = result["anxiety_score"]
    text_summary = result["detail"]["text_emotion"]["summary"]

    if max(stress, depression, anxiety) >= 75:
        lead = "Your signals show a high mental load right now."
    elif max(stress, depression, anxiety) >= 45:
        lead = "Your signals suggest some strain, but there are also stabilizing signs."
    else:
        lead = "Your current signals look relatively balanced."

    return (
        f"{lead} {text_summary} Consider a short reset: hydrate, step away "
        "from the screen, slow your breathing for two minutes, and talk to a trusted person "
        "if these feelings continue."
    )


def multimodal_suggestions(result):
    suggestions = [
        "Try a two-minute breathing reset and reduce screen stimulation briefly.",
        "Write one concrete next step instead of holding the whole problem in your head.",
        "If this pattern repeats for several days, speak with a counselor or trusted person.",
    ]
    detail = result.get("detail", {})
    neural = detail.get("neural_models", {})
    text = detail.get("text_emotion", {})

    if neural.get("cnn_depression", 0) > 55:
        suggestions.append("Take a posture and eye-rest break; low movement and gaze avoidance can reflect fatigue.")
    if neural.get("rnn_stress", 0) > 45:
        suggestions.append("Typing rhythm suggests strain; pause before replying to stressful messages.")
    if text.get("provider") == "fallback":
        suggestions.append("Install Transformers for stronger Hugging Face text emotion detection.")
    return suggestions


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/test')
def test():
    """Stress test page"""
    return render_template('test.html')


@app.route('/dashboard')
def dashboard():
    """Analytics dashboard"""
    return render_template('dashboard.html')


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    """API endpoint for stress prediction"""
    try:
        data = request.json
        
        # Extract features from request
        features = []
        for feature in FEATURE_NAMES:
            if feature in data:
                features.append(float(data[feature]))
            else:
                return jsonify({'error': f'Missing feature: {feature}'}), 400
        
        # Convert the 8-field web form into the 17-feature trained model input.
        X = np.array([build_model_features(data)])
        
        # Load scaler if exists
        preprocessor.load_scaler()
        
        # Normalize features
        X_scaled = preprocessor.scaler.transform(X)
        
        # Load the trained model if the app was just started.
        if not stress_model.is_trained:
            stress_model.load_model()

        # Make prediction
        prediction, probability = stress_model.predict(X_scaled)
        
        # Prepare response
        stress_level = STRESS_LEVELS[prediction[0]] if prediction[0] < len(STRESS_LEVELS) else 'Unknown'
        confidence = float(np.max(probability[0])) * 100
        depression_risk = float(probability[0][-1]) * 100 if len(probability[0]) > 0 else 0
        
        # Get suggestions
        stress_category = stress_level.split()[0]  # 'Low', 'Medium', or 'High'
        suggestions = SUGGESTIONS.get(stress_category, [])
        
        response = {
            'stress_level': stress_level,
            'confidence': round(confidence, 2),
            'depression_risk': round(depression_risk, 2),
            'suggestions': suggestions,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/multimodal-assess', methods=['POST'])
def multimodal_assessment():
    """Behavioral intelligence endpoint using questionnaire, text, face, typing, and cognitive signals."""
    try:
        payload = request.json or {}

        result = multimodal_assess(payload)
        result["stress_level"] = stress_label(float(result["stress_score"]))
        result["assistant_message"] = build_assistant_message(result)
        result["suggestions"] = multimodal_suggestions(result)
        result["history_entry"] = record_assessment(result, payload)

        high_risk = (
            result["depression_score"] >= 75
            or "high_depression_risk" in result.get("flags", [])
        )
        result["safety_note"] = (
            "If you feel unsafe or may harm yourself, contact local emergency services or a trusted person immediately."
            if high_risk
            else "Use this as a supportive wellness signal, not a diagnosis."
        )

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/assessment-history', methods=['GET'])
def assessment_history():
    """Return local assessment history for dashboard analytics."""
    history = load_assessment_history()
    total = len(history)

    if total == 0:
        return jsonify({
            'status': 'empty',
            'total': 0,
            'history': [],
            'summary': {
                'low': 0,
                'medium': 0,
                'high': 0,
                'avg_stress': 0,
                'avg_depression': 0,
                'avg_anxiety': 0,
            },
            'insight': 'No assessments yet. Run a behavioral assessment to populate this dashboard.'
        }), 200

    low = sum(1 for item in history if item.get('stress_score', 0) < 35)
    medium = sum(1 for item in history if 35 <= item.get('stress_score', 0) < 70)
    high = total - low - medium
    avg_stress = sum(item.get('stress_score', 0) for item in history) / total
    avg_depression = sum(item.get('depression_score', 0) for item in history) / total
    avg_anxiety = sum(item.get('anxiety_score', 0) for item in history) / total
    latest = history[-1]

    insight = (
        f"Latest assessment shows {latest.get('stress_level', 'Unknown')} with "
        f"{latest.get('stress_score', 0):.1f}% stress, "
        f"{latest.get('depression_score', 0):.1f}% depression risk, and "
        f"{latest.get('anxiety_score', 0):.1f}% anxiety signal."
    )

    return jsonify({
        'status': 'success',
        'total': total,
        'history': history,
        'summary': {
            'low': low,
            'medium': medium,
            'high': high,
            'avg_stress': round(avg_stress, 2),
            'avg_depression': round(avg_depression, 2),
            'avg_anxiety': round(avg_anxiety, 2),
        },
        'latest': latest,
        'insight': insight,
    }), 200


@app.route('/api/train', methods=['POST'])
def train_model():
    """API endpoint to train the model"""
    try:
        # Load dataset
        df = preprocessor.load_dataset()
        
        # Preprocess data
        df_processed = preprocessor.preprocess(df)
        
        # Separate features and target
        # Assuming last column is the target
        X = df_processed.iloc[:, :-1].values
        y = df_processed.iloc[:, -1].values
        
        # Normalize features
        X_scaled = preprocessor.normalize_features(X)
        preprocessor.save_scaler()
        
        # Split data
        X_train, X_test, y_train, y_test = preprocessor.split_data(X_scaled, y)
        
        # Train model
        stress_model.train(X_train, y_train)
        
        # Evaluate model
        metrics = stress_model.evaluate(X_test, y_test)
        
        # Save model
        stress_model.save_model()
        
        # Get feature importance
        importance_df = stress_model.get_feature_importance()
        
        return jsonify({
            'status': 'success',
            'message': 'Model trained successfully',
            'metrics': metrics,
            'feature_importance': importance_df.to_dict(orient='records')
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


@app.route('/api/dataset-info', methods=['GET'])
def dataset_info():
    """Get dataset information"""
    try:
        if not os.path.exists(DATASET_FILE):
            return jsonify({
                'status': 'error',
                'message': 'Dataset not found. Please download it from Kaggle.'
            }), 404
        
        df = pd.read_csv(DATASET_FILE)
        
        return jsonify({
            'status': 'success',
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': df.columns.tolist(),
            'data_types': df.dtypes.astype(str).to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'MindCare AI is running',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Route not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("=" * 60)
    print("MindCare AI - Flask Application")
    print("=" * 60)
    app.run(debug=True, host='localhost', port=5000)
