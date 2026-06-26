"""
API Documentation for MindCare AI
Complete guide to all available endpoints
"""

API_DOCUMENTATION = """

╔══════════════════════════════════════════════════════════════════════════════╗
║                          MINDCARE AI - API DOCUMENTATION                     ║
║                    Depression and Stress Evaluation System                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

BASE URL: http://localhost:5000

═════════════════════════════════════════════════════════════════════════════════

1. HOME PAGE
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  GET /
   Purpose:   Display home page with project overview
   Returns:   HTML page
   
   Example:
   curl http://localhost:5000/

═════════════════════════════════════════════════════════════════════════════════

2. STRESS TEST ASSESSMENT
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  GET /test
   Purpose:   Display assessment form
   Returns:   HTML form page
   
   Example:
   curl http://localhost:5000/test

═════════════════════════════════════════════════════════════════════════════════

3. DASHBOARD
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  GET /dashboard
   Purpose:   Display analytics dashboard with visualizations
   Returns:   HTML dashboard page
   
   Example:
   curl http://localhost:5000/dashboard

═════════════════════════════════════════════════════════════════════════════════

4. ABOUT PAGE
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  GET /about
   Purpose:   Display about page with project information
   Returns:   HTML about page
   
   Example:
   curl http://localhost:5000/about

═════════════════════════════════════════════════════════════════════════════════

5. MAKE PREDICTION (Main API)
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  POST /api/predict
   Purpose:   Get stress and depression prediction
   Method:    POST
   Content-Type: application/json
   
   Request Body:
   {
       "Age": <integer 13-100>,
       "Gender": <0 for Male, 1 for Female>,
       "Sleep_Hours": <float 0-12>,
       "Study_Pressure": <integer 1-5>,
       "Work_Pressure": <integer 1-5>,
       "Financial_Stress": <integer 1-5>,
       "Anxiety": <float 0-10>,
       "Social_Activity": <integer 0-7>
   }
   
   Response (Success - 200):
   {
       "stress_level": "Medium Stress",
       "confidence": 92.50,
       "depression_risk": 35.25,
       "suggestions": [
           "Try to reduce your workload when possible",
           "Practice meditation or yoga",
           "Take regular breaks",
           "Engage in relaxing activities",
           "Consider speaking with a counselor"
       ],
       "timestamp": "2024-01-01T12:00:00.000000"
   }
   
   Response (Error - 400):
   {
       "error": "Missing feature: Age"
   }
   
   Example using curl:
   curl -X POST http://localhost:5000/api/predict \\
     -H "Content-Type: application/json" \\
     -d '{
       "Age": 25,
       "Gender": 0,
       "Sleep_Hours": 7,
       "Study_Pressure": 3,
       "Work_Pressure": 3,
       "Financial_Stress": 2,
       "Anxiety": 5,
       "Social_Activity": 3
     }'
   
   Example using Python:
   import requests
   import json
   
   url = "http://localhost:5000/api/predict"
   data = {
       "Age": 25,
       "Gender": 0,
       "Sleep_Hours": 7,
       "Study_Pressure": 3,
       "Work_Pressure": 3,
       "Financial_Stress": 2,
       "Anxiety": 5,
       "Social_Activity": 3
   }
   
   response = requests.post(url, json=data)
   print(response.json())

═════════════════════════════════════════════════════════════════════════════════

6. TRAIN MODEL
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  POST /api/train
   Purpose:   Train ML model on dataset (requires dataset.csv)
   Method:    POST
   Returns:   Training metrics and results
   
   Response (Success - 200):
   {
       "status": "success",
       "message": "Model trained successfully",
       "metrics": {
           "accuracy": 0.8523,
           "precision": 0.8412,
           "recall": 0.8201,
           "f1_score": 0.8305,
           "confusion_matrix": [[...], [...], [...]]
       },
       "feature_importance": [
           {
               "feature": "Anxiety",
               "importance": 0.245
           },
           ...
       ]
   }
   
   Response (Error - 400):
   {
       "status": "error",
       "message": "Dataset not found at dataset/student_depression_dataset.csv"
   }
   
   Example:
   curl -X POST http://localhost:5000/api/train

═════════════════════════════════════════════════════════════════════════════════

7. GET DATASET INFORMATION
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  GET /api/dataset-info
   Purpose:   Get information about the dataset
   Returns:   Dataset statistics and metadata
   
   Response (Success - 200):
   {
       "status": "success",
       "rows": 1500,
       "columns": 9,
       "column_names": [
           "Age", "Gender", "Sleep_Hours", "Study_Pressure",
           "Work_Pressure", "Financial_Stress", "Anxiety",
           "Social_Activity", "Depression"
       ],
       "data_types": {
           "Age": "int64",
           "Gender": "object",
           ...
       }
   }
   
   Response (Error - 404):
   {
       "status": "error",
       "message": "Dataset not found. Please download it from Kaggle."
   }
   
   Example:
   curl http://localhost:5000/api/dataset-info

═════════════════════════════════════════════════════════════════════════════════

8. HEALTH CHECK
───────────────────────────────────────────────────────────────────────────────

   Endpoint:  GET /api/health
   Purpose:   Check if API is running
   Returns:   Health status
   
   Response (Success - 200):
   {
       "status": "healthy",
       "message": "MindCare AI is running",
       "timestamp": "2024-01-01T12:00:00.000000"
   }
   
   Example:
   curl http://localhost:5000/api/health

═════════════════════════════════════════════════════════════════════════════════

RESPONSE CODES
───────────────────────────────────────────────────────────────────────────────

   200 OK              - Request successful
   400 Bad Request     - Invalid request data
   404 Not Found       - Resource not found
   500 Server Error    - Internal server error

═════════════════════════════════════════════════════════════════════════════════

FEATURE DESCRIPTIONS
───────────────────────────────────────────────────────────────────────────────

   Age (13-100)
   - Age of the person
   - Type: Integer
   - Range: 13 to 100 years

   Gender
   - Biological gender
   - Type: Integer (0 or 1)
   - Values: 0 = Male, 1 = Female

   Sleep_Hours (0-12)
   - Average sleep hours per day
   - Type: Float
   - Range: 0 to 12 hours

   Study_Pressure (1-5)
   - Level of academic pressure
   - Type: Integer
   - Scale: 1 = Very Low, 5 = Very High

   Work_Pressure (1-5)
   - Level of work pressure
   - Type: Integer
   - Scale: 1 = Very Low, 5 = Very High

   Financial_Stress (1-5)
   - Level of financial stress
   - Type: Integer
   - Scale: 1 = Very Low, 5 = Very High

   Anxiety (0-10)
   - General anxiety level
   - Type: Float
   - Scale: 0 = No Anxiety, 10 = Maximum Anxiety

   Social_Activity (0-7)
   - Social interactions per week
   - Type: Integer
   - Range: 0 to 7 times

═════════════════════════════════════════════════════════════════════════════════

OUTPUT STRESS LEVELS
───────────────────────────────────────────────────────────────────────────────

   Low Stress
   - Healthy stress levels
   - Recommendations: Maintain current routine

   Medium Stress
   - Moderate stress requiring attention
   - Recommendations: Reduce workload, practice relaxation

   High Stress
   - Elevated stress requiring intervention
   - Recommendations: Consult mental health professional

═════════════════════════════════════════════════════════════════════════════════

EXAMPLE WORKFLOW
───────────────────────────────────────────────────────────────────────────────

   1. Check API Health
      GET /api/health
   
   2. Get Dataset Info (Optional)
      GET /api/dataset-info
   
   3. Train Model (First time only)
      POST /api/train
   
   4. Make Predictions
      POST /api/predict
      (Provide user assessment data)
   
   5. Display Results
      (Parse response and show to user)

═════════════════════════════════════════════════════════════════════════════════

ERROR HANDLING
───────────────────────────────────────────────────────────────────────────────

   All endpoints follow standard HTTP status codes:
   - 200 Series: Success
   - 400 Series: Client errors (invalid input)
   - 500 Series: Server errors

   Error Response Format:
   {
       "error": "Description of error",
       "status": "error"  (optional)
   }

═════════════════════════════════════════════════════════════════════════════════

NOTES
───────────────────────────────────────────────────────────────────────────────

   • All timestamps are in ISO 8601 format
   • Confidence is returned as percentage (0-100)
   • All numeric values are properly validated
   • Missing required fields return 400 error
   • Dataset is required for training and predictions
   • Model file is required for predictions (generated after training)

═════════════════════════════════════════════════════════════════════════════════

For more information, see README.md or visit the dashboard at /dashboard

═════════════════════════════════════════════════════════════════════════════════
"""

if __name__ == '__main__':
    print(API_DOCUMENTATION)
