#Joining means putting contents of two or more arrays in a single array.
import numpy as np
# arr1 =np.array([1, 2, 3])

# arr2 =np.array([4, 5, 6])

# arr3 =np.array([7, 8, 9])

# arr = np.concatenate((arr1, arr2, arr3))

# arr1 = np.array([[1, 2], [3, 4]]) stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
#Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=1)

# hstack() to stack along rows.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))

arr = np.vstack((arr1, arr2)) # vstack()  to stack along columns.

arr = np.dstack((arr1, arr2)) #dstack() to stack along height, which is the same as depth.

print(arr)