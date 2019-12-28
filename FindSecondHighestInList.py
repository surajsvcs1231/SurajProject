#Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given scores.
# Store them in a list and find the score of the runner-up.


def calulatesecondhighest(ar_size):
    ar_list=[]
    for i in range(0,ar_size):
        ar_list.append(int(input("Enter the List Element")))
    ar_list.sort()
    print(ar_list)
    return ar_list[-2]

ar_size=int(input("Enter the size of the array"))
sec_high=calulatesecondhighest(ar_size)
print(sec_high)