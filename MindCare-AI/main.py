"""
MindCare AI - Depression and Stress Evaluation System
Main entry point for the application
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

print("=" * 60)
print("MindCare AI Project Started")
print("Depression and Stress Evaluation System")
print("=" * 60)

# Import the Flask app
from app import app

if __name__ == '__main__':
    print("\n✅ Application initialized successfully!")
    print("🚀 Starting MindCare AI Server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("\n" + "=" * 60)
    
    # Run the Flask app
    app.run(debug=True, host='localhost', port=5000)
