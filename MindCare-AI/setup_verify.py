"""
Quick Start Guide for MindCare AI.
Execute this file to verify the setup.
"""

import os
import sys


def verify_setup():
    """Verify project setup."""
    print("\n" + "=" * 70)
    print("MindCare AI - Quick Start Verification")
    print("=" * 70)

    print("\n1. Checking Python Version...")
    python_version = (
        f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    print(f"   Python {python_version}")
    if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
        print("   [OK] Python version OK")
    else:
        print("   [ERROR] Python 3.8+ required")
        return False

    print("\n2. Checking Project Structure...")
    required_dirs = ["dataset", "templates", "static", "model"]
    all_exist = True
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"   [OK] {dir_name}/ exists")
        else:
            print(f"   [ERROR] {dir_name}/ missing")
            all_exist = False

    print("\n3. Checking Required Files...")
    required_files = [
        "app.py",
        "model.py",
        "config.py",
        "main.py",
        "test.py",
        "requirements.txt",
        "templates/index.html",
        "templates/test.html",
        "templates/dashboard.html",
        "templates/about.html",
        "static/style.css",
        "static/script.js",
    ]
    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"   [OK] {file_name}")
        else:
            print(f"   [ERROR] {file_name} missing")
            all_exist = False

    print("\n4. Checking Dataset...")
    dataset_path = os.path.join("dataset", "Student Depression Dataset.csv")
    if os.path.exists(dataset_path):
        print(f"   [OK] Dataset found: {dataset_path}")
    else:
        print("   [WARNING] Dataset not found; it is needed for training")
        print("      Expected: dataset/Student Depression Dataset.csv")

    print("\n5. Checking Python Libraries...")
    libraries = [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("sklearn", "scikit-learn"),
        ("flask", "flask"),
    ]
    for module, label in libraries:
        try:
            __import__(module)
            print(f"   [OK] {label}")
        except ImportError:
            print(f"   [ERROR] {label} not installed")
            all_exist = False

    return all_exist


def print_next_steps():
    """Print next steps."""
    print("\n" + "=" * 70)
    print("Next Steps:")
    print("=" * 70)
    print(
        """
1. If setup is verified:
   python test.py        # Test library installation
   python train.py       # Train the ML model
   python main.py        # Start the web application

2. Open browser:
   http://localhost:5000

3. If dataset is missing:
   - Visit: https://www.kaggle.com
   - Search: "Student Depression Dataset"
   - Download CSV file
   - Place in: dataset/Student Depression Dataset.csv

4. For more information:
   - Read: README.md
   - View: templates/index.html
   - API docs: app.py
"""
    )
    print("=" * 70 + "\n")


if __name__ == "__main__":
    print("\nStarting MindCare AI Setup Verification...\n")

    success = verify_setup()

    if success:
        print("\n[OK] Setup verification completed successfully!")
    else:
        print("\n[WARNING] Some checks failed. Please review the messages above.")
        print("   Run: pip install -r requirements.txt")

    print_next_steps()
