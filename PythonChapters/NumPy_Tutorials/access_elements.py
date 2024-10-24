import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
# Access 2-D Arrays
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
print('2nd element on 1st row: ', arr[0, 2])
print('2nd element on 1st row: ', arr[1, 3])

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0, 1, 2])