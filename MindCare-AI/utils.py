"""
Utility functions for MindCare AI
"""

import os
import json
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
from config import DATASET_DIR, MODEL_DIR


def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [DATASET_DIR, MODEL_DIR]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✅ Directories created/verified")


def load_json(filepath):
    """Load JSON file"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None


def save_json(data, filepath):
    """Save data to JSON file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved to {filepath}")


def get_timestamp():
    """Get current timestamp"""
    return datetime.now().isoformat()


def format_number(value, decimals=2):
    """Format number with specified decimals"""
    return round(float(value), decimals)


def validate_input(data, required_fields):
    """Validate input data"""
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
        try:
            float(data[field])
        except (ValueError, TypeError):
            return False, f"Invalid value for {field}: {data[field]}"
    return True, "Valid"


def calculate_statistics(values):
    """Calculate basic statistics"""
    if not values:
        return None
    
    return {
        'mean': float(np.mean(values)),
        'median': float(np.median(values)),
        'std': float(np.std(values)),
        'min': float(np.min(values)),
        'max': float(np.max(values))
    }


def normalize_value(value, min_val=0, max_val=1):
    """Normalize value between min and max"""
    return (value - min_val) / (max_val - min_val)


def denormalize_value(value, min_val=0, max_val=1):
    """Denormalize value"""
    return value * (max_val - min_val) + min_val


class DataCache:
    """Simple data caching utility"""
    
    def __init__(self):
        self.cache = {}
    
    def set(self, key, value, ttl=None):
        """Store value in cache"""
        self.cache[key] = {
            'value': value,
            'timestamp': datetime.now(),
            'ttl': ttl
        }
    
    def get(self, key):
        """Retrieve value from cache"""
        if key not in self.cache:
            return None
        
        entry = self.cache[key]
        
        # Check if expired
        if entry['ttl']:
            elapsed = (datetime.now() - entry['timestamp']).total_seconds()
            if elapsed > entry['ttl']:
                del self.cache[key]
                return None
        
        return entry['value']
    
    def clear(self):
        """Clear all cache"""
        self.cache.clear()


# Global cache instance
cache = DataCache()


if __name__ == '__main__':
    # Test utilities
    print("Testing utilities...")
    
    # Test directory creation
    create_directories()
    
    # Test number formatting
    print(f"Format 3.14159: {format_number(3.14159, 2)}")
    
    # Test statistics
    values = [1, 2, 3, 4, 5]
    stats = calculate_statistics(values)
    print(f"Statistics: {stats}")
    
    # Test cache
    cache.set('test', 'value')
    print(f"Cache get: {cache.get('test')}")
    
    print("✅ All utilities working correctly!")
