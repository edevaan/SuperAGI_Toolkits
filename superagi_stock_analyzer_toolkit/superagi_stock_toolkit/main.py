## main.py
"""
This module serves as the entry point of the SuperAGI stock analysis application.
It orchestrates the flow of the program, utilizing the SuperAGI toolkit to analyze stock data,
generate insights, and render a dashboard.
"""

from __init__ import config
from toolname_toolkit import SuperAGIToolkit
from superagi import SuperAGIAgents, SuperAGIUI
import pandas as pd

def main():
    # Initialize the SuperAGI toolkit
    toolkit = SuperAGIToolkit()

    # Read stock data from CSV file
    data = pd.read_csv(config.DATA_FILE_PATH)

    # Analyze stock data using the SuperAGI toolkit
    analyzed_data = toolkit.analyze_stock_data(data)

    # Generate insights from the analyzed data
    insights = toolkit.generate_insights(analyzed_data)

    # Get an agent from SuperAGI agents
    agents = SuperAGIAgents()
    agent = agents.get_agent(config.AGENT_ID)

    # Render dashboard with insights using the SuperAGI UI
    ui = SuperAGIUI()
    ui.render_dashboard(insights)

    # Print a simple confirmation that the process has completed
    print("Dashboard has been successfully displayed.")

# Check if the script is run as the main program and call the main function
if __name__ == "__main__":
    main()
