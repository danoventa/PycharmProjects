__author__ = 'Noventa'

import numpy as np
import pandas as pd
from numpy.random import randn

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dataset = randn(25)
sns.rugplot(dataset)
plt.ylim(0, 1)
#plt.show()
plt.hist(dataset, alpha=0.3)
sns.rugplot(dataset)
#plt.show()
sns.rugplot(dataset)

x_min = dataset.min() - 2
x_max = dataset.max() + 2

x_axis = np.linspace(x_min, x_max, 100)

bandwidth = ((4*dataset.std()**5)/(3*len(dataset))) ** 0.2

kernel_list = []
for data_pt in dataset:
    kernel = stats.norm(data_pt, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    kernel = kernel / kernel.max()
    kernel = kernel * 0.4
    plt.plot(x_axis, kernel, color='grey', alpha=0.5)

plt.ylim(0, 1)
#plt.show()

sum_of_kde = np.sum(kernel_list, axis=0)
fig = plt.plot(x_axis, sum_of_kde, color='indianred')
sns.rugplot(dataset)
plt.yticks([])
plt.suptitle("Sum of the basis functions")
plt.show()

sns.kdeplot(dataset)
#plt.show()
sns.rugplot(dataset, color='black')

for bw in np.arange(0.5, 2, 0.25):
    sns.kdeplot(dataset, bw=bw, lw=1.8, label=bw)

#plt.show()
kernel_options = ['biw', 'cos', 'epa', 'gau', 'tri', 'triw']

for kern in kernel_options:
    sns.kdeplot(dataset, kernel=kern, label=kern)

plt.show()

dataset = randn(100)
sns.distplot(dataset, bins=25)
plt.show()

sns.distplot(dataset, bins=25,
             kde_kws={'color' : 'indianred', 'label' : 'KDE PLOT'},
             hist_kws={'color' : 'blue', 'label' : 'HIST'})
plt.show()

