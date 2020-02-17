import random
r=random.randint(1,20)
b=1
m=0
while(b<=5):
    y=int(input("Guess the Number:"))
    if(y==r):
        print("You have guessed it Right ")
        m=m+1
        break
    elif(y>r):
        print("The Actual Number is Smaller")
        b=b+1
    elif(y<r):
        print("The Actual Number is Big")
        b=b+1
if(m==0):
    print("Your Chance Got Over")
    print("You Failed")
if(m==1):
    print("Congrats")
    
