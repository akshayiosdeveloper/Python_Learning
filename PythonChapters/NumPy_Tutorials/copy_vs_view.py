import numpy as np
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view
arr = np.array([1, 2, 3, 4, 5])
copy1 = arr.copy()
arr[0] = 666
print(arr)
print("===copy example===")
print(copy1)
# The copy SHOULD NOT be affected by the changes made to the original array.

print("===view  example===")
# The view SHOULD be affected by the changes made to the original array.


originalArray = np.array([1, 2, 3, 4, 5])
view = originalArray.view()
originalArray[0] = 42

print(originalArray)
print(view)
print("=== make changes in view ===")
# The original array SHOULD be affected by the changes made to the view.


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute base that returns None if the array owns the data.

# Otherwise, the base  attribute refers to the original object.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
print("Check if Array Owns its Data")
print(x.base)
print(y.base)