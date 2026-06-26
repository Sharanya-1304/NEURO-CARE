"""
Model Training Script for MindCare AI
This script trains the ML model on the dataset
"""

import sys
import os
import pandas as pd
from data_preprocessing import DataPreprocessor
from model import StressModel
from config import DATASET_FILE

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    """Main training function"""
    print("\n" + "=" * 70)
    print("MindCare AI - Model Training")
    print("=" * 70)
    
    try:
        # Initialize components
        preprocessor = DataPreprocessor()
        stress_model = StressModel()
        
        # Check if dataset exists
        if not os.path.exists(DATASET_FILE):
            print("\n❌ Error: Dataset not found!")
            print(f"   Expected location: {DATASET_FILE}")
            print("\n📥 Please download the dataset from Kaggle:")
            print("   1. Go to: https://www.kaggle.com")
            print("   2. Search for: 'Student Depression Dataset'")
            print("   3. Download the CSV file")
            print(f"   4. Place it in: {os.path.dirname(DATASET_FILE)}")
            return False
        
        print("\n✅ Dataset found!")
        
        # Step 1: Load dataset
        print("\n" + "-" * 70)
        print("Step 1: Loading Dataset")
        print("-" * 70)
        df = preprocessor.load_dataset()
        
        # Step 2: Preprocess data
        print("\n" + "-" * 70)
        print("Step 2: Preprocessing Data")
        print("-" * 70)
        df_processed = preprocessor.preprocess(df)
        
        # Step 3: Prepare features and target
        print("\n" + "-" * 70)
        print("Step 3: Preparing Features and Target")
        print("-" * 70)
        
        # Assuming last column is target
        feature_names = df_processed.columns[:-1].tolist()
        X = df_processed.iloc[:, :-1].values
        y = df_processed.iloc[:, -1].values
        
        print(f"✅ Features shape: {X.shape}")
        print(f"✅ Target shape: {y.shape}")
        print(f"✅ Classes: {sorted(set(y))}")
        
        # Step 4: Normalize features
        print("\n" + "-" * 70)
        print("Step 4: Normalizing Features")
        print("-" * 70)
        X_scaled = preprocessor.normalize_features(X)
        preprocessor.save_scaler()
        
        # Step 5: Split data
        print("\n" + "-" * 70)
        print("Step 5: Splitting Data")
        print("-" * 70)
        X_train, X_test, y_train, y_test = preprocessor.split_data(X_scaled, y)
        
        # Step 6: Train model
        print("\n" + "-" * 70)
        print("Step 6: Training Model")
        print("-" * 70)
        stress_model.train(X_train, y_train)
        
        # Step 7: Evaluate model
        print("\n" + "-" * 70)
        print("Step 7: Evaluating Model")
        print("-" * 70)
        metrics = stress_model.evaluate(X_test, y_test)
        
        # Step 8: Feature importance
        print("\n" + "-" * 70)
        print("Step 8: Feature Importance")
        print("-" * 70)
        importance_df = stress_model.get_feature_importance(feature_names)
        
        # Step 9: Save model
        print("\n" + "-" * 70)
        print("Step 9: Saving Model")
        print("-" * 70)
        stress_model.save_model()
        
        # Summary
        print("\n" + "=" * 70)
        print("🎉 MODEL TRAINING COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        
        print("\n📊 Training Summary:")
        print(f"   • Dataset: {df.shape[0]} samples")
        print(f"   • Training samples: {len(X_train)}")
        print(f"   • Testing samples: {len(X_test)}")
        print(f"   • Accuracy: {metrics['accuracy']:.4f}")
        print(f"   • F1-Score: {metrics['f1_score']:.4f}")
        
        print("\n✅ Model ready for predictions!")
        print("🚀 Run 'python main.py' to start the application")
        print("=" * 70 + "\n")
        
        return True
        
    except FileNotFoundError as e:
        print(f"\n❌ File Error: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error during training: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
