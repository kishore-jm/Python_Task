height=int(input("Enter your height:"))
weight=int(input("Enter your weight:"))
ht=height/100
bmi=weight/ht**2
if (bmi<18.5):
    print("You are Underweight")
elif (bmi>18.5 and bmi<24.9):
    print("You are Normal")
else:
    print("You are Pre-Obesity")
    
 
