print("Welocme to tips Calculator")
amnt=int(input("what was your bill amount:"))
share=int(input("How many people to split the amount"))
percentage=int(input("what was the percentage tip would you like to give 2,4 or 6"))
per=amnt*percentage/100
to=amnt+per
tips=to/share
print(int(tips))
