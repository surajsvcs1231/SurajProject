class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        f1=self.m1+other.m1
        f2=self.m2+other.m2
        return f1+f2
    def __gt__(self, other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        if m1>m2:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1,self.m2)






s1=student(15,97)
s2=student(87,56)
print(s1+s2)   #internally it calls like int.__add__(s1,s2)
if s1>s2:
    print("s1 is greater")
else:
    print("s2 is greater")

print(s1)   
print(s2)