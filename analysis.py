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

# Describe method from Pandas will summarize numerical column and store in var summary (count,mean,std,max and min)
# (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
summary = iris.describe()

# code line will save summary to a tab separated txt file
# (https://www.w3resource.com/python-exercises/pandas/python-pandas-data-frame-exercise-27.php)
summary.to_csv('variable_summary.txt', sep='\t')

# Plotting histograms
# For loop will iterate over all columns except last one which is species
# (https://www.w3schools.com/python/python_for_loops.asp)
for column in iris.columns[:-1]:
# initialise a new figure (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
    plt.figure()
# plots histogram using seaborn (https://seaborn.pydata.org/generated/seaborn.histplot.html)
    sns.histplot(iris[column], kde=True, bins=20)
# plot title for the plot (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)
    plt.title(f'Histogram of {column}')
# save fig as png file (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
    plt.savefig(f'plots/histogram_{column}.png')
# close figure to preven memory issues in loop (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html)
    plt.close()

# This codeline will plot scatter plot for paired features visualisation
# for loop is run to generate possible pair of the features on the dataset
# (https://docs.python.org/3/library/itertools.html)
for x, y in itertools.combinations(iris.columns[:-1], 2):
    plt.figure()
# this line will create scatter plot with color added to the species (https://seaborn.pydata.org/generated/seaborn.scatterplot.html)
    sns.scatterplot(data=iris, x=x, y=y, hue='species')
    plt.title(f'Scatter Plot: {x} vs {y}')
    plt.savefig(f'plots/scatter_{x}_vs_{y}.png')
    plt.close()

print("Analysis complete. Outputs saved.")