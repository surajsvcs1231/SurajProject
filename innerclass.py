class student:
    def __init__(self,name,marks,roll):
        self.name=name
        self.roll=roll
        self.marks=marks
        self.lap=self.Laptop(cpu='',ram='',brand='')

    def show(self):
        print("Name",self.name,"Com Marks",self.marks,"Roll",self.roll)

    class Laptop:
        def __init__(self,cpu,ram,brand):
            self.cpu=cpu
            self.ram=ram
            self.brand=brand

        def show(self):
            print(self.cpu,self.ram,self.brand)



s1=student("Suraj",67,12)
s2=student("Pranshu",4,18)
l1=s1.Laptop('i5',16,'dell')
l1.show()
s1.show()