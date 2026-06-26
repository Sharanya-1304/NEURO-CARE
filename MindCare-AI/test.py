"""
Test file to verify all required libraries are installed.
"""

import sys


print("=" * 60)
print("Testing MindCare AI - Library Installation")
print("=" * 60)

libraries = {
    "pandas": "pandas",
    "numpy": "numpy",
    "sklearn": "scikit-learn",
    "flask": "Flask",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "joblib": "joblib",
    "plotly": "plotly",
}

failed = []
passed = []

for module, name in libraries.items():
    try:
        __import__(module)
        print(f"[OK] {name:20} - Installed successfully")
        passed.append(name)
    except ImportError:
        print(f"[MISSING] {name:20} - NOT installed")
        failed.append(name)

print("=" * 60)
print(f"\n[OK] Passed: {len(passed)}/{len(libraries)}")
print(f"[MISSING] Failed: {len(failed)}/{len(libraries)}")

if failed:
    print(f"\nMissing libraries: {', '.join(failed)}")
    print("\nInstall missing libraries with:")
    print(f"pip install {' '.join(failed)}")
    sys.exit(1)

print("\nAll libraries installed successfully!")
print("[OK] MindCare AI environment is ready!")
sys.exit(0)
