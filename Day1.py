import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# reshaped = arr.reshape((3,3))
# print(reshaped)

#diminstion
# arr = np.array([1,2,3])
# expanded = arr[:, np.newaxis]
# print(expanded)
   # ...............
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)
# print(a - b)
# print(a*b)


# arr = np.array([4, 16, 25])
# print(np.sqrt(arr))
# print(np.mean(arr))

### Excersise


# a = np.arange(1,6)
# b = np.arange(6,11)
# print("Add: ", a + b)
# print("Sub: ", a - b)
# print("Mult: ", a*b)
# print("Div: ", a/b)


### MAtrix

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Original matrix: \n", matrix)
transpose = matrix.T
print(f"Transpose: \n {transpose}")

another_matrix = np.array([[9,8,7], [6,5,4], [3,2,1]])
print("Addition: \n", matrix + another_matrix)
print("Mutiplication: \n", matrix * another_matrix)