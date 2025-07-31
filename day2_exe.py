import numpy as np

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# vector = np.array([1, 0, -1])

# result_add = matrix + vector
# print(f"Addition : \n {result_add}")

# result_mult = matrix * 2
# print("Multiplication: \n", result_mult)

### Exe 2

# Generating a 5x5 dataset
dataset = np.random.randint(1,51, size=(5,5))
print("Orginal Dataset: \n", dataset)

## Filtering dataset>30 replace 0 in it
dataset[dataset > 30] = 0
print("Modified daraset: \n", dataset)

## Calculation
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))