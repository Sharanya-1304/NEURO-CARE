"""
Data Cleaning Module
Cleans and preprocesses the dataset
"""

import pandas as pd
import numpy as np
import os
import sys
from sklearn.preprocessing import LabelEncoder
import joblib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class DataCleaner:
    """Clean and preprocess data"""
    
    def __init__(self, df):
        self.df = df.copy()
        self.label_encoders = {}
        self.numeric_columns = []
        self.categorical_columns = []
        self.target_column = None
        
    def identify_column_types(self):
        """Identify numeric and categorical columns"""
        print("\n" + "=" * 70)
        print("🔍 IDENTIFYING COLUMN TYPES")
        print("=" * 70)
        
        self.numeric_columns = self.df.select_dtypes(
            include=['int64', 'float64']
        ).columns.tolist()
        
        self.categorical_columns = self.df.select_dtypes(
            include=['object']
        ).columns.tolist()
        
        print(f"\n✅ Numeric Columns ({len(self.numeric_columns)}):")
        print(f"   {self.numeric_columns}")
        
        print(f"\n✅ Categorical Columns ({len(self.categorical_columns)}):")
        print(f"   {self.categorical_columns}")
        
        return self.numeric_columns, self.categorical_columns
    
    def remove_duplicates(self):
        """Remove duplicate rows"""
        print("\n" + "=" * 70)
        print("🔄 REMOVING DUPLICATES")
        print("=" * 70)
        
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        
        removed = before - after
        
        if removed == 0:
            print(f"✅ No duplicates found!")
        else:
            print(f"✅ Removed {removed} duplicate rows")
            print(f"   Before: {before} rows")
            print(f"   After: {after} rows")
        
        return self.df
    
    def handle_missing_values(self, strategy='mean'):
        """Handle missing values
        
        Args:
            strategy: 'mean' for numeric, 'mode' for categorical
        """
        print("\n" + "=" * 70)
        print("🔧 HANDLING MISSING VALUES")
        print("=" * 70)
        
        missing_before = self.df.isnull().sum().sum()
        
        if missing_before == 0:
            print("✅ No missing values found!")
            return self.df
        
        # Fill numeric columns
        for col in self.numeric_columns:
            if self.df[col].isnull().sum() > 0:
                if strategy == 'mean':
                    self.df[col].fillna(self.df[col].mean(), inplace=True)
                    print(f"✅ Filled {col} with mean value")
        
        # Fill categorical columns
        for col in self.categorical_columns:
            if self.df[col].isnull().sum() > 0:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
                print(f"✅ Filled {col} with mode value")
        
        missing_after = self.df.isnull().sum().sum()
        print(f"\n📊 Missing values before: {missing_before}")
        print(f"📊 Missing values after: {missing_after}")
        
        return self.df
    
    def encode_categorical_variables(self):
        """Encode categorical variables to numeric"""
        print("\n" + "=" * 70)
        print("🔤 ENCODING CATEGORICAL VARIABLES")
        print("=" * 70)
        
        for col in self.categorical_columns:
            if col != self.target_column:
                encoder = LabelEncoder()
                self.df[col] = encoder.fit_transform(self.df[col])
                self.label_encoders[col] = encoder
                
                print(f"✅ Encoded {col}")
                print(f"   Mapping: {dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))}")
        
        return self.df
    
    def remove_outliers(self, method='iqr', threshold=1.5):
        """Remove outliers using IQR method
        
        Args:
            method: 'iqr' or 'zscore'
            threshold: multiplier for IQR (1.5 is standard)
        """
        print("\n" + "=" * 70)
        print("📊 REMOVING OUTLIERS (IQR Method)")
        print("=" * 70)
        
        before = len(self.df)
        
        for col in self.numeric_columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            
            # Count outliers
            outliers = len(self.df[
                (self.df[col] < lower_bound) | (self.df[col] > upper_bound)
            ])
            
            if outliers > 0:
                print(f"✅ {col}: {outliers} outliers detected")
                self.df = self.df[
                    (self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)
                ]
        
        after = len(self.df)
        removed = before - after
        
        print(f"\n📊 Rows removed: {removed}")
        print(f"   Before: {before}")
        print(f"   After: {after}")
        
        return self.df
    
    def standardize_labels(self, col_mapping=None):
        """Standardize categorical labels"""
        print("\n" + "=" * 70)
        print("🏷️  STANDARDIZING LABELS")
        print("=" * 70)
        
        if col_mapping is None:
            col_mapping = {}
        
        for col, mapping in col_mapping.items():
            if col in self.df.columns:
                self.df[col] = self.df[col].map(mapping)
                print(f"✅ Standardized {col}")
        
        return self.df
    
    def get_cleaned_data(self, target_column=None):
        """Get fully cleaned dataset"""
        self.target_column = target_column
        
        print("\n" + "=" * 70)
        print("🧹 COMPLETE DATA CLEANING PIPELINE")
        print("=" * 70)
        
        self.identify_column_types()
        self.remove_duplicates()
        self.handle_missing_values()
        self.encode_categorical_variables()
        self.remove_outliers()
        
        print("\n" + "=" * 70)
        print("✅ DATA CLEANING COMPLETE")
        print("=" * 70)
        print(f"\n📊 Final Dataset Shape: {self.df.shape}")
        
        return self.df
    
    def save_cleaned_data(self, output_path):
        """Save cleaned dataset"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path, index=False)
        print(f"\n✅ Cleaned data saved to: {output_path}")
        
    def save_encoders(self, output_dir):
        """Save label encoders for later use"""
        os.makedirs(output_dir, exist_ok=True)
        
        for col, encoder in self.label_encoders.items():
            path = os.path.join(output_dir, f"{col}_encoder.pkl")
            joblib.dump(encoder, path)
        
        print(f"✅ Encoders saved to: {output_dir}")


def main():
    """Main execution"""
    try:
        from load_data import DataLoader
        
        # Load data
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'data', 'raw', 'Student Depression Dataset.csv'
        )
        
        loader = DataLoader(file_path)
        df = loader.load_data()
        
        # Clean data
        cleaner = DataCleaner(df)
        cleaned_df = cleaner.get_cleaned_data(target_column='Depression')
        
        # Save cleaned data
        output_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'data', 'processed', 'cleaned_data.csv'
        )
        
        cleaner.save_cleaned_data(output_path)
        
        # Save encoders
        encoder_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'models', 'encoders'
        )
        cleaner.save_encoders(encoder_dir)
        
        print("\n✅ Data cleaning pipeline complete!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
