# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Loading dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
del df['species']
## Claculating Corelation matrix
correlation_matrix = df.corr()
# Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correleation Heatmap")
plt.show()