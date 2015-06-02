__author__ = 'Noventa'

import IPython
import timeit
from BenchmarkingProfiling import benchmark

result = timeit.timeit('benchmark()', setup='from __main__ import benchmark', number=10)
print(result)

result = timeit.repeat('benchmark()', setup='from __main__ import benchmark', number=10)
print(result)

