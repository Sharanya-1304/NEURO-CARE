"""
Configuration file for MindCare AI
"""

import os

# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
MODEL_DIR = os.path.join(BASE_DIR, 'model')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Dataset configuration
DATASET_FILE = os.path.join(DATASET_DIR, 'Student Depression Dataset.csv')
TEST_SPLIT = 0.2
RANDOM_STATE = 42

# Model configuration
MODEL_FILE = os.path.join(MODEL_DIR, 'stress_model.pkl')
SCALER_FILE = os.path.join(MODEL_DIR, 'scaler.pkl')

# Flask configuration
DEBUG = True
SECRET_KEY = 'mindcare-ai-secret-key'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Feature names (update based on your dataset)
FEATURE_NAMES = [
    'Age',
    'Gender',
    'Sleep_Hours',
    'Study_Pressure',
    'Financial_Stress',
    'Anxiety',
    'Social_Activity',
    'Work_Pressure'
]

# Target categories
STRESS_LEVELS = ['Low Stress', 'Medium Stress', 'High Stress']
DEPRESSION_RISK_THRESHOLD = 0.6

# Suggestions based on stress level
SUGGESTIONS = {
    'Low': [
        'Maintain your healthy routine',
        'Continue regular exercise',
        'Keep a balanced sleep schedule',
        'Stay connected with friends and family'
    ],
    'Medium': [
        'Try to reduce your workload when possible',
        'Practice meditation or yoga',
        'Take regular breaks',
        'Engage in relaxing activities',
        'Consider speaking with a counselor'
    ],
    'High': [
        'Please consult a mental health professional',
        'Prioritize your well-being',
        'Try stress-management techniques',
        'Reach out to support networks',
        'Consider professional help immediately'
    ]
}
