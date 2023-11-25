# Utilities for generating plots, graphs, and other visual data representations

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_time_series(time, values, title="Time Series Plot", xlabel="Time", ylabel="Value"):
    """Plot a time series."""
    plt.figure(figsize=(10, 6))
    plt.plot(time, values, label='Values over Time')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_histogram(data, bins=20, title="Histogram", xlabel="Values", ylabel="Frequency"):
    """Plot a histogram."""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_scatter(x, y, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    """Plot a scatter plot."""
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.7, edgecolors='w', s=100)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_correlation_matrix(matrix, title="Correlation Matrix"):
    """Plot a correlation matrix."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title(title)
    plt.show()

def plot_bar_chart(categories, values, title="Bar Chart", xlabel="Categories", ylabel="Values"):
    """Plot a bar chart."""
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

def plot_pie_chart(labels, sizes, title="Pie Chart"):
    """Plot a pie chart."""
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(title)
    plt.show()

# Additional visualization functions can be added as needed
