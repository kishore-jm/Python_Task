print("Lets see your Type")
score=0
one=input("What do you prefer Movies or Web Series ? :")
if (one=="Movies"):
    score+=1
elif(one=="Web Series"):
    score+=1
else:
    score+=2
two=input("What do you prefer Mountain or Beaches ? :")
if (two=="Mountain"):
    score+=2
else:
    score+=1
three=input("What do you prefer Music or Dance ? :")
if (three=="Music"):
    score+=2
else:
    score+=1
four=input("What do you prefer Alone or Party ? :")
if (four=="Alone"):
    score+=2
else:
    score+=1
five=input("What do you prefer Hot drinks or Cold drinks ? :")
if (five=="Hot drinks"):
    score+=1
else:
    score+=2
if (score==10):
    print("You are Introvert(MY TYPE)")
else:
    print("You are Extrovert")

