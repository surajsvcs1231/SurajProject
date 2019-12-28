class checking:
    def __init__(self):
        self.name = "Suraj"
        self.age=31

    def update(self):
        self.age=29

    def compare(self,other):
        if c1.age>c2.age:
            print(c1.age,"is greater")
        else:
            print(c2.age,"is greater")


c1=checking()
c2=checking()
c1.update()
print(c1.compare(c2))
print(c1.age)
print(c2.name)