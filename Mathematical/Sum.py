__author__ = 'Noventa'

def t_recursive_sum (x, sum):
    if x == 0:
        return sum
    else:
        return t_recursive_sum(x-1, x+sum)

print(t_recursive_sum(25, 0))