tam=int(input("Enter your Tamil Mark:"))
eng=int(input("Enter your English Mark:"))
mat=int(input("Enter your Maths Mark:"))
sci=int(input("Enter your Science Mark:"))
soc=int(input("Enter your Social Mark:"))
tot=tam+eng+mat+sci+soc
avg=int(tot/5)
if (avg>90):
    print("You got Distinction")
elif (avg>80 and avg<90):
    print("You got First class")
elif (avg>65 and avg<80):
    print("You got Second class")
elif (avg>35 and avg<65):
    print("You got Third class")
else:
    print("You got Fail")

          
