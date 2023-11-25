# General utility functions used across modules

import numpy as np

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

def relu(x):
    """ReLU (Rectified Linear Unit) activation function."""
    return np.maximum(0, x)

def normalize(data, lower=0, upper=1):
    """Normalize data to a specific range."""
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val) * (upper - lower) + lower

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt(np.sum((np.array(point1) - np.array(point2)) ** 2))

def generate_random_weights(size, low=-1.0, high=1.0):
    """Generate a matrix of random weights."""
    return np.random.uniform(low, high, size)

def rolling_average(data, window_size):
    """Calculate the rolling average of a dataset."""
    return np.convolve(data, np.ones(window_size), 'valid') / window_size

def create_time_series(length, time_step):
    """Generate a time series array."""
    return np.arange(0, length * time_step, time_step)

def binarize_data(data, threshold=0.5):
    """Binarize data based on a specified threshold."""
    return np.where(data > threshold, 1, 0)

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum."""
    return max(min_value, min(value, max_value))

def logistic_growth(initial_value, growth_rate, carrying_capacity, time):
    """Model logistic growth."""
    return carrying_capacity / (1 + ((carrying_capacity - initial_value) / initial_value) * np.exp(-growth_rate * time))

def interpolate_linear(x1, y1, x2, y2, x):
    """Linear interpolation between two points."""
    return y1 + (y2 - y1) * ((x - x1) / (x2 - x1))

# Add more utilities as needed
