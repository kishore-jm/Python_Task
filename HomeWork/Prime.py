x=int(input("Enter your number:"))
count=0
for i in range(1,x):
    if (i%2==0):
        count=count+1
        if (i%3==0):
            count=count+1
            if (i%4==0):
                count=count+1
                if (i%5==0):
                     count=count+1
                     if (i%6==0):
                         count=count+1
                         if (i%7==0):
                              count=count+1
                              if (i%8==0):
                                  count=count+1
                                  if (i%9==0):
                                       count=count+1
if(count==1):
        print("It is a Prime Number")
else:
        print("It is not a Prime Number")
            
                                    
        
        




