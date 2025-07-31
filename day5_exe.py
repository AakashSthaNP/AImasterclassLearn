import pandas as pd

data = {
    "Class": ["A", "B", "C", "B", "A", "c"],
    "Score": [90,85,95,88,94,85],
    "Age": [15,16,17,14,16,17]
    }

df = pd.DataFrame(data)
print("Original DataSet: \n", df)

grouped = df.groupby("Class").mean()
print(grouped)

by_stat = df.groupby("Class").agg(
    {"Score": ["mean", "max", "min"], "Age": ["mean", "max", "min"],}
)

print("The Groupby Stat.: \n", by_stat)