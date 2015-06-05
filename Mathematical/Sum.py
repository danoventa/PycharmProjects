__author__ = 'Noventa'

def t_recursive_sum (x, sum):
    if x == 0:
        return sum
    else:
        return t_recursive_sum(x-1, x+sum)

print(t_recursive_sum(997, 0))

def recursive_sum(x):
    if x == 1:
        return x
    else:
        return x + recursive_sum(x - 1)

print(recursive_sum(997))