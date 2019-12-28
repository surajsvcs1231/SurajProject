def maindev(a,b):
    print(a/b)

def decorator_func(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

dev1=decorator_func(maindev)

#dev1(2,4)
if __name__=="__main__":
    dev1(2,4)