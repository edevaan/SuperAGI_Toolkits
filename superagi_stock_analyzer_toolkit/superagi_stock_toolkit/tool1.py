## tool1.py
"""
This module provides additional data manipulation tools that complement the Pandas library.
These tools are designed to be used within the SuperAGI stock analysis toolkit.
"""

# Since we need to ensure there are no circular imports, we only import what's necessary.
import pandas as pd

def fill_missing_data(dataframe: pd.DataFrame, method: str = 'ffill') -> pd.DataFrame:
    """
    Fills missing data in a DataFrame using the specified method.

    Parameters:
    - dataframe: pd.DataFrame - The DataFrame with missing data to fill.
    - method: str - The method to use for filling missing data. Default is forward fill ('ffill').

    Returns:
    - pd.DataFrame - The DataFrame with missing data filled.
    """
    # Validate input parameters
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The 'dataframe' parameter must be an instance of pd.DataFrame.")
    if method not in ['ffill', 'bfill', 'mean', 'median']:
        raise ValueError("The 'method' parameter must be one of 'ffill', 'bfill', 'mean', 'median'.")

    # Apply the specified method to fill missing data
    if method == 'ffill':
        return dataframe.ffill()
    elif method == 'bfill':
        return dataframe.bfill()
    elif method == 'mean':
        return dataframe.fillna(dataframe.mean())
    elif method == 'median':
        return dataframe.fillna(dataframe.median())

def remove_outliers(dataframe: pd.DataFrame, column: str, method: str = 'IQR') -> pd.DataFrame:
    """
    Removes outliers from a specific column in a DataFrame using the specified method.

    Parameters:
    - dataframe: pd.DataFrame - The DataFrame from which to remove outliers.
    - column: str - The name of the column from which to remove outliers.
    - method: str - The method to use for outlier detection. Default is Interquartile Range (IQR).

    Returns:
    - pd.DataFrame - The DataFrame with outliers removed.
    """
    # Validate input parameters
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The 'dataframe' parameter must be an instance of pd.DataFrame.")
    if column not in dataframe.columns:
        raise KeyError(f"The 'column' parameter must be one of the DataFrame's columns. Available columns: {dataframe.columns.tolist()}")
    if method not in ['IQR', 'Z-score']:
        raise ValueError("The 'method' parameter must be one of 'IQR', 'Z-score'.")

    # Calculate the IQR or Z-score and filter out the outliers
    if method == 'IQR':
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]
    elif method == 'Z-score':
        from scipy import stats
        z_scores = stats.zscore(dataframe[column])
        abs_z_scores = abs(z_scores)
        filtered_entries = (abs_z_scores < 3)
        return dataframe[filtered_entries]

# Additional helper functions can be added here as needed to support data manipulation tasks.
