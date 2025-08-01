### Exercis

import pandas as pd
import numpy as np

# Creating a sample dataset

data = {
    "Name": ["Aman", "Bobby", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}
df = pd.DataFrame(data)
print("Original Dataset: \n", df)

df["Age"] =df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

# print("Dataset: \n", df)
df = df.rename(columns={"Name":"Student_Name", "Score":"Exam_Score"})
print("Dataset: \n", df)