a=int(input("Enter number:"))
for i in range(a):
    x=a%10
    n=x-1
    b=x*10+n
    a=a//10
    x=x//10
print(b)
