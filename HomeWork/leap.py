yr=int(input("Enter the year:"))
if (yr%4==0 and yr%100!=0):
    print("It is a Leap year")
elif (yr%400==0):
    print("It is a Leap year")
else:
    print("It is not a Leap year")
    
