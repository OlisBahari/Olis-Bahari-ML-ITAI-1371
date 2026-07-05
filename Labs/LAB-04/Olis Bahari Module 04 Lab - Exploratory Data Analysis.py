# Filemame......: Olis Bahari Module 04 Lab - Exploratory Data Analysis.py
# Language......: Python
# Class.........: ITAI 1371 Introduction to Machine
# Semster.......: Summer 2026
# Class Type....: Online
# Instructor....; Sitaram Ayyagari
# Major Part of Code Written by: Sitaram Ayyagari
# Minor Part of Code Written by: Olis Bahari
# Version......................: V1.0

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn is built on top of Matplotlib

# Load the dataset directly from a URL
df = pd.read_csv(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
)

print("--- First 5 Rows ---")
print(df.head())

print("\n--- Basic Info ---")
# Shows column names, data types, and missing values
df.info()



# Get summary statistics for numerical columns
print("--- Descriptive Statistics ---")
print(df.describe())

print("--- Key Insights from Statistics ---")
print(f"The average age of a passenger was {df['Age'].mean():.1f} years.")
print(f"The overall survival rate was {df['Survived'].mean():.1%}.")
print(f"Fares ranged from ${df['Fare'].min():.2f} to a whopping ${df['Fare'].max():.2f}.")



# Visualization 2
# Set a nice visual style
sns.set_style('whitegrid')

# Create the figure
plt.figure(figsize=(8, 6))

# Create the count plot
sns.countplot(x='Survived', data=df)

# Add title
plt.title('Survival Distribution (0 = Died, 1 = Survived)')

# Display the plot
plt.show()

print("Insight: Far more people died than survived. This is an example of an imbalanced dataset, which can sometimes be a challenge for machine learning models.")



# Visualization 2
# Create the figure
plt.figure(figsize=(10, 6))

# Create the count plot
sns.countplot(x='Pclass', hue='Survived', data=df)

# Add title
plt.title('Survival by Passenger Class')

# Customize legend
plt.legend(['Died', 'Survived'])

# Show plot
plt.show()

print("Insight: This is a very strong pattern. 1st class passengers had a much higher chance of survival compared to 3rd class passengers. Money seems to have made a difference.")




# Visualization 3
# Create the figure
plt.figure(figsize=(10, 6))

# Create the count plot
sns.countplot(x='Sex', hue='Survived', data=df)

# Add title
plt.title('Survival by Gender')

# Add legend
plt.legend(['Died', 'Survived'])

# Display the plot
plt.show()

print("Insight: The pattern is undeniable. A much higher proportion of females survived compared to males. This is another very strong predictor.")



# Visualization 4
# A FacetGrid allows us to create multiple plots side-by-side
# to compare distributions.

# Create one histogram for passengers who died (0)
# and one for passengers who survived (1)
g = sns.FacetGrid(df, col='Survived', height=6)

# Plot Age distributions
g.map(plt.hist, 'Age', bins=20)

# Add axis labels
g.set_axis_labels("Age", "Count")

# Add titles
g.set_titles("Survived = {col_name}")

# Display the plots
plt.show()

print("Insight: The age distribution for those who did not survive is centered around the 20-40 age range. For those who survived, there is a noticeable spike for young children. This supports the 'children' part of the mantra.")



# Module 04 Lab Experiement 1 by Olis Bahari
plt.figure(figsize=(10, 6))

sns.countplot(x='Embarked', hue='Survived', data=df)

plt.title('Survival by Port of Embarkation')
plt.xlabel('Port of Embarkation')
plt.ylabel('Number of Passengers')

# Display the plot
plt.show()



# Module 04 Lab Experiement 2 by Olis Bahari
plt.figure(figsize=(10, 6))

sns.boxplot(x='Survived', y='Fare', data=df)

plt.title('Fare Distribution by Survival Status')
plt.xlabel('Survived (0 = Died, 1 = Survived)')
plt.ylabel('Fare')

plt.show()