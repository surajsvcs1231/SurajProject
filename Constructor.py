class A:
    def __init__(self):
        print("Init in A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init in B")

a1=B()
