# analysis.py
# Author Deepika Gusain

# Import pandas library, which is used for data manipulation (https://pandas.pydata.org/)
import pandas as pd
# import seadborn which is used for statistical visualisation and based on matplotlib
# (https://seaborn.pydata.org/)

import seaborn as sns
# Import Matplotlib for plotting, saving plots (https://matplotlib.org/)
import matplotlib.pyplot as plt

# Import Itertools used for effecient looping (https://docs.python.org/3/library/itertools.html)
import itertools

# Import python library os to interact with operating system. To create directories to save output file
# (https://docs.python.org/3/library/os.html)
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