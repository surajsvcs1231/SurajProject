f=open("C:\\Users\\suraj prakash\\Desktop\\bank.txt",'r')
#print(f.read())
print(f.readline(3))
#######################################################################
f1=open("C:\\Users\\suraj prakash\\Desktop\\blr.txt",'a')
f1 .write(' Laptop')
######################################################################
im=open("C:\\Users\\suraj prakash\\Desktop\\IMG_20160722_211259.jpg",'rb')
#for i in im:
    #print(i)
im1=open("C:\\Users\\suraj prakash\\Desktop\\Chotu.jpg",'wb')
for i in im:
    im1.write(i)
