import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading datasets
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

## Inspecting data
print(df.info())
print(df.describe())

## Handling with missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Removing Duplicates
df = df.drop_duplicates()

## Filtering data for First class passenger
first_class = df[df["Pclass"] == 1]
print("First class passenger: \n", first_class.head())

# Bar chart for survived by class
Survived_by_class = df.groupby("Pclass")["Survived"].mean()
Survived_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival by class")
plt.ylabel("Survival rate")
plt.show()