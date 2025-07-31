import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Charle","John","Vivian"],
    "Age": [20,25,30],
    "Country": ["Nepal","India","USA"],
})
df2 = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [85,90,88],
    "Grade": ["B+", "A+","A"]
})
print("Dataset 1: \n", df1)
print("Dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

merged["Score_percentage"] = (merged["Score"] / 100) * 100
print("Merged Dataset: \n", merged)