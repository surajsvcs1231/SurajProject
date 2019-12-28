'''n="YOUTUBE"
#print(n[1:5:2])
#print(n[-2:-7:-2])
l1=[2,3,4,5,6]
l1.insert(2,9)
print(l1)
l1.pop()
print(l1)
from random import choice
print(choice(l1))
t1=tuple(l1)
print(t1)
print(type(t1))
l2=['hello','world','bye',3,1,2]
print(list(zip(l2)))
print(l2)
d1=dict(zip(l2[0::2],l2[1::2]))
print(d1)
print(l1.__iter__())'''

l1=[x**2 for x in range(0,10)]
print(l1)



