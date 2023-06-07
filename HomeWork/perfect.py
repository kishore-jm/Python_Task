'''x=int(input("Enter the Number:" ))
sum=0
for i in range(1,x):
    if (x%i==0):
        sum=sum+i
if (sum==x):
    print("The number is a Perfect Number")
else:
    print("The number is not  a Perfect Number")'''

        
x=int(input("Enter the Number:" ))
sum=0
a=1
while a<x:
    
    if (x%a==0):
        sum=sum+a
    a+=1

if (sum==x):
    print("The number is a Perfect Number")
else:
    print("The number is not  a Perfect Number")


        
