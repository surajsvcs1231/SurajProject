
'''def acceptlist(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[9,6,1,7,3,4,5,8,10,13]
for i in lst:
    even,odd\
        =acceptlist(lst)
print("Even={} and Odd={}".format(even,odd))'''

size=int(input("Enter the size of the list"))
lst=[]
for i in range(size):
    lst.append(int(input("Enter the {} elemnt".format(i))))
print(lst)