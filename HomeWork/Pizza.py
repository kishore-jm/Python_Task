print("Welcome to Pizza Hub")
bill=0
size=str(input("What size pizza do you want S,M or L?:"))
if (size=="S"):
    bill=bill+10
elif (size=="M"):
     bill=bill+20
else:
    bill=bill+30
    
ex=input("Do you want Extra Toppings? :")
if (ex=="Y" and size=="S"):
    bill=bill+5
elif (ex=="Y" and size=="M"):
    bill=bill+10
elif (ex=="Y" and size=="L"):
    bill=bill+15

che=input("Do you want Extra Cheese? :")
if (che=="Y"):
    bill=bill+10
print("The Total amount of Bill is :",bill)
      
