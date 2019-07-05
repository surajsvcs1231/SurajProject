#Take array size and array input from user and add those element and print the result
import os
import sys
def simpleArraySum(ar):
    ar_list = []
    sum1=0
    for i in range(0,ar):
        #ar_list.insert(i,int(input("Enter Array Limit")))
        ar_list.append(int(input("Enter Array Limit")))
        sum1=sum1+ar_list[i]
    return sum1


if __name__ == '__main__':
    ar_count = int(input("Enter input"))
    ar_sum=simpleArraySum(ar_count)
    print("Array Sum",ar_sum)

    #fptr.write(str(result) + '\n')

    #fptr.close()