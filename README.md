# Statistics and Trends: Global City Temperature Analysis

## 📘 Overview
This project analyzes long-term global temperature trends using the **GlobalLandTemperaturesByCity** dataset.  
It performs statistical computations, data cleaning, and visual exploration to understand temperature variations across time and regions.

The project demonstrates **statistical moment analysis**, **data visualization**, and **trend exploration** using Python, Pandas, Seaborn, and Matplotlib.

---

## 🔍 Key Features
- **Data Preprocessing**: Cleans missing values, converts dates, and creates time-based columns (Year, Month, Decade).  
- **Statistical Analysis**: Calculates four statistical moments for numeric variables:
  - Mean  
  - Variance  
  - Skewness  
  - Kurtosis  
- **Relational Plots**:
  - Line plot showing global temperature trends over years.  
- **Categorical Plots**:
  - Histogram of temperature distribution.  
  - Bar chart of average monthly temperatures.  
  - Pie chart of uncertainty levels.  
- **Statistical Plots**:
  - Correlation heatmap.  
  - Boxplot and violin plot for distribution.  
  - Pairplot for temperature vs uncertainty.  
- **Report Generation**:
  - A short report with summary statistics (`outputs/short_report.txt`).

---

## 🗂 Project Structure
Statistics-and-Trends/
│
├── stats_trends_globalcity.py # Main Python script
├── GlobalLandTemperaturesByCity.csv # Input dataset (not uploaded due to size)
├── outputs/
│ ├── short_report.txt # Generated summary report
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


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/qumrisharooj/Statistics-and-Trends.git
cd Statistics-and-Trends


2. Install Required Libraries
pip install pandas numpy matplotlib seaborn scipy
