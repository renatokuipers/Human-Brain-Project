# Functions for data import, export, and manipulation

import pandas as pd
import numpy as np
import json
import csv

def read_csv(file_path, delimiter=','):
    """Read data from a CSV file."""
    try:
        return pd.read_csv(file_path, delimiter=delimiter)
    except Exception as e:
        # Handle exceptions (like file not found, parse error, etc.)
        raise

def write_csv(data, file_path, delimiter=','):
    """Write data to a CSV file."""
    try:
        data.to_csv(file_path, index=False, sep=delimiter)
    except Exception as e:
        # Handle exceptions (like IO error)
        raise

def read_json(file_path):
    """Read data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        # Handle exceptions (like file not found, JSON decode error, etc.)
        raise

def write_json(data, file_path):
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        # Handle exceptions
        raise

def convert_df_to_numpy(df):
    """Convert a Pandas DataFrame to a NumPy array."""
    return df.to_numpy()

def normalize_data(data):
    """Normalize data for processing."""
    # Placeholder for a normalization function
    return (data - np.mean(data)) / np.std(data)

def preprocess_data(data):
    """Preprocess data for simulation use."""
    # Placeholder for a preprocessing function
    # This could include normalization, handling missing values, etc.
    return data

def split_data(data, test_size=0.2):
    """Split data into training and testing sets."""
    # Placeholder for a data splitting function
    # This is particularly useful for machine learning applications
    from sklearn.model_selection import train_test_split
    return train_test_split(data, test_size=test_size)

# Additional data handling functions can be added here as required
