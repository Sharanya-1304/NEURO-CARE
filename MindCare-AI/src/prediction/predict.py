"""
Prediction Engine
Makes predictions using trained model
"""

import pandas as pd
import numpy as np
import os
import sys
import joblib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class PredictionEngine:
    """Make predictions using trained model"""
    
    def __init__(self, model_path):
        self.model = None
        self.model_path = model_path
        self.load_model()
        
    def load_model(self):
        """Load trained model"""
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model not found at {self.model_path}")
        
        self.model = joblib.load(self.model_path)
        print(f"✅ Model loaded: {self.model_path}")
    
    def predict(self, X):
        """Make predictions
        
        Args:
            X: Input features (numpy array or list)
        
        Returns:
            predictions: Predicted classes
            probabilities: Prediction probabilities
        """
        if isinstance(X, list):
            X = np.array(X)
        
        # Reshape if single sample
        if X.ndim == 1:
            X = X.reshape(1, -1)
        
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)
        
        return predictions, probabilities
    
    def predict_with_confidence(self, X, stress_levels=['Low Stress', 'Medium Stress', 'High Stress']):
        """Make predictions with confidence scores
        
        Returns:
            result: Dictionary with prediction and confidence
        """
        predictions, probabilities = self.predict(X)
        
        results = []
        for i, pred in enumerate(predictions):
            confidence = max(probabilities[i]) * 100
            
            result = {
                'prediction': stress_levels[pred] if pred < len(stress_levels) else f'Class {pred}',
                'confidence': round(confidence, 2),
                'probabilities': {
                    stress_levels[j]: round(prob * 100, 2) 
                    for j, prob in enumerate(probabilities[i])
                }
            }
            results.append(result)
        
        return results[0] if len(results) == 1 else results


def main():
    """Main execution - Example predictions"""
    try:
        # Load model
        model_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'models', 'stress_model.pkl'
        )
        
        if not os.path.exists(model_path):
            print(f"\n❌ Model not found at {model_path}")
            print("   Please train the model first: python src/training/train_model.py")
            return
        
        engine = PredictionEngine(model_path)
        
        # Example predictions
        print("\n" + "=" * 70)
        print("🔮 MAKING PREDICTIONS")
        print("=" * 70)
        
        # Example 1: Low stress person
        print("\n\n📊 Example 1: Person with Low Stress")
        print("-" * 70)
        sample1 = [
            25,      # Age
            0,       # Gender (0=Male)
            8,       # Sleep Hours
            2,       # Study Pressure
            2,       # Work Pressure
            1,       # Financial Stress
            3,       # Anxiety
            5        # Social Activity
        ]
        
        result1 = engine.predict_with_confidence(sample1)
        print(f"   Stress Level: {result1['prediction']}")
        print(f"   Confidence: {result1['confidence']}%")
        print(f"   Breakdown:")
        for level, prob in result1['probabilities'].items():
            print(f"      {level}: {prob}%")
        
        # Example 2: High stress person
        print("\n\n📊 Example 2: Person with High Stress")
        print("-" * 70)
        sample2 = [
            30,      # Age
            1,       # Gender (1=Female)
            4,       # Sleep Hours
            5,       # Study Pressure
            5,       # Work Pressure
            4,       # Financial Stress
            8,       # Anxiety
            1        # Social Activity
        ]
        
        result2 = engine.predict_with_confidence(sample2)
        print(f"   Stress Level: {result2['prediction']}")
        print(f"   Confidence: {result2['confidence']}%")
        print(f"   Breakdown:")
        for level, prob in result2['probabilities'].items():
            print(f"      {level}: {prob}%")
        
        # Example 3: Medium stress person
        print("\n\n📊 Example 3: Person with Medium Stress")
        print("-" * 70)
        sample3 = [
            28,      # Age
            0,       # Gender
            6,       # Sleep Hours
            3,       # Study Pressure
            3,       # Work Pressure
            2,       # Financial Stress
            5,       # Anxiety
            3        # Social Activity
        ]
        
        result3 = engine.predict_with_confidence(sample3)
        print(f"   Stress Level: {result3['prediction']}")
        print(f"   Confidence: {result3['confidence']}%")
        print(f"   Breakdown:")
        for level, prob in result3['probabilities'].items():
            print(f"      {level}: {prob}%")
        
        print("\n" + "=" * 70)
        print("✅ Prediction engine working correctly!")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
