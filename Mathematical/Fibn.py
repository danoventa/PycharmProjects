__author__ = 'Noventa'
import math

def fib(n):
    return_fib = (1/(5**.5))*(((1+(5**.5))/2)**n - ((1-(5**.5))/2)**n)
    return round(return_fib)


print(fib(8))