a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if (a>b):
    if (a>c):
        print("a is greater than others")
    else:
        print("c is greatere")
else:
    if (b>c):
        print("b is greater than others")
    else:
        print("c is greater than others")

if (a>b and a>c):
    print("a is greater than others")
elif (b>c):
    print("b is greater than others")
else:
    print("c is greater than others")

