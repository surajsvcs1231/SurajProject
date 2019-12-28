from functools import reduce
square=lambda  a:a*a

result=square(5)
print(result)
###############################
num = [4,9,1,6,10,12,2,7]
result_filter=list(filter(lambda n:n%2==0,num))
print("filter",result_filter)
result_map=list(map(lambda n:n*2,result_filter))
print("map",result_map)
result_reduce=reduce((lambda a,b:a+b),result_map)
print(result_reduce)
