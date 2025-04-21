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

# This code will load iris dataset from seaborn which is inbuilt.
# Dataset contain three target classes with measurement of data on petel/sepal lenght/width
# (https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
iris = sns.load_dataset('iris')

# code will save Dataframe iris to csv, index=false will prevent row indices to the file
# (https://www.geeksforgeeks.org/how-to-export-pandas-dataframe-to-a-csv-file/)
iris.to_csv('iris.csv', index=False)

# mkdir from os library is used to create directory and will not throw error if it exists.
# (https://www.geeksforgeeks.org/python-os-makedirs-method/)
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