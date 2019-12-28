a=1
for i in range(4,0,-1):
    k=a
    for j in range(i):
        print(k,end='')
        k+=1
    a+=1
    print()