n=int(input("Enter the Number:"))
for i in range(n):
    for j in range(n):
        if (j==0)or i+j==3  or i-j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    
