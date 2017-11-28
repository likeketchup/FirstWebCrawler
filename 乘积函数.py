from functools import reduce
def x(a,b):
    return a*b
l=[2, 4, 5, 7, 12]
print(reduce(x,l))