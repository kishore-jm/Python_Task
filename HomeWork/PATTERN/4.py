n=int(input("Enter the NUmber:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==4  or (i==3 and (j>0 and j<4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
            
        
