A = 10
'''Returns argument a is squared.'''
print(A)
#list comprehension
lst1=[i for i in range(1,10) if i%2==0]
print(lst1)

#Dictionary Comprehension
key=[1,2,3,4]
values=['suraj','aman','piyush','pranshu']
dict1={k:v for (k,v) in zip(key,values) }
dict2={x:x**2 for x in range(1,6)}
print(dict2)
print(dict1)
