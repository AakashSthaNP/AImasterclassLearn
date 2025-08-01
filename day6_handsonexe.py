import matplotlib.pyplot as plt

# Line
years = [2020, 2021, 2022, 2023, 2024, 2025]
sales = [1000, 2000, 3000, 4500, 10800, 32001]
plt.plot(years, sales, label="Sales Trend", color="red", marker="x")
plt.title("Sales Trend Over Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()

#Scatter plot

hour_std = [1,2,3,4,5,6]
score_exm = [90,88,80,70,76,99]
plt.scatter(hour_std, score_exm, color="red")
plt.title("Study hours vs score")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.show()