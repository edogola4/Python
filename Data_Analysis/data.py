# Analyzing Data with Pandas and Visualizing Results with Matplotlib

'''
Task 1: Load and Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.
Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.
Task 3: Data Visualization
Create at least four different types of visualizations:
Line chart showing trends over time (for example, a time-series of sales data).
Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
Histogram of a numerical column to understand its distribution.
Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
Customize your plots with titles, labels for axes, and legends where necessary.



Additional Instructions

Dataset Suggestions:

You can use publicly available datasets from sites like Kaggle or UCI Machine Learning Repository.
The Iris dataset (a classic dataset for classification problems) can be accessed via sklearn.datasets.load_iris(), which can be used for the analysis.

Plot Customization:

Customize the plots using the matplotlib library to add titles, axis labels, and legends.
Use seaborn for additional plotting styles, which can make your charts more visually appealing.

Error Handling:

Handle possible errors during the file reading (e.g., file not found), missing data, or incorrect data types by using exception-handling mechanisms (try, except).

Submission:

Ensure your submission is complete with all necessary code and explanations. Make sure that each plot is properly labeled and provides insights into the dataset.

'''


# Task 1: Load and Explore the Dataset
# using the Iris dataset for this assignment
# the dataset can be loaded via pandas or directly from sklearn.datasets.
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load the Iris dataset using seaborn which has it as a built-in dataset. If you have a CSV file, you can load it like this:
# For CSV dataset
# df = pd.read_csv('your_dataset.csv')

# Load Iris dataset from seaborn
from sklearn.datasets import load_iris
iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = iris_data.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the dataset
print(df.head())

# Check Data Types and Missing Values:
df.info()
df.isnull().sum()

# it shouldn't have any missing values. But if it did, we could either drop or fill the missing values:
# Drop missing values (if any)
df = df.dropna()

# Or fill missing values with the mean of the column
# df = df.fillna(df.mean())



### Task 2: Basic Data Analysis
# Compute basic statistics such as mean, median, and standard deviation for numerical columns.
df.describe()

#  Let's compute the mean of numerical columns for each species group (categorical column).
df.groupby('species').mean()

# Identify any patterns or interesting findings from your analysis.
# For example, let's compare the sepal length across species.
sns.barplot(x='species', y='sepal length (cm)', data=df)

plt.title('Comparison of Sepal Length Across Species')




### Task 3: Data Visualization
# Line Chart (Trends Over Time): If we had time-series data, we could plot trends over time. For this dataset, we can visualize how the petal length changes across species.

# Line plot showing average petal length per species
plt.figure(figsize=(10, 6))
sns.lineplot(x="species", y="petal length (cm)", data=df, marker="o")
plt.title('Petal Length Across Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()


# Bar Chart (Comparison Across Categories): We’ll show the average petal length per species.
# Bar chart to compare petal length across species
plt.figure(figsize=(10, 6))
sns.barplot(x="species", y="petal length (cm)", data=df)
plt.title('Average Petal Length Per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

#Histogram (Distribution of a Numerical Column): Let’s plot the histogram for the petal length.
# Histogram of petal length
plt.figure(figsize=(10, 6))
sns.histplot(df['petal length (cm)'], bins=15, kde=True)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()


# Scatter Plot (Relationship Between Two Numerical Columns): Now, we can create a scatter plot to visualize the relationship between sepal length and petal length.

# Scatter plot of sepal length vs petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
