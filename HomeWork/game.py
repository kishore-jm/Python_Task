print("Welcome to the Game")
di=input("Choose Right or Left :")
if (di=="Left"):
    le=input("Choose Wait or Swim :")
    if (le=="Swim"):
        col=input("Choose Red or Black :")
        if (col=="Red"):
            print("You won the Game")
        else:
            print("You lose the Game")
    else:
         print("You lose the Game")
else:
    print("You lose the Game")
            
        
