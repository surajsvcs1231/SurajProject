
def feb(lmt):
    if lmt>0:
        n1=0
        n2=1
        if lmt==1:
            print(n1)
        else:
            print(n1)
            print(n2)
            for i in range(2,lmt):
                n3=n1+n2
                if n3<=lmt:
                    n1=n2
                    n2=n3
                    print(n3)
    else:
        print(("invalid input"))

lmt=int(input("Enter the limit of fibonacci series"))
feb(lmt)
