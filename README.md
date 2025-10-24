Statistics and Trends: Global City Temperature Analysis
Overview

This project analyzes long-term global temperature trends using the "GlobalLandTemperaturesByCity" dataset. It performs statistical computation, data cleaning, and visual exploration to understand temperature variations across time and regions.

The project demonstrates statistical moment analysis, data visualization, and trend exploration using Python, Pandas, Seaborn, and Matplotlib.

Key Features

Data Preprocessing: Cleans missing values, converts dates, and prepares structured time-based columns (Year, Month, Decade).

Statistical Analysis: Calculates four key statistical moments for all numeric variables:

Mean

Variance

Skewness

Kurtosis

Relational Plots:

Line plot showing global temperature trends over years.

Categorical Plots:

Histogram of temperature distribution.

Bar chart of average monthly temperatures.

Pie chart representing uncertainty levels.

Statistical Plots:

Correlation heatmap.

Boxplot and violin plot for distribution.

Pairplot for temperature vs uncertainty relationships.

Report Generation:

Generates a short summary report with key findings (outputs/short_report.txt).

Project Structure

Statistics-and-Trends/
│
├── stats_trends_globalcity.py # Main Python script
├── GlobalLandTemperaturesByCity.csv # Input dataset (not uploaded due to size)
├── outputs/
│ ├── short_report.txt # Auto-generated report
├── plots/
│ ├── relational_plot_trend.png
│ ├── categorical_hist.png
│ ├── categorical_bar.png
│ ├── categorical_pie.png
│ ├── stat_heatmap.png
│ ├── stat_boxplot.png
│ ├── stat_violin.png
│ ├── stat_pairplot.png
└── README.md # Project documentation

Installation & Setup

Clone the Repository:
git clone https://github.com/qumrisharooj/Statistics-and-Trends.git

cd Statistics-and-Trends

Install Required Libraries:
pip install pandas numpy matplotlib seaborn scipy

Add Dataset:
Download the "GlobalLandTemperaturesByCity.csv" dataset from Kaggle and place it in the project’s root directory.

Run the Script:
python stats_trends_globalcity.py

This will preprocess the dataset, compute statistical metrics, generate visual plots in the "plots" folder, and create a textual report in the "outputs" folder.

Sample Output

Relational Plot:
Shows average global temperature trend across years.

Statistical Report:
Climate Data Analysis Report

Rows after cleaning: 857654
Numeric columns analyzed: AverageTemperature, AverageTemperatureUncertainty

Statistical moments:
variable mean variance skewness kurtosis_excess
AverageTemperature 12.34 22.56 0.47 -0.68
AverageTemperatureUncertainty 1.25 0.22 1.12 0.35

Technologies Used

Python 3.x

Pandas – Data cleaning & manipulation

NumPy – Numerical computation

Matplotlib / Seaborn – Data visualization

SciPy – Statistical analysis

Learning Outcomes

Understanding and application of descriptive statistics

Hands-on experience with data preprocessing

Visualization of trends, categories, and statistical relationships

Development of a complete data analysis pipeline

License

This project is released under the MIT License.
