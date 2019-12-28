from numpy import *
arr1=array([
            [2,3,5,9,1,13],
            [7,1,4,19,12,19]
            ])
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
arr2=arr1.flatten()
print(arr2)
arr3=arr2.reshape(2,2,3)
print(arr3)