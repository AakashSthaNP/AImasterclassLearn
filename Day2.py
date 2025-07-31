# Advance NumPy operations

import numpy as np

# arr = np.array([[1,2,3],[4,5,6]])
# print("Sum: ", np.sum(arr))
# print("Mean: ", np.mean(arr))
# print("Max: ", np.max(arr))
# print("Min: ", np.min(arr))
# print("Standard Deviation: ", np.std(arr))
# print("Sum along rows: ", np.sum(arr, axis=1))
# print("Sum along column: ", np.sum(arr, axis=0))

# print("Matrix: ", arr)

### Boolean Indexing and filtering

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# evens = arr[arr % 2 == 0]
# print("Evens: \n", evens)
# arr[arr > 3] = 0
# print("Modification Array: ", arr)

### Random number generation and setting seeds

## Seed
np.random.seed(42) #.... IS the seed that makes random generation same till seed There can be 1.....42...100... any in seed


random_array = np.random.rand(3,3)
print("Rnadom Array: \n", random_array)

random_integers = np.random.randint(0,10, size=(2,3))
print("Rnadom Integers: \n", random_integers)