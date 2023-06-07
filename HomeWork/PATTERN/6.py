n=int(input("Enter the Number:"))
for i in range(n):
    for j in range(n):
        if (i==i and j==0):
            print("*",end="")
        else:
            print(" " ,end="")
            
