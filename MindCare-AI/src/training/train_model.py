"""
Model Training Module
Trains machine learning models for stress prediction
"""

import pandas as pd
import numpy as np
import os
import sys
import joblib
import warnings
warnings.filterwarnings('ignore')

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, confusion_matrix, classification_report
)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from xgboost import XGBClassifier
except ImportError:
    XGBClassifier = None

try:
    from lightgbm import LGBMClassifier
except ImportError:
    LGBMClassifier = None

class ModelTrainer:
    """Train and evaluate ML models"""
    
    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.model = None
        self.metrics = {}
        
    def train_random_forest(self, n_estimators=100, max_depth=15):
        """Train Random Forest model"""
        print("\n" + "=" * 70)
        print("🌲 TRAINING RANDOM FOREST MODEL")
        print("=" * 70)
        
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1,
            verbose=1
        )
        
        print("\n🚀 Training in progress...")
        self.model.fit(self.X_train, self.y_train)
        print("✅ Training complete!")
        
        return self.model
    
    def train_xgboost(self):
        """Train XGBoost model"""
        if XGBClassifier is None:
            raise ImportError("xgboost is not installed. Run: pip install xgboost")

        print("\n" + "=" * 70)
        print("⚡ TRAINING XGBOOST MODEL")
        print("=" * 70)
        
        self.model = XGBClassifier(
            max_depth=7,
            learning_rate=0.1,
            n_estimators=100,
            random_state=42,
            n_jobs=-1,
            verbose=1
        )
        
        print("\n🚀 Training in progress...")
        self.model.fit(self.X_train, self.y_train)
        print("✅ Training complete!")
        
        return self.model
    
    def train_lightgbm(self):
        """Train LightGBM model"""
        if LGBMClassifier is None:
            raise ImportError("lightgbm is not installed. Run: pip install lightgbm")

        print("\n" + "=" * 70)
        print("💡 TRAINING LIGHTGBM MODEL")
        print("=" * 70)
        
        self.model = LGBMClassifier(
            num_leaves=31,
            learning_rate=0.1,
            n_estimators=100,
            random_state=42,
            n_jobs=-1,
            verbose=1
        )
        
        print("\n🚀 Training in progress...")
        self.model.fit(self.X_train, self.y_train)
        print("✅ Training complete!")
        
        return self.model
    
    def evaluate_model(self):
        """Evaluate model performance"""
        print("\n" + "=" * 70)
        print("📊 MODEL EVALUATION")
        print("=" * 70)
        
        # Make predictions
        y_pred = self.model.predict(self.X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(self.y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(self.y_test, y_pred, average='weighted', zero_division=0)
        
        # Store metrics
        self.metrics = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'confusion_matrix': confusion_matrix(self.y_test, y_pred).tolist()
        }
        
        # Print results
        print(f"\n✅ Model Performance Metrics:")
        print(f"   Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
        print(f"   Precision: {precision:.4f}")
        print(f"   Recall:    {recall:.4f}")
        print(f"   F1-Score:  {f1:.4f}")
        
        # Print confusion matrix
        print(f"\n📊 Confusion Matrix:")
        cm = confusion_matrix(self.y_test, y_pred)
        print(cm)
        
        # Print classification report
        print(f"\n📋 Classification Report:")
        print(classification_report(self.y_test, y_pred))
        
        return self.metrics
    
    def get_feature_importance(self, feature_names=None, top_n=10):
        """Get feature importance"""
        print("\n" + "=" * 70)
        print("🎯 FEATURE IMPORTANCE")
        print("=" * 70)
        
        if not hasattr(self.model, 'feature_importances_'):
            print("❌ Model does not support feature importance")
            return None
        
        importances = self.model.feature_importances_
        
        if feature_names is None:
            feature_names = [f"Feature_{i}" for i in range(len(importances))]
        
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importances
        }).sort_values('importance', ascending=False)
        
        print(f"\n📊 Top {top_n} Features:")
        for idx, row in importance_df.head(top_n).iterrows():
            bar_length = int(row['importance'] * 50)
            bar = '█' * bar_length
            print(f"   {row['feature']:20} {bar} {row['importance']:.4f}")
        
        return importance_df
    
    def save_model(self, path):
        """Save trained model"""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)
        print(f"\n✅ Model saved to: {path}")


def main():
    """Main execution"""
    try:
        # Load cleaned data
        data_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'data', 'processed', 'cleaned_data.csv'
        )
        
        if not os.path.exists(data_path):
            print(f"\n❌ Cleaned data not found at {data_path}")
            print("   Please run: python src/preprocessing/clean_data.py")
            return
        
        df = pd.read_csv(data_path)
        
        # Prepare features and target
        print("\n" + "=" * 70)
        print("🔧 PREPARING DATA FOR TRAINING")
        print("=" * 70)
        
        # Assuming last column is target
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values
        
        feature_names = df.columns[:-1].tolist()
        target_name = df.columns[-1]
        
        print(f"\n✅ Features: {len(feature_names)}")
        print(f"   {feature_names}")
        print(f"\n✅ Target: {target_name}")
        print(f"   Classes: {sorted(set(y))}")
        
        # Split data
        print("\n" + "=" * 70)
        print("📊 SPLITTING DATA")
        print("=" * 70)
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        print(f"\n✅ Training set: {len(X_train)} samples ({len(X_train)/len(X)*100:.1f}%)")
        print(f"✅ Testing set:  {len(X_test)} samples ({len(X_test)/len(X)*100:.1f}%)")
        
        # Train Random Forest model
        trainer = ModelTrainer(X_train, X_test, y_train, y_test)
        trainer.train_random_forest()
        
        # Evaluate
        metrics = trainer.evaluate_model()
        
        # Feature importance
        importance_df = trainer.get_feature_importance(feature_names)
        
        # Save model
        model_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'models', 'stress_model.pkl'
        )
        trainer.save_model(model_path)
        
        # Print summary
        print("\n" + "=" * 70)
        print("🎉 TRAINING COMPLETE!")
        print("=" * 70)
        print(f"\n✅ Accuracy: {metrics['accuracy']:.4f} ({metrics['accuracy']*100:.2f}%)")
        print(f"✅ Model ready for predictions!")
        print(f"✅ Next step: python src/prediction/predict.py")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
