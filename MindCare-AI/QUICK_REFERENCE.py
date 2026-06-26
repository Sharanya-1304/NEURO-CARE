"""
QUICK REFERENCE CARD - MindCare AI
Save this for quick access to common commands and information
"""

print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                   MindCare AI - QUICK REFERENCE CARD                     ║
║              AI-Based Depression and Stress Evaluation System            ║
╚═══════════════════════════════════════════════════════════════════════════╝

📋 FILES AT A GLANCE
──────────────────────────────────────────────────────────────────────────

   🚀 main.py              → START HERE (python main.py)
   📱 app.py               → Flask web app (don't run directly)
   🧠 model.py             → ML model training & prediction
   🔧 train.py             → Train model (python train.py)
   ✅ test.py              → Verify installation (python test.py)
   📋 setup_verify.py      → Check project setup


🛠️  INSTALLATION COMMANDS
──────────────────────────────────────────────────────────────────────────

   1. Install Dependencies
      $ pip install -r requirements.txt

   2. Verify Setup
      $ python setup_verify.py

   3. Test Libraries
      $ python test.py

   4. Download Dataset
      • Kaggle.com → Search "Student Depression Dataset"
      • Download CSV → Place in dataset/ folder

   5. Train Model
      $ python train.py

   6. Run Application
      $ python main.py

   7. Open Browser
      → http://localhost:5000


📊 FEATURES REQUIRED FOR PREDICTION
──────────────────────────────────────────────────────────────────────────

   Age              : 13-100 (years)
   Gender           : 0 (Male) or 1 (Female)
   Sleep_Hours      : 0-12 (hours per day)
   Study_Pressure   : 1-5 (1=Very Low, 5=Very High)
   Work_Pressure    : 1-5 (1=Very Low, 5=Very High)
   Financial_Stress : 1-5 (1=Very Low, 5=Very High)
   Anxiety          : 0-10 (0=None, 10=Maximum)
   Social_Activity  : 0-7 (times per week)


🌐 WEB PAGES & URLS
──────────────────────────────────────────────────────────────────────────

   Home          : http://localhost:5000/
   Assessment    : http://localhost:5000/test
   Dashboard     : http://localhost:5000/dashboard
   About         : http://localhost:5000/about


🔌 API ENDPOINTS (CURL EXAMPLES)
──────────────────────────────────────────────────────────────────────────

   Health Check
   $ curl http://localhost:5000/api/health

   Make Prediction
   $ curl -X POST http://localhost:5000/api/predict \
     -H "Content-Type: application/json" \
     -d '{"Age":25,"Gender":0,"Sleep_Hours":7,"Study_Pressure":3,...}'

   Train Model
   $ curl -X POST http://localhost:5000/api/train

   Dataset Info
   $ curl http://localhost:5000/api/dataset-info


🎯 OUTPUT STRESS LEVELS
──────────────────────────────────────────────────────────────────────────

   ✅ Low Stress        → Maintain healthy routine
   ⚠️  Medium Stress     → Reduce workload, practice relaxation
   🔴 High Stress       → Consult mental health professional


📁 PROJECT STRUCTURE
──────────────────────────────────────────────────────────────────────────

   MindCare-AI/
   ├── Python Files
   │   ├── main.py          ← Run this
   │   ├── app.py
   │   ├── model.py
   │   ├── train.py
   │   └── ...
   ├── templates/
   │   ├── index.html       ← Home page
   │   ├── test.html        ← Assessment
   │   ├── dashboard.html   ← Analytics
   │   └── about.html
   ├── static/
   │   ├── style.css
   │   └── script.js
   ├── model/               ← Trained models
   ├── dataset/             ← Add CSV here
   └── requirements.txt


⚙️  CONFIGURATION
──────────────────────────────────────────────────────────────────────────

   File: config.py

   Key Settings:
   • DATASET_FILE    : Path to CSV dataset
   • MODEL_FILE      : Where trained model is saved
   • TEST_SPLIT      : Train/test split ratio (0.2 = 20% test)
   • RANDOM_STATE    : Random seed for reproducibility


🐛 COMMON ISSUES & FIXES
──────────────────────────────────────────────────────────────────────────

   Issue              → Solution
   ──────────────────────────────────────────────────────────
   pandas not found   → pip install -r requirements.txt
   Port 5000 in use   → Change port in main.py
   Dataset not found  → Download from Kaggle, place in dataset/
   Model not found    → Run python train.py first
   Import error       → Check Python version (3.8+)
   Template not found → Verify templates/ folder exists


🚀 DEPLOYMENT QUICK LINKS
──────────────────────────────────────────────────────────────────────────

   Render.com      : https://render.com
   Railway.app     : https://railway.app
   Heroku.com      : https://heroku.com
   PythonAnywhere  : https://pythonanywhere.com


📚 DOCUMENTATION
──────────────────────────────────────────────────────────────────────────

   README.md           : Full documentation
   API_DOCS.py         : API reference (run to view)
   PROJECT_SUMMARY.py  : Detailed summary (run to view)
   config.py           : Configuration options


🧪 TESTING COMMANDS
──────────────────────────────────────────────────────────────────────────

   Verify Installation
   $ python test.py

   Verify Project Setup
   $ python setup_verify.py

   View API Documentation
   $ python API_DOCS.py

   View Project Summary
   $ python PROJECT_SUMMARY.py


🎓 LEARNING RESOURCES
──────────────────────────────────────────────────────────────────────────

   Flask             : flask.palletsprojects.com
   Scikit-learn      : scikit-learn.org
   Pandas            : pandas.pydata.org
   NumPy             : numpy.org
   Kaggle Datasets   : kaggle.com/datasets


⚠️  IMPORTANT NOTES
──────────────────────────────────────────────────────────────────────────

   ⚠️  This tool is NOT a substitute for professional mental health advice
   ⚠️  In crisis? Call 1-800-273-8255 (National Suicide Prevention)
   ⚠️  Always consult qualified healthcare professionals
   ⚠️  Data is processed locally, not stored or shared


🔐 SECURITY
──────────────────────────────────────────────────────────────────────────

   ✅ Data Encryption : Features are normalized/scaled
   ✅ No Storage      : Assessments not saved
   ✅ Local Processing: All computation on your machine
   ✅ Input Validation: All inputs are validated


💾 FILE SIZES (APPROXIMATE)
──────────────────────────────────────────────────────────────────────────

   stress_model.pkl  : 1-2 MB
   scaler.pkl        : 100 KB
   Dataset CSV       : 5-10 MB
   Total Needed      : ~50 MB


⏱️  EXECUTION TIMES (APPROXIMATE)
──────────────────────────────────────────────────────────────────────────

   pip install       : 2-3 minutes
   python test.py    : 5 seconds
   python train.py   : 1-2 minutes
   Model prediction  : <1 second
   Dashboard load    : 2-3 seconds


📞 QUICK CONTACTS
──────────────────────────────────────────────────────────────────────────

   National Suicide Prevention Lifeline
   Phone: 1-800-273-8255 (24/7)
   Website: suicidepreventionlifeline.org

   Crisis Text Line
   Text HOME to: 741741

   International Association for Suicide Prevention
   Website: iasp.info


🎯 SUCCESS INDICATORS
──────────────────────────────────────────────────────────────────────────

   ✅ test.py shows all libraries installed
   ✅ setup_verify.py shows all files present
   ✅ main.py starts without errors
   ✅ http://localhost:5000 opens in browser
   ✅ Assessment form works and returns results
   ✅ Dashboard loads with visualizations


═══════════════════════════════════════════════════════════════════════════

Quick Start: pip install -r requirements.txt → python main.py

═══════════════════════════════════════════════════════════════════════════
""")
