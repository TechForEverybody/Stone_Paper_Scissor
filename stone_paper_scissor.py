print("*"*5," stone paper scissor ","*"*5)

import random
def game(a,b):
    if a==b:
        print("tie")
    elif a==1:
        if b==2:
            print("Tie")
        else:
            print("You lose")
    elif a==2:
        if b==1:
            print("Tie")
        else:
            print("You Loose")
    elif a==3:
        if b==1:
            print("You Loose")
        else:
            print("You Win")
    
def input_validater(a):
    if a==1:
        return "stone"
    elif a==2:
        return "paper"
    elif a==3:
        return "scissor"
def input_string_validater(a):
    a=a.lower()
    if a=="stone":
        return 1
    elif a=="paper":
        return 2
    elif a=="scissor":
        return 3
    else:
        return 0
while True:
    print("\nfor exit enter exit\n")
    print("Enter from The Below \n1.stone\n2.paper\n3.scissor")
    a=random.randint(1,3)
    b=input("enter your choice : ")
    if b=="exit":
        exit()
    print("computer choose : ",input_validater(a))
    if(input_string_validater(b)==0):
        print("\nPlease Enter valid choice")
    else:
        game(a,input_string_validater(b))


# print("\n\n\n","*"*5," stone paper scissor ","*"*5)