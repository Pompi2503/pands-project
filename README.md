# Programming and Scripting Project

<br>

# Project Title
Exploring the Iris flower Dataset using Python - Project For Programming and Scripting (2025)

# Project Overview
This project focusses on examinin the well-known Iris flowere dataset by utilizing Python.
It demonstrates how scripting toolds can be applied to carry out souring, pre-processing and visuation of the data which are integral part of the data analysis. The work on the project involves gathering insight from the existing Iris dataaset, generating visual, and explainaing finding through structured programming and clear documentation.


# Dataset Background
The Iris dataset, introduced by statistician Ronald Fisher, includes 150 flower samples spanning three species: Setosa, Versicolor, and Virginica. Each sample holds four numerical measurements — petal length and width, along with sepal length and width. This dataset serves as a valuable resource for practicing classification and pattern recognition.


 # Objectives
- To understand and explain the Iris dataset.
- To write Python code that processes and analyzes the data.
- To generate statistical summaries and visual representations.
- To keep the project well-organized and thoroughly documented.
- To use GitHub effectively for version control and submission.
- To develop meaningful conclusions based on analysis.


 # Technology Used
The project uses several popular Python tools:
- Pandas for data manipulation
- Seaborn for statistical graphics
- Matplotlib for custom plotting
- Jupyter Notebook (for documenting steps interactively and running code interactively)
- GitHub for tracking changes and storing the code


# Repository Structure
```
pands-project/
├── analysis.py              # Script to perform analysis
├── iris.csv                 # The dataset file
├── variable_summary.txt     # Summary of statistics
├── plots/                   # Contains graphs and plots
│   ├── histogram_*.png
│   └── scatter_*_vs_*.png
├── README.md                # Project overview
├── requirements.txt         # Dependencies
```

# How to Run the project
1. Download the project from GitHub:
```bash
git clone 
cd pands-project
```
2. Install the necessary libraries:
```bash
pip install -r requirements.txt
```
3. Run the main script:
```bash
python analysis.py
```

# Output Summary
After running the script, you will get:
- A text file with basic statistics (`variable_summary.txt`)
- Histograms showing the distribution of each measurement
- Scatter plots comparing every pair of features

# Analysis Insights
The analysis showed that the petal dimensions are the most helpful in telling the species apart. For instance, Iris Setosa can be clearly identified based on petal size. The scatter plots helped uncover feature correlations and confirmed that some species overlap slightly in certain measurements.

# References
- Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems.
- https://archive.ics.uci.edu/ml/datasets/iris
- https://www.python.org/
- https://pandas.pydata.org/
- https://seaborn.pydata.org/
- https://matplotlib.org/