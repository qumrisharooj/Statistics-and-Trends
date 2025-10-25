"""
stats_trends_globalcity.py

Dataset: GlobalLandTemperaturesByCity.csv
Performs:
 - Preprocessing & cleaning
 - Compute 4 moments (mean, variance, skewness, kurtosis)
 - Relational plot (trend)
 - Categorical plots (hist/bar/pie)
 - Statistical plots (heatmap/box/violin/pair)
 - Generates summary statistics and a short report
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ===================================================
# SETTINGS
# ===================================================
DATA_FILE = "GlobalLandTemperaturesByCity.csv"
OUTPUT_DIR = "outputs"
PLOTS_DIR = "plots"
np.random.seed(42)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)
sns.set(style="whitegrid")

# ===================================================
# HELPERS
# ===================================================
def read_data(path):
    if not os.path.exists(path):
        print(f"ERROR: {path} not found. Place the CSV file in working directory.")
        sys.exit(1)
    df = pd.read_csv(path)
    print(f"Loaded {path}: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def basic_preprocess(df):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]

    if 'dt' not in df.columns:
        raise ValueError("Expected a 'dt' column for date.")
    df['dt'] = pd.to_datetime(df['dt'], errors='coerce')
    df = df.dropna(subset=['dt']).drop_duplicates()

    df['Year'] = df['dt'].dt.year.astype('Int64')
    df['Month'] = df['dt'].dt.month.astype('Int64')
    df['Decade'] = (df['Year'] // 10 * 10).astype('Int64')

    if 'AverageTemperature' in df.columns:
        df['AverageTemperature'] = (
            df.groupby('City')['AverageTemperature']
            .transform(lambda s: s.interpolate(limit_direction='both'))
        )
        df['AverageTemperature'].fillna(df['AverageTemperature'].median(), inplace=True)

    return df

def compute_moments_for_numeric(df):
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [c for c in numeric_cols if c not in ['Year', 'Month', 'Decade']]
    rows = []
    for c in numeric_cols:
        s = pd.to_numeric(df[c], errors='coerce').dropna()
        if s.empty: continue
        rows.append({
            'variable': c,
            'mean': s.mean(),
            'variance': s.var(ddof=0),
            'skewness': stats.skew(s),
            'kurtosis_excess': stats.kurtosis(s, fisher=True)
        })
    return pd.DataFrame(rows)

# ===================================================
# PLOTTING FUNCTIONS
# ===================================================
def plot_relational(df):
    """Line plot of global average temperature trend"""
    outpath = os.path.join(PLOTS_DIR, "relational_plot_trend.png")
    plt.figure(figsize=(12,6))
    global_trend = df.groupby("Year")["AverageTemperature"].mean().reset_index()
    sns.lineplot(x="Year", y="AverageTemperature", data=global_trend, color="blue")
    plt.title("Relational Plot: Global Average Temperature Over Time")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f"Saved relational plot -> {outpath}")

def plot_categorical(df):
    """Histogram, Bar, and Pie Charts"""
    # -----> Histogram
    plt.figure(figsize=(10,6))
    sns.histplot(df["AverageTemperature"], bins=30, kde=True, color="orange")
    plt.title("Histogram of Average Temperature")
    plt.xlabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "categorical_hist.png"))
    plt.close()

    # -----> Bar chart by month
    monthly = df.groupby("Month")["AverageTemperature"].mean().reset_index()
    plt.figure(figsize=(10,6))
    sns.barplot(x="Month", y="AverageTemperature", data=monthly, palette="coolwarm")
    plt.title("Average Temperature by Month")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "categorical_bar.png"))
    plt.close()

    # -----> Pie chart - Uncertainty levels
    if "AverageTemperatureUncertainty" in df.columns:
        bins = [0, 0.5, 1, 2, 5]
        labels = ["Very Low", "Low", "Medium", "High"]
        df["UncertaintyLevel"] = pd.cut(df["AverageTemperatureUncertainty"], bins=bins, labels=labels)
        counts = df["UncertaintyLevel"].value_counts()
        plt.figure(figsize=(6,6))
        plt.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
        plt.title("Temperature Uncertainty Levels")
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, "categorical_pie.png"))
        plt.close()
    print("Saved categorical plots (hist/bar/pie).")

def plot_statistical(df):
    """Correlation heatmap, boxplot, violin plot, and pairplot"""
    num_df = df.select_dtypes(include=[np.number]).drop(columns=["Year","Month","Decade"], errors="ignore")

    # -----> Heatmap
    plt.figure(figsize=(6,4))
    sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "stat_heatmap.png"))
    plt.close()

    # -----> Boxplot
    plt.figure(figsize=(8,5))
    sns.boxplot(y="AverageTemperature", data=df, color="skyblue")
    plt.title("Boxplot of Average Temperature")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "stat_boxplot.png"))
    plt.close()

    # -----> Violin plot
    plt.figure(figsize=(8,5))
    sns.violinplot(y="AverageTemperature", data=df, color="lightgreen")
    plt.title("Violin Plot of Average Temperature")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "stat_violin.png"))
    plt.close()

    # -----> Pairplot
    if "AverageTemperatureUncertainty" in df.columns:
        sns.pairplot(df[["AverageTemperature", "AverageTemperatureUncertainty"]].dropna())
        plt.suptitle("Pair Plot of Temperature & Uncertainty", y=1.02)
        plt.savefig(os.path.join(PLOTS_DIR, "stat_pairplot.png"))
        plt.close()
    print("Saved statistical plots (heatmap/box/violin/pair).")

# ===================================================
# MAIN FLOW
# ===================================================
def main():
    df = read_data(DATA_FILE)
    df_clean = basic_preprocess(df)

    # -----> Compute statistical moments
    moments_df = compute_moments_for_numeric(df_clean)
    print("Summary statistics:\n", moments_df)

    # -----> Generate all plots
    plot_relational(df_clean)
    plot_categorical(df_clean)
    plot_statistical(df_clean)

    # -----> Generate a short textual report
    with open(os.path.join(OUTPUT_DIR, "short_report.txt"), "w", encoding="utf-8") as f:
        f.write("Climate Data Analysis Report\n")
        f.write("="*40 + "\n")
        f.write(f"Rows after cleaning: {len(df_clean)}\n")
        f.write(f"Numeric columns analyzed: {', '.join(moments_df['variable'])}\n\n")
        f.write("Statistical moments:\n")
        f.write(moments_df.to_string(index=False))
    print("Report generated successfully.")

if __name__ == "__main__":
    main()
