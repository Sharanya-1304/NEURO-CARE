"""
Machine Learning Model module for MindCare AI
Handles model training, prediction, and evaluation
"""

import os
import sys
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from data_preprocessing import DataPreprocessor
from config import MODEL_FILE, FEATURE_NAMES

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

class StressModel:
    def __init__(self):
        self.model = None
        self.preprocessor = DataPreprocessor()
        self.is_trained = False
        
    def train(self, X_train, y_train):
        """Train the Random Forest model"""
        print("\n" + "=" * 60)
        print("Training Machine Learning Model")
        print("=" * 60)
        
        # Initialize Random Forest Classifier
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        )
        
        # Train the model
        print("🚀 Training Random Forest model...")
        self.model.fit(X_train, y_train)
        
        self.is_trained = True
        print("✅ Model training completed!")
        
        return self.model
    
    def evaluate(self, X_test, y_test):
        """Evaluate model performance"""
        if not self.is_trained or self.model is None:
            raise ValueError("Model not trained yet!")
        
        print("\n" + "=" * 60)
        print("Model Evaluation")
        print("=" * 60)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        
        print(f"\n📊 Model Performance Metrics:")
        print(f"   Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
        print(f"   Precision: {precision:.4f}")
        print(f"   Recall:    {recall:.4f}")
        print(f"   F1-Score:  {f1:.4f}")
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        print(f"\n📈 Confusion Matrix:")
        print(cm)
        
        print("=" * 60)
        
        metrics = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'confusion_matrix': cm.tolist()
        }
        
        return metrics
    
    def predict(self, X):
        """Make predictions on new data"""
        if not self.is_trained or self.model is None:
            raise ValueError("Model not trained yet!")
        
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)
        
        return predictions, probabilities
    
    def get_feature_importance(self, feature_names=None):
        """Get feature importance from the model"""
        if not self.is_trained or self.model is None:
            raise ValueError("Model not trained yet!")
        
        importances = self.model.feature_importances_
        if feature_names is None or len(feature_names) != len(importances):
            feature_names = [f"feature_{idx}" for idx in range(len(importances))]

        feature_importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importances
        }).sort_values('importance', ascending=False)
        
        print("\n📊 Feature Importance:")
        print(feature_importance_df.to_string(index=False))
        
        return feature_importance_df
    
    def save_model(self, filepath=MODEL_FILE):
        """Save the trained model"""
        if not self.is_trained or self.model is None:
            raise ValueError("Model not trained yet!")
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.model, filepath)
        print(f"✅ Model saved to {filepath}")
    
    def load_model(self, filepath=MODEL_FILE):
        """Load a trained model"""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Model not found at {filepath}")
        
        self.model = joblib.load(filepath)
        self.is_trained = True
        print(f"✅ Model loaded from {filepath}")
        
        return self.model


if __name__ == '__main__':
    """Example usage of the model"""
    try:
        # Initialize model
        model = StressModel()
        
        # Load and preprocess data
        preprocessor = DataPreprocessor()
        df = preprocessor.load_dataset()
        
        print("\n✅ Model module loaded successfully!")
        print("   Use this module in app.py for predictions")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
