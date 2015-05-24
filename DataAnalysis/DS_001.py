__author__ = 'Executor'

import numpy as np

my_list1 = [1, 2, 3, 4]

my_array1 = np.array(my_list1)
my_list2 = [11, 22, 33, 44]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)

print(my_array2)
print(my_array2.shape)
print(my_array2.dtype)

np.zeros(5)
my_zeros_array = np.zeros(5)
print(my_zeros_array.dtype)

print(np.ones([5, 5]))
print(np.empty(5))
print(np.eye(5))
print(np.arange(5))
print(np.arange(5, 50, 2))
