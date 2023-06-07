n=int(input("Enter the Number:"))
for i in range(n):
    for j in range(n):
        if (j==N3  or i==0 or i==4):
            print("*",end="")
        else:
             print(" ",end="")
    print()
