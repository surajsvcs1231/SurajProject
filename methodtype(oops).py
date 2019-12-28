class Student:
    school="DNS"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod   #class method
    def schooldet(cls):
        cls.school="Subharti"
        return cls.school

    @staticmethod
    def info():
        print("this is the static method")

s1=Student(67,89,42)
s2=Student(76,98,69)

print(s2.avg(),Student.school)
print(s1.avg(),Student.schooldet())
s1.info()

