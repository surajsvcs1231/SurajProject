a=10
#print('global',id(a))

def variablescope():
    a=15
    print(a)
    #x=globals()['a']
    #print("local",id(x))
    #print(x)
    globals()['a']=19

variablescope()

print('a',a)
'''

a=16
def va():
    global a
    print(a)

va()
print(a)'''
class test:
    c = 0 # global variable
    def add(self):
        global c
        c = c + 2 # increment by 2
        print("Inside add():", c)

t1=test()
t1.add()
print(t1.c)

