__author__ = 'Noventa'
import math

def fib(n):
    return (1/(5**.5))*(((1+(5**.5))/2)**n - ((1-(5**.5))/2)**n)

print(round(fib(15)))