print("Welcome to Positive ATM")
re=int(100000)
a=True
while a :
    print(" 1. Cash Withdraw  2. Deposit  3.Bank Balance  4.Exit")
    opt=input("Please Select an option:")
    if (opt=="Cash Withdraw"):
        amnt=int(input("Enter the amount"))
        re=re-amnt
        if (amnt<re):
             print("Thank You")
        else:
            print("insuffient balance ")
            
         
        
    elif (opt=="Deposit"):
         dep=int(input("Enter amount to be deposited"))
         re = re+dep
         
         print("THAN YOU")
    elif (opt=="Bank Balance"):
        print(re)
    elif  (opt=="Exit"):
        print("THANK YOU")
        break
