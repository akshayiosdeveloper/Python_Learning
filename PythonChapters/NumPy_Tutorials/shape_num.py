import numpy as np
# The shape of an array is the number of elements in each dimension.

# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

arr = np.array([[1, 2,3],[7,0,0],[0,0,0]])

# print(arr.shape)

arr = np.array([1, 2], ndmin=3)

print(arr)
print('shape of array :', arr.shape)