a=10
b=4
try:
    print(a/b)
    c=int(input("Enter a number"))

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

except Exception as e:
    print(e)

finally:
    print("Thanks You")