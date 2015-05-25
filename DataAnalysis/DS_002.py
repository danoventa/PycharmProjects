__author__ = 'Executor'

import numpy as np


print(5/2)

arr1 = np.array([[1, 2, 3, 4], [8, 9, 10, 11]])
print(arr1)
print(arr1*arr1)
print(arr1-arr1)
print(1/arr1)
print(arr1**3)

arr = np.arange(0, 11)
print(arr)

print(arr[8])
print(arr[1:5])
print(arr[0:5])
arr[0:5] = 100
print(arr)
arr = np.arange(0, 11)
slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:] = 99
print(slice_of_arr)

print(arr)

arr_copy = arr.copy()
print(arr_copy)

arr_2d = np.array(([5, 10, 5], [20, 24, 54], [45, 23, 532]))
print(arr_2d)
print(arr_2d[2][0])

print(arr_2d[:2, 1:])
print(arr_2d[2])

arr2d = np.zeros((10, 10))
print(arr2d)

<<<<<<< HEAD
theNew = np.array(([1, 2, 3], [2, 3, 4]))
print(theNew)
=======
print()
arr = np.arange(50).reshape((10, 5))
print(arr)
print(arr.T)

print(np.dot(arr.T, arr))
arr3d = np.arange(50).reshape((5, 5, 2))
print(arr3d)

print(arr3d.transpose(1, 0, 2))

arrx = np.array([[1, 2, 3]])
print(arrx.swapaxes(1, 0))

print(np.sqrt(arr))

print(np.exp(arr))

A = np.random.randn(10)
print(A)
B = np.random.randn(10)
print(B)
print(np.add(A, B))
print(np.maximum(A, B))

'''
import webbrowser as wb
website = 'http://docs.scipy.org/numpy/reference/ufuncs.html#available-ufuncs'
wb.open(website)
'''

>>>>>>> 87d797bbc4a0c2ffafdfe5aa37d3f251bd297257
