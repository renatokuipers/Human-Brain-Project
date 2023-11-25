# Tools for measuring and reporting simulation performance

import time
import functools
import tracemalloc
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def timing_decorator(func):
    """Decorator to measure the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {(end_time - start_time):.4f} seconds")
        return result
    return wrapper

def track_memory_usage(func):
    """Decorator to track memory usage of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{func.__name__} used {current / 10**6:.2f} MB with a peak of {peak / 10**6:.2f} MB")
        return result
    return wrapper

def calculate_rmse(y_true, y_pred):
    """Calculate Root Mean Square Error."""
    return mean_squared_error(y_true, y_pred, squared=False)

def calculate_mae(y_true, y_pred):
    """Calculate Mean Absolute Error."""
    return mean_absolute_error(y_true, y_pred)

def calculate_accuracy(y_true, y_pred, threshold=0.5):
    """Calculate accuracy for binary classification."""
    y_pred_binarized = np.where(y_pred > threshold, 1, 0)
    return np.mean(y_true == y_pred_binarized)

# More specialized performance metrics can be added as needed
