import pandas as pd

s = pd.Series([10,20,30], index=["a", "b", "c"])
# print(s)

data = {"Name": ["Aakash", "Magnus"], "Age": [17, 32]}
df = pd.DataFrame(data)
print(df)

"""
df = pd.read_csv("Data.csv")
df = pd.read_excel("Data.xlsx")
for exporting, to save
   df.to_csv("Data.csv")
   df.to_excel("Data.xlsx")
"""

print(df[df["Age"] > 25])
