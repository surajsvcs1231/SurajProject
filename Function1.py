def add(a,b):
    return a+b
sum = add(5,9)
print(sum)

#########################################################################
def update(a):
    print(a)
    a=100
    return a

x=20
print(id(x))
result=update(id(x))
print(id(result))
print(result)