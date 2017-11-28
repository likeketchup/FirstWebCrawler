def rootCheck(a):
    a=a**0.5
    b=int(a)
    return a==b
l=range(100)
print(list(filter(rootCheck,l)))