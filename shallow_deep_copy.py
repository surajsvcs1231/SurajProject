from numpy import *
arr1=array([3,8,1,4])
arr2=arr1.view()  #shallow copy
arr1[2]=5
print(arr1)
print(arr2)
print(id(arr2))
print(id(arr1))

arr3=array([7,1,2,9,3,8,11])
arr4=arr3.copy()
arr3[4]=17
print(arr3)
print(arr4)