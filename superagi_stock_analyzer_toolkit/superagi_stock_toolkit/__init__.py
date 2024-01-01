"""
This module initializes the Python package for the SuperAGI stock analysis toolkit.
It sets up shared constants and configurations used across multiple modules within the project.
"""

# Define shared constants and configurations
DEFAULT_AGENT_ID = 'default_agent'
FILE_PATH = 'data/stock_data.csv'

# Import necessary modules from the standard library
import os

# Set up environment variables if needed
os.environ.setdefault('SUPERAGI_API_KEY', 'your-api-key')

# Import necessary modules from third-party packages
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn import model_selection, metrics
import superagi

# Define a base configuration class to hold common settings
class Config:
    AGENT_ID = os.getenv('SUPERAGI_AGENT_ID', DEFAULT_AGENT_ID)
    DATA_FILE_PATH = os.getenv('SUPERAGI_DATA_FILE_PATH', FILE_PATH)
    API_KEY = os.getenv('SUPERAGI_API_KEY')

# Ensure that the package is initialized with default configurations
config = Config()
