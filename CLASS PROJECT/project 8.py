a=int(input("Enter the number"))
sum=0
for i in range(a):
    x=a%10
    sum=sum+x
    a=a//10
print(sum)

