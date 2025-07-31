### https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

## Loading Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

### Exploring structure

# print("First 5 rows: ", df.head())
# print("Last 5 rows: ", df.tail())
#print(df.info())
# print(df.describe())

selected_column = df[["species", "sepal_length"]]
# print("Selected column: ", selected_column)

filtered_row = df[(df["sepal_length"]>5.0) & (df["species"]=="setosa")]
print("Filtered Rows: \n", filtered_row)