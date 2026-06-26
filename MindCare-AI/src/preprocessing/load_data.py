"""
Data Loading Module
Loads and explores the dataset
"""

import pandas as pd
import numpy as np
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class DataLoader:
    """Load and explore dataset"""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.raw_data = None
        
    def load_data(self):
        """Load dataset from CSV"""
        print("\n" + "=" * 70)
        print("📂 LOADING DATASET")
        print("=" * 70)
        
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Dataset not found at {self.file_path}")
        
        self.df = pd.read_csv(self.file_path)
        self.raw_data = self.df.copy()
        
        print(f"\n✅ Dataset loaded successfully!")
        print(f"   📊 Shape: {self.df.shape}")
        print(f"   📈 Rows: {self.df.shape[0]}")
        print(f"   📋 Columns: {self.df.shape[1]}")
        
        return self.df
    
    def explore_data(self):
        """Explore dataset structure and statistics"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        print("\n" + "=" * 70)
        print("🔍 DATASET EXPLORATION")
        print("=" * 70)
        
        # Display first rows
        print("\n📋 First 5 Rows:")
        print(self.df.head())
        
        # Display data types
        print("\n📊 Data Types:")
        print(self.df.dtypes)
        
        # Display basic statistics
        print("\n📈 Basic Statistics:")
        print(self.df.describe())
        
        # Display info
        print("\n📝 Dataset Info:")
        self.df.info()
        
        return self.df
    
    def check_missing_values(self):
        """Check for missing values"""
        print("\n" + "=" * 70)
        print("❓ MISSING VALUES ANALYSIS")
        print("=" * 70)
        
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df)) * 100
        
        missing_df = pd.DataFrame({
            'Column': missing.index,
            'Missing_Count': missing.values,
            'Missing_Percent': missing_percent.values
        })
        
        if missing_df[missing_df['Missing_Count'] > 0].empty:
            print("\n✅ No missing values found!")
        else:
            print("\n⚠️  Missing Values Detected:")
            print(missing_df[missing_df['Missing_Count'] > 0])
        
        return missing_df
    
    def check_duplicates(self):
        """Check for duplicate rows"""
        print("\n" + "=" * 70)
        print("🔁 DUPLICATE ANALYSIS")
        print("=" * 70)
        
        duplicates = self.df.duplicated().sum()
        
        if duplicates == 0:
            print(f"✅ No duplicate rows found!")
        else:
            print(f"⚠️  Found {duplicates} duplicate rows")
        
        return duplicates
    
    def analyze_columns(self):
        """Analyze each column"""
        print("\n" + "=" * 70)
        print("📊 COLUMN ANALYSIS")
        print("=" * 70)
        
        for column in self.df.columns:
            print(f"\n🔹 Column: {column}")
            print(f"   Data Type: {self.df[column].dtype}")
            print(f"   Non-null Count: {self.df[column].notna().sum()}")
            
            if self.df[column].dtype in ['float64', 'int64']:
                print(f"   Min: {self.df[column].min()}")
                print(f"   Max: {self.df[column].max()}")
                print(f"   Mean: {self.df[column].mean():.2f}")
                print(f"   Unique Values: {self.df[column].nunique()}")
            else:
                print(f"   Unique Values: {self.df[column].nunique()}")
                print(f"   Categories: {self.df[column].unique()[:5]}")
    
    def get_summary(self):
        """Get complete summary"""
        print("\n" + "=" * 70)
        print("📊 DATASET SUMMARY")
        print("=" * 70)
        
        self.explore_data()
        self.check_missing_values()
        self.check_duplicates()
        self.analyze_columns()
        
        return self.df


def main():
    """Main execution"""
    try:
        # Define file path
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'data', 'raw', 'Student Depression Dataset.csv'
        )
        
        # Load and explore data
        loader = DataLoader(file_path)
        df = loader.load_data()
        loader.get_summary()
        
        print("\n" + "=" * 70)
        print("✅ Dataset loading complete!")
        print("=" * 70 + "\n")
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print("\n📥 Please download the dataset from Kaggle:")
        print("   1. Visit: https://www.kaggle.com/datasets")
        print("   2. Search: 'Student Depression Dataset'")
        print("   3. Download CSV file")
        print("   4. Place in: data/raw/")


if __name__ == '__main__':
    main()
