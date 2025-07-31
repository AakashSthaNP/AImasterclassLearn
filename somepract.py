import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1,2,3,4,5,6,7],
    "Name": ["Aakash","Oshan","Pasang","Lhakpa","Wang","Nurbu","Prem"],
    "Age": [17,16,16,18,17,18,17],
    
})

df2 = pd.DataFrame({
    "ID": [1,2,3,4,5,6,7],
    "Score": [100,91,90,88,95,90,89],
})

print("Dataset 1: \n", df1)
print("Dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

merged["Scored_percentage"] = (merged["Score"] / 100) * 100
# merged["Scored_Grade"] = (merged["Score"] > 90 ) == "A+" & (merged["Score"] < 90) == "A"
print("Merged Dataset: \n", merged)
