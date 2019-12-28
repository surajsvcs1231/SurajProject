#simple vending machine where there is a limited stock of candies

av_can=5
x=int(input("How many candies you need?:"))
for i in range(1,x+1):
    if i>av_can:
        print("Sorry we have ",av_can," Candies Only")
        break
    print("Candies:",i)
print("Thanks!!!!")