n=int(input("Enter the Number:"))
for i in range(n):
    for j in range(n):
        if j==0 or (j==4 and (i!=0 and i!=3)) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(" " ,end="")
            
