num=[9 ,3 , 6 ,1 ,10 ,17 ,24]
num.append(45)
print(num)   #[9, 3, 6, 1, 10, 17, 24, 45]
num.insert(3,97)
print(num)   #[9, 3, 6, 97, 1, 10, 17, 24, 45]
num.remove(24)
print(num) #[9, 3, 6, 97, 1, 10, 17, 45]
num.pop(1)
print(num)
num.pop()
print(num)
#del num[4:]
#print(num)
print('max',max(num))
print('min',min(num))
print('sum',sum(num))
print('length',len(num))
num.sort()
print(num)
