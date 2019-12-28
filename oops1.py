class computer:
    def __init__(self,cpu,ram):
        print("in init")
        self.cpu = cpu
        self.ram = ram
    def config(self,con,pon):
        print("config details:cpu {} and ram {}".format(con,pon))
        print("config details:cpu {} and ram {}".format(self.cpu,self.ram))

com1=computer(16,'1TB')
com1.config(20,'2TB')