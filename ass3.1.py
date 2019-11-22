
a = int(input("Enter 1st number = "))
c = input("Enter an operator = ")
b = int(input("Enter 2nd number = " ))
if c == "+" :
    print(a + b)

elif c == "-" :
    print(a - b)

elif c == "*" :
    print(a * b)

elif c == "/" :
    print(a // b)

elif c == "^" :
    print(a ** b)

else:
    print("invalid operator !")

