from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd
import numpy as np
from scipy import stats


class StatisticalDataAnalysisTool(BaseTool):
    """
    A tool for performing comprehensive statistical analysis on data. It supports descriptive statistics, hypothesis testing, and other statistical computations.

    This tool is essential for the ExpertDataAnalyst agent to derive insights from numeric and categorical data, facilitating the identification of trends, patterns, and actionable insights.
    """

    data_path: str = Field(
        ..., description="Path to the CSV or Excel file containing the data to be analyzed.")

    def run(self):
        data = pd.read_csv(self.data_path) if self.data_path.endswith('.csv') else pd.read_excel(self.data_path)
        descriptive_stats = data.describe()
        correlation_matrix = data.corr()
        return f"Descriptive Statistics:\n{descriptive_stats}\n\nCorrelation Matrix:\n{correlation_matrix}"
