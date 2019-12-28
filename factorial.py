'''def fact(num):
    prod=1
    for i in range(1,num+1):
        prod=prod*i
    return prod


num=int(input("Enter number"))
result=fact(num)
print(result)'''
#############Recursion#############
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
result=fact(3)
print(result)