# analysis.py
# Author Deepika Gusain

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import os

# Load dataset
iris = sns.load_dataset('iris')

# Save to CSV (if needed)
iris.to_csv('iris.csv', index=False)

# Create output directories
os.makedirs('plots', exist_ok=True)

# Summary stats
summary = iris.describe()
summary.to_csv('variable_summary.txt', sep='\t')

# Histograms
for column in iris.columns[:-1]:
    plt.figure()
    sns.histplot(iris[column], kde=True, bins=20)
    plt.title(f'Histogram of {column}')
    plt.savefig(f'plots/histogram_{column}.png')
    plt.close()

# Scatter plots for all pairs
for x, y in itertools.combinations(iris.columns[:-1], 2):
    plt.figure()
    sns.scatterplot(data=iris, x=x, y=y, hue='species')
    plt.title(f'Scatter Plot: {x} vs {y}')
    plt.savefig(f'plots/scatter_{x}_vs_{y}.png')
    plt.close()

print("Analysis complete. Outputs saved.")