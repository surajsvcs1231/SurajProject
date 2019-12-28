class A:
    def feature1(self):
        print('Feature1')
    def feature2(self):
        print("Feature2")

class B(A):
    def feature3(self):
        print("Feature3")
    def feature4(self):
        print("Feature4")

b1=B()
b1.feature4()
class C(B):  #Multilevel Inheritance
    print("Class c")
    def feature5(self):
        print("Feature5")

class D:
    def __init__(self):
        print("Init method")
    def feature6(self):
        print("Feature6")

class E(A,D):
    def __init__(self):
        print("in E init")
    pass

e1=E()
e1.feature1()

c1=C()
c1.feature5()

#d1=D()
