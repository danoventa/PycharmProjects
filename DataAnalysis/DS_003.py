__author__ = 'Executor'

import numpy as np
from matplotlib import pyplot as plt


''' array processing '''

print(np.__version__)

points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)
print(dx)
print(dy)
z = (np.sin(dx) + np.sin(dy))



plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x)+sin(y)')

A = np.array(([1, 2, 3, 4]))
B = np.array([100, 200, 300, 400])

condition = np.array([True, True, False, False])

answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A, B, condition)]
print(answer)

answer2 = np.where(condition, A, B)
print(answer2)

from numpy.random import randn

arr = randn(5, 5)
print(arr)
ans3 = np.where(arr<0, 0, arr)
print(ans3 )

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

print(arr2.sum())

print(arr2.mean())
print(arr2.std())
print(arr.var())

barr = np.array([True, False, True])
print(barr.any())
print(barr.all())
barr.sort()
print(barr)

countries = np.array(['France', 'Germany', 'USA'])
print(np.unique(countries))

print(np.in1d(['France', 'USA', 'Sweeded'], countries))

arrk = np.arange(10)
np.save('ark', arrk)
arrk = np.arange(5)
print(arrk)
print(np.load('ark.npy'))
arrk2 = arrk
arrk = np.load('ark.npy')
print(arrk)
print(arrk2)
np.savez('ziparr.npz', x=arrk, y=arrk2)
arcarr = np.load('ziparr.npz')
print(arcarr)
print(arcarr['x'])
print(arcarr['y'])

art = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('mytext.txt', art, delimiter=',')
arp = np.loadtxt('mytext.txt', delimiter=',')
print(art)
print(arp)

plt.show()
