def add(a,*b):
    c=a
    for i in b:
        #c=c+i
        print(i)
    return c

result=add(5,6,7,9,11,'b')
print(result)
#############Keyword variable length argument############
def person(name,**data):
    print("name",name)
    print("data",data)

person('suraj',age=25,city='BLR',mob=9808620307)
