def changeToCap(x):
    return x.lower().capitalize()
list1=['toma','lISa','tOm','thoMaS']
print(list(map(changeToCap,list1)))