"""
Data Preprocessing module for MindCare AI
Handles data cleaning, transformation, and preparation
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import os
import sys
from config import DATASET_FILE, SCALER_FILE, TEST_SPLIT, RANDOM_STATE, FEATURE_NAMES

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.feature_names = FEATURE_NAMES
        
    def load_dataset(self, file_path=DATASET_FILE):
        """Load the dataset from CSV file"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset not found at {file_path}")
        
        df = pd.read_csv(file_path)
        print(f"✅ Dataset loaded successfully!")
        print(f"   Shape: {df.shape}")
        print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    
    def check_missing_values(self, df):
        """Check and report missing values"""
        missing = df.isnull().sum()
        if missing.sum() > 0:
            print(f"\n⚠️  Missing values found:")
            print(missing[missing > 0])
            # Fill missing values
            df = df.fillna(df.mean(numeric_only=True))
            print("✅ Missing values filled with mean")
        else:
            print("✅ No missing values found")
        return df
    
    def encode_categorical(self, df, categorical_cols):
        """Encode categorical variables"""
        df_encoded = df.copy()
        
        for col in categorical_cols:
            if col in df_encoded.columns:
                if col not in self.label_encoders:
                    self.label_encoders[col] = LabelEncoder()
                    df_encoded[col] = self.label_encoders[col].fit_transform(df_encoded[col])
                else:
                    df_encoded[col] = self.label_encoders[col].transform(df_encoded[col])
        
        print(f"✅ Encoded {len(categorical_cols)} categorical columns")
        return df_encoded
    
    def normalize_features(self, X):
        """Normalize features using StandardScaler"""
        X_scaled = self.scaler.fit_transform(X)
        print("✅ Features normalized")
        return X_scaled
    
    def save_scaler(self, filepath=SCALER_FILE):
        """Save the scaler for later use"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.scaler, filepath)
        print(f"✅ Scaler saved to {filepath}")
    
    def load_scaler(self, filepath=SCALER_FILE):
        """Load the scaler"""
        if os.path.exists(filepath):
            self.scaler = joblib.load(filepath)
            print(f"✅ Scaler loaded from {filepath}")
            return True
        return False
    
    def preprocess(self, df, categorical_cols=None):
        """Complete preprocessing pipeline"""
        if categorical_cols is None:
            categorical_cols = df.select_dtypes(include=["object", "str"]).columns.tolist()
        
        print("\n" + "=" * 60)
        print("Starting Data Preprocessing")
        print("=" * 60)
        
        # Step 1: Check missing values
        df = self.check_missing_values(df)
        
        # Step 2: Encode categorical variables
        df = self.encode_categorical(df, categorical_cols)
        
        # Step 3: Display statistics
        print(f"\n📊 Dataset Statistics:")
        print(df.describe())
        
        print("\n" + "=" * 60)
        print("✅ Preprocessing completed successfully!")
        print("=" * 60)
        
        return df
    
    def split_data(self, X, y, test_size=TEST_SPLIT, random_state=RANDOM_STATE):
        """Split data into train and test sets"""
        from sklearn.model_selection import train_test_split
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        print(f"\n✅ Data split completed:")
        print(f"   Training set: {X_train.shape[0]} samples")
        print(f"   Testing set: {X_test.shape[0]} samples")
        
        return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    # Example usage
    preprocessor = DataPreprocessor()
    
    try:
        # Load dataset
        df = preprocessor.load_dataset()
        
        # Preprocess
        df_processed = preprocessor.preprocess(df)
        
        print("\n✅ Data preprocessing demo completed!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
