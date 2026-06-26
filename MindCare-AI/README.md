# MindCare AI - Depression and Stress Evaluation System

An AI-powered system for evaluating stress levels and depression risk using machine learning algorithms.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technology Stack](#technology-stack)
- [Dataset](#dataset)
- [Model Information](#model-information)
- [Deployment](#deployment)
- [License](#license)
- [Disclaimer](#disclaimer)

## 📖 Overview

MindCare AI is a comprehensive mental health assessment system that uses machine learning to predict stress levels and depression risk based on behavioral and lifestyle factors. The system is built with a Flask backend, scikit-learn ML models, and an interactive HTML/CSS/JS frontend.

## ✨ Features

- **Real-time Assessment**: Get instant stress and depression predictions
- **AI-Powered Insights**: Personalized suggestions based on assessment results
- **Analytics Dashboard**: Track mental health trends with visualizations
- **Secure & Private**: Data encryption and local processing
- **Machine Learning**: Random Forest classifier for accurate predictions
- **User-Friendly Interface**: Interactive web-based assessment form
- **API Endpoints**: RESTful API for integration with other systems
- **Real-time A+B Pipeline**: Questionnaire + behavior-inference (audio/video/typing/cognitive)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- 500MB free disk space
- Internet connection (for dataset download)

## 🚀 Installation

### Step 1: Clone or Download the Project

```bash
cd MindCare-AI
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
python test.py
```

Expected output:
```
============================================================
Testing MindCare AI - Library Installation
============================================================
✅ pandas              - Installed successfully
✅ numpy               - Installed successfully
✅ scikit-learn        - Installed successfully
✅ Flask               - Installed successfully
✅ matplotlib          - Installed successfully
✅ seaborn             - Installed successfully
✅ joblib              - Installed successfully
✅ plotly              - Installed successfully
============================================================
✅ Passed: 8/8
🎉 All libraries installed successfully!
```

### Step 4: Download Dataset

1. Visit [Kaggle](https://www.kaggle.com)
2. Search for "Student Depression Dataset"
3. Download the CSV file
4. Place it in `dataset/` folder as `student_depression_dataset.csv`

## 📁 Project Structure

```
MindCare-AI/
│
├── app.py                    # Flask application
├── model.py                  # ML model training and prediction
├── data_preprocessing.py     # Data cleaning and transformation
├── config.py                 # Configuration settings
├── main.py                   # Entry point
├── test.py                   # Library verification
├── train.py                  # Model training script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── dataset/                  # Dataset folder
│   └── student_depression_dataset.csv  # Training dataset
│
├── model/                    # Trained models
│   ├── stress_model.pkl      # Trained Random Forest model
│   └── scaler.pkl            # Feature scaler
│
├── templates/                # HTML templates
│   ├── index.html            # Home page
│   ├── test.html             # Assessment form
│   ├── dashboard.html        # Analytics dashboard
│   └── about.html            # About page
│
└── static/                   # Static files
    ├── style.css             # CSS styles
    └── script.js             # JavaScript functionality
│
├── src/                       # Modular Python source
│   ├── realtime/              # Real-time assessment pipeline (A + B)
│   │   ├── runtime.py          # Fusion orchestrator
│   │   ├── questionnaire.py    # PHQ-9 / GAD-7 / DASS-21 scoring
│   │   ├── audio_features.py   # Audio heuristics (features in)
│   │   ├── video_features.py   # Video heuristics (features in)
│   │   ├── typing_features.py  # Typing heuristics
│   │   ├── cognitive_tests.py  # Reaction-time heuristics
│   │   └── cli_demo.py         # Demo runner
```

## 💻 Usage

### Run the Application

```bash
python main.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

### Run the Real-time A+B Demo

```bash
python src/realtime/cli_demo.py
```

### Train the Model

```bash
python train.py
```

Or use the Dashboard API:
```bash
curl -X POST http://localhost:5000/api/train
```

### Run Tests

```bash
python test.py
```

## 🔌 API Endpoints

### 1. Get Home Page
```
GET /
```

### 2. Get Assessment Page
```
GET /test
```

### 3. Get Dashboard
```
GET /dashboard
```

### 4. Get About Page
```
GET /about
```

### 5. Make Prediction
```
POST /api/predict
Content-Type: application/json

{
    "Age": 25,
    "Gender": 0,
    "Sleep_Hours": 7,
    "Study_Pressure": 3,
    "Work_Pressure": 3,
    "Financial_Stress": 2,
    "Anxiety": 5,
    "Social_Activity": 3
}

Response:
{
    "stress_level": "Medium Stress",
    "confidence": 92.50,
    "depression_risk": 35.25,
    "suggestions": ["...", "..."],
    "timestamp": "2024-01-01T12:00:00"
}
```

### 6. Train Model
```
POST /api/train

Response:
{
    "status": "success",
    "message": "Model trained successfully",
    "metrics": {
        "accuracy": 0.85,
        "precision": 0.83,
        "recall": 0.82,
        "f1_score": 0.82
    }
}
```

### 7. Get Dataset Info
```
GET /api/dataset-info

Response:
{
    "status": "success",
    "rows": 1500,
    "columns": 9,
    "column_names": ["Age", "Gender", "Sleep_Hours", ...]
}
```

### 8. Health Check
```
GET /api/health

Response:
{
    "status": "healthy",
    "message": "MindCare AI is running",
    "timestamp": "2024-01-01T12:00:00"
}
```

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3, Flask |
| ML Framework | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Frontend | HTML5, CSS3, JavaScript |
| Serialization | Joblib |

## 📊 Dataset Information

The project uses the "Student Depression Dataset" from Kaggle with the following features:

| Feature | Type | Description |
|---------|------|-----------|
| Age | Integer | Age of the student |
| Gender | Categorical | Male (0) / Female (1) |
| Sleep Hours | Float | Hours of sleep per day |
| Study Pressure | Integer | Study pressure level (1-5) |
| Work Pressure | Integer | Work pressure level (1-5) |
| Financial Stress | Integer | Financial stress level (1-5) |
| Anxiety | Float | Anxiety level (0-10) |
| Social Activity | Integer | Social interactions per week |
| Depression | Target | Depression status (0/1/2) |

## 🤖 Model Information

**Algorithm**: Random Forest Classifier

**Parameters**:
- n_estimators: 100
- max_depth: 15
- min_samples_split: 5
- min_samples_leaf: 2

**Performance Metrics**:
- Accuracy: ~85%
- Precision: ~83%
- Recall: ~82%
- F1-Score: ~82%

**Features Used**: 8 features (Age, Gender, Sleep Hours, Study Pressure, Work Pressure, Financial Stress, Anxiety, Social Activity)

**Output Classes**: 
- 0: Low Stress
- 1: Medium Stress
- 2: High Stress

## 🌐 Deployment

### Deployment Options

1. **Render.com** (Free tier available)
   - Deploy Flask backend
   - Free for first 750 hours/month

2. **Railway.app**
   - Full-stack deployment
   - Free credits: $5/month

3. **Heroku** (Paid)
   - Simple git-based deployment
   - Starting at $7/month

4. **PythonAnywhere**
   - Python-specific hosting
   - Free tier available

### Pre-Deployment Checklist

- [ ] All dependencies in requirements.txt
- [ ] Environment variables configured
- [ ] Database/dataset configured
- [ ] Trained model included
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Security measures in place

## 📝 License

This project is open-source and available under the MIT License.

## ⚠️ Disclaimer

**Important**: MindCare AI is a supportive tool designed for self-assessment purposes. It is **NOT** a substitute for professional medical or psychological advice.

If you are experiencing severe mental health issues or having thoughts of self-harm, please contact:
- **National Suicide Prevention Lifeline**: 1-800-273-8255
- **Crisis Text Line**: Text HOME to 741741
- **International Association for Suicide Prevention**: https://www.iasp.info/resources/Crisis_Centres/

Always consult with qualified healthcare professionals for proper diagnosis and treatment.

## 📧 Support

For issues, questions, or suggestions, please create an issue in the repository or contact the development team.

## 🙏 Acknowledgments

- Kaggle for providing the dataset
- Scikit-learn community
- Flask framework developers
- All contributors to this project

---

**Happy Mental Health Tracking! 🧠💚**

*Developed with care for mental health awareness and early intervention.*
