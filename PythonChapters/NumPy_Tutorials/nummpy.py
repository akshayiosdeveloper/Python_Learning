import numpy as np
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

# 0-D Arrays
arr = np.array(42)
print(arr)
#1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# Check Number of Dimensions?

a1 = np.array(42)
b1 = np.array([1, 2, 3, 4, 5])
c1 = np.array([[1, 2, 3], [4, 5, 6]])
d1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a1.ndim)
print(b1.ndim)
print(c1.ndim)
print(d1.ndim)

# Higher Dimensional Arrays
# When the array is created, you can define the number of dimensions by using the ndmin argument.
# Create an array with 5 dimensions and verify that it has 5 dimensions:


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)