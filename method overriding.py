class A:
    def sum(self):
        print("i m in A")

class B(A):
    def sum(self):
        print("i m in B")

a1=B()
a1.sum()