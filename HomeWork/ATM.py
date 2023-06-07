print("Welcome to Positive ATM")
re=int(100000)
de=0
a=True
while a : 
    print(" 1. Cash Withdraw  2. Deposit  3.Bank Balance  4.Exit")
    opt=input("Please Select an option:")
    if (opt=="Cash Withdraw"):
        amnt=int(input("Enter the amount"))
        re=re-amnt
        print("THANK YOU")
    elif (opt=="Deposit"):
        de=int(input("Enter amount to be deposited"))
        print("THAN YOU")
     elif (opt=="Bank Balance"):
         bal=re+de
        print(bal)
     elif  (opt=="Exit"):
        print("THANK YOU")
        break
 
        
        
        
    
