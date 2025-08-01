import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("HeatMap")
plt.show()

# Basic plot

# x = [1,2,3,4]
# y = [10,20,25,30]

# plt.plot(x,y)
# plt.show()

## Line ploting
# plt.plot([1,2,3],[10,20,30], label="Trend")
# plt.plot([1,2,3],[10,20,30], label="Trend", color="orange", linestyle="--", marker="x")
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.show()

### Bar Chart
# catagories = ["A", "B", "Z"]
# values = [10,20,14]
# plt.bar(catagories, values, color="Blue")
# plt.title("Bar Chart")
# plt.show()

#### Histogram

# data = [1,2,2,3,3,3,4,4,4,4]
# plt.hist(data, bins=4, color="green", edgecolor = "black")
# plt.title("Histogram")
# plt.show()


## Scatter Plot
# x = [1,2,3,4,5,6,7,8]
# y = [10,12,25,30,45,50,62,74]
# plt.scatter(x,y, color="red")
# plt.title("Scatter Plot")
# plt.show()