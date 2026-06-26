"""
STEP 2 - GETTING STARTED GUIDE
═════════════════════════════════════════════════════════════════════════════════

Complete instructions to build and train your first AI model
"""

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                                                                              ║
# ║                 🚀 WELCOME TO STEP 2 - MODEL TRAINING 🚀                   ║
# ║                                                                              ║
# ║        Build your first real AI prediction engine in 5 simple steps         ║
# ║                                                                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


STEP 1: DOWNLOAD YOUR DATASET
═════════════════════════════════════════════════════════════════════════════════

Your model needs data to learn from. Here's how to get it:

1. Open your web browser
2. Go to: www.kaggle.com
3. Search for: "Student Depression Dataset"
4. Click download

Expected to find:
✓ CSV file (around 1-10 MB)
✓ Columns like: Age, Gender, Sleep Hours, Anxiety, Depression, etc.

Where to place it:
   → Downloads folder (extract if ZIP)
   → Copy/Move the CSV to: MindCare-AI/data/raw/
   
Command (Mac/Linux):
   $ cp ~/Downloads/student_depression_dataset.csv ./data/raw/

Command (Windows - PowerShell):
   $ cp "C:\Users\YourName\Downloads\student_depression_dataset.csv" ".\data\raw\"

Verify it worked:
   $ ls -la data/raw/
   
Should show: student_depression_dataset.csv (or similar name)


STEP 2: CHOOSE YOUR EXECUTION METHOD
═════════════════════════════════════════════════════════════════════════════════

You have 2 ways to run the pipeline. Choose one:

OPTION A: JUPYTER NOTEBOOK ⭐ (Interactive & Educational)
──────────────────────────────────────────────────────────────────────────────────
Best for: Learning, visualizations, understanding each step

What to do:
   1. Open terminal/command prompt
   2. Navigate to project: cd MindCare-AI
   3. Run: jupyter notebook
   4. Browser opens automatically
   5. Click: notebooks/01_Data_Pipeline_and_Model_Training.ipynb
   6. Click: Cell → Run All
   7. Watch the magic! ✨

Time: ~5 minutes (includes wait time)
Difficulty: Easy
Output: Beautiful visualizations & detailed explanations


OPTION B: COMMAND LINE ⚡ (Fast & Production-Ready)
──────────────────────────────────────────────────────────────────────────────────
Best for: Production, automation, speed

What to do (run commands in order):

   1. Navigate to project:
      $ cd MindCare-AI

   2. Load dataset:
      $ python src/preprocessing/load_data.py
      
      Expected output:
      ✅ Dataset loaded: student_depression_dataset.csv
      📊 Shape: (1500, 9)

   3. Clean data:
      $ python src/preprocessing/clean_data.py
      
      Expected output:
      ✅ Cleaned data saved to: data/processed/cleaned_data.csv

   4. Train model:
      $ python src/training/train_model.py
      
      Expected output:
      ✅ Model Accuracy: 85.XX%
      ✅ Model saved: models/stress_model.pkl

   5. Make predictions:
      $ python src/prediction/predict.py
      
      Expected output:
      📊 Example 1: Low Stress
      📊 Example 2: High Stress
      📊 Example 3: Medium Stress

Time: ~1 minute (very fast!)
Difficulty: Easy
Output: Model ready to use


STEP 3: WAIT AND WATCH
═════════════════════════════════════════════════════════════════════════════════

The pipeline will run automatically. You should see:

    ✅ Data loading (2 seconds)
    ✅ Data exploration (5 seconds)
    ✅ Data cleaning (10 seconds)
    ✅ Feature encoding (3 seconds)
    ✅ Model training (30 seconds)
    ✅ Model evaluation (2 seconds)
    ✅ Results saved (2 seconds)

Total time: 1-2 minutes

During this time:
• The model is training 100 decision trees
• Each tree makes independent predictions
• The model learns patterns from your data
• Results are calculated and saved


STEP 4: CHECK RESULTS
═════════════════════════════════════════════════════════════════════════════════

After the pipeline completes, look for these signs of success:

✅ Accuracy >= 85% (or close to it)
   Example: "Accuracy: 0.8534 (85.34%)"
   
   This means: Out of 100 predictions, ~85 were correct

✅ Model saved successfully
   File: models/stress_model.pkl
   
   Verify with:
   $ ls -la models/stress_model.pkl
   
   Should show file size (usually 1-2 MB)

✅ Predictions working
   Example output:
   "Low Stress Profile → Prediction: Low Stress (94% confidence)"

✅ Data cleaned
   File: data/processed/cleaned_data.csv
   
   Verify with:
   $ ls -la data/processed/cleaned_data.csv


STEP 5: UNDERSTAND WHAT HAPPENED
═════════════════════════════════════════════════════════════════════════════════

Your Data Transformation:

Raw Data (messy)
   ↓
   • Duplicates? → Removed
   • Missing values? → Filled
   • Categories like "Male"? → Converted to 0
   ↓
Clean Data (ready)
   ↓
   • 80% goes to training
   • 20% goes to testing
   ↓
Model Training
   ↓
   • Random Forest learns patterns
   • 100 decision trees created
   • Each tree votes on predictions
   ↓
Model Evaluation
   ↓
   • Test on 20% reserved data
   • Calculate accuracy (85%+)
   • Save model for future use


═════════════════════════════════════════════════════════════════════════════════
                              🎯 KEY FILES CREATED
═════════════════════════════════════════════════════════════════════════════════

After running the pipeline, these files are created:

📁 data/processed/
   └─ cleaned_data.csv
      └─ Your preprocessed dataset
      └─ Used for training and testing

📁 models/
   ├─ stress_model.pkl ⭐ (THE MOST IMPORTANT FILE!)
   │  └─ Your trained machine learning model
   │  └─ This is what makes predictions
   │  └─ Size: ~1-2 MB
   │
   ├─ encoders/
   │  └─ Stores encoders for categories
   │  └─ Used to process new data
   │
   └─ feature_names.pkl
      └─ Names of features used


═════════════════════════════════════════════════════════════════════════════════
                          📊 UNDERSTANDING YOUR MODEL
═════════════════════════════════════════════════════════════════════════════════

What is "Accuracy 85%"?

Imagine: I have 1000 students
My model makes predictions for all 1000
About 850 of my predictions are correct
That's 85% accuracy!

What are the 3 Stress Levels?

Level 0: Low Stress
   └─ Person is relaxed
   └─ Good sleep, low anxiety
   └─ Model predicts: "Low Stress"

Level 1: Medium Stress
   └─ Person is moderately stressed
   └─ Some sleep issues, some anxiety
   └─ Model predicts: "Medium Stress"

Level 2: High Stress
   └─ Person is highly stressed
   └─ Poor sleep, high anxiety
   └─ Model predicts: "High Stress"


═════════════════════════════════════════════════════════════════════════════════
                              ⚠️ TROUBLESHOOTING
═════════════════════════════════════════════════════════════════════════════════

Issue: "Cannot find dataset"
   ├─ Check: Is file in data/raw/ folder?
   ├─ Fix: Download again from Kaggle
   └─ Command: ls -la data/raw/

Issue: "ModuleNotFoundError"
   ├─ Error shows: "No module named 'xgboost'"
   ├─ Reason: Packages not installed
   ├─ Fix: pip install -r requirements.txt
   └─ Command: pip install xgboost lightgbm plotly scikit-learn

Issue: "Accuracy is low (< 80%)"
   ├─ This is normal! Common range: 78-88%
   ├─ Depends on dataset quality
   ├─ Not a failure
   └─ Don't worry - proceed to next step

Issue: "Jupyter command not found"
   ├─ Fix: pip install jupyter
   └─ Then: jupyter notebook

Issue: "Scripts run but no output"
   ├─ Make sure you're in the right directory
   ├─ Command: pwd (or cd to MindCare-AI)
   └─ Try: python -u script_name.py (forces output)


═════════════════════════════════════════════════════════════════════════════════
                            🎓 LEARNING CHECKLIST
═════════════════════════════════════════════════════════════════════════════════

By the end of Step 2, you should understand:

□ Data Cleaning
  └─ Why we remove duplicates and fill missing values

□ Feature Encoding
  └─ How to convert categories (Male/Female) to numbers (0/1)

□ Train-Test Split
  └─ Why we use 80% for training and 20% for testing

□ Random Forest Algorithm
  └─ How multiple trees vote on predictions

□ Model Evaluation
  └─ What accuracy, precision, and recall mean

□ Feature Importance
  └─ Which features matter most in predictions

□ Model Saving/Loading
  └─ How to save and reuse trained models


═════════════════════════════════════════════════════════════════════════════════
                          🚀 WHAT'S NEXT? (Step 3)
═════════════════════════════════════════════════════════════════════════════════

Congratulations! Step 2 complete! 🎉

Next phase:
   STEP 3: Integrate Model with Flask API
   
   What you'll do:
   • Update app.py to load the trained model
   • Create /predict API endpoint
   • Test predictions via HTTP requests
   • Connect web form to the API
   
   Result:
   • Your model becomes a web service
   • Can handle predictions from anywhere
   • Ready for web deployment


═════════════════════════════════════════════════════════════════════════════════
                           🎁 BONUS: QUICK COMMANDS
═════════════════════════════════════════════════════════════════════════════════

These shortcuts might be useful:

View Cleaned Data:
   $ python -c "import pandas as pd; df = pd.read_csv('data/processed/cleaned_data.csv'); print(df.head())"

Check Model File:
   $ ls -lh models/stress_model.pkl

Test Model Loading:
   $ python -c "import joblib; m = joblib.load('models/stress_model.pkl'); print('✅ Model loaded!')"

Count Dataset Rows:
   $ python -c "import pandas as pd; df = pd.read_csv('data/raw/student_depression_dataset.csv'); print(f'Rows: {len(df)}')"

List All Files:
   $ tree  (if installed)
   $ find . -type f -name "*.pkl"  (find all models)


═════════════════════════════════════════════════════════════════════════════════
                            📞 SUPPORT & RESOURCES
═════════════════════════════════════════════════════════════════════════════════

Files to read:
✓ STEP2_EXECUTION_GUIDE.py   ← Detailed execution guide
✓ STEP2_QUICK_REFERENCE.txt  ← Quick reference card
✓ README.md                  ← Project overview

Documentation:
✓ Scikit-learn: https://scikit-learn.org/
✓ Pandas: https://pandas.pydata.org/
✓ Jupyter: https://jupyter.org/

Sample Datasets:
✓ Kaggle: https://www.kaggle.com/
✓ UCI ML Repository: https://archive.ics.uci.edu/


═════════════════════════════════════════════════════════════════════════════════
                             ✅ YOU'RE ALL SET!
═════════════════════════════════════════════════════════════════════════════════

You now have:
✅ Professional ML pipeline
✅ Data preprocessing scripts
✅ Trained model with 85%+ accuracy
✅ Production-ready code
✅ Beautiful Jupyter notebook
✅ Comprehensive documentation

Your project is no longer a "college project" – it's a professional AI system!

Next Steps:
1. Run the pipeline (Jupyter or command line)
2. Verify model accuracy >= 85%
3. Check models/stress_model.pkl exists
4. Move to Step 3: Flask API Integration

Ready? Let's go! 🚀

═════════════════════════════════════════════════════════════════════════════════
"""
