## tools.py
"""
This module contains a collection of tools for data visualization and additional data analysis functions.
These tools are designed to be used within the SuperAGI stock analysis toolkit.
"""

# Import necessary modules from third-party packages
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

class VisualizationTools:
    """
    This class provides methods for visualizing data using Matplotlib and Plotly.
    """

    @staticmethod
    def plot_line_chart(dataframe: pd.DataFrame, x_column: str, y_column: str, title: str = "Line Chart") -> None:
        """
        Plots a line chart using Matplotlib.

        Parameters:
        - dataframe: pd.DataFrame - The DataFrame containing the data to plot.
        - x_column: str - The name of the column to be used as the x-axis.
        - y_column: str - The name of the column to be used as the y-axis.
        - title: str - The title of the chart. Default is "Line Chart".
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("The 'dataframe' parameter must be an instance of pd.DataFrame.")
        if x_column not in dataframe.columns or y_column not in dataframe.columns:
            raise KeyError("The 'x_column' and 'y_column' parameters must be among the DataFrame's columns.")

        plt.figure(figsize=(10, 5))
        plt.plot(dataframe[x_column], dataframe[y_column], marker='o')
        plt.title(title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_bar_chart(dataframe: pd.DataFrame, x_column: str, y_column: str, title: str = "Bar Chart") -> None:
        """
        Plots a bar chart using Plotly.

        Parameters:
        - dataframe: pd.DataFrame - The DataFrame containing the data to plot.
        - x_column: str - The name of the column to be used as the x-axis.
        - y_column: str - The name of the column to be used as the y-axis.
        - title: str - The title of the chart. Default is "Bar Chart".
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("The 'dataframe' parameter must be an instance of pd.DataFrame.")
        if x_column not in dataframe.columns or y_column not in dataframe.columns:
            raise KeyError("The 'x_column' and 'y_column' parameters must be among the DataFrame's columns.")

        fig = px.bar(dataframe, x=x_column, y=y_column, title=title)
        fig.show()

# Additional visualization and analysis tools can be added here as needed to support the project's requirements.
