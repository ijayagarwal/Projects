''' 
In this program we are going to make a Stone, Paper, Scissor game
to give you some nostalgia.


1 for Stone
-1 for Paper
0 for Scissor
'''
import random

computer= random.choice([-1,0,1])
youstr = input("enter your choice: ")
youDict={"stone":1, "paper":-1,"scissor":0}
reverseDict={1:"Stone",0:"Scissor",-1:"Paper"}
you=youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]} .") 

## we made reversedict(variable) to make code more readable.

if computer==you:
    print("It's a Draw")

else:    
    if computer==-1 and you==0:
        print("You win")
    elif computer==-1 and you==1:
        print("you Lose")    
    elif computer==1 and you==-1:
        print("you Win")

    elif computer==1 and you==0:
        print("you Lose")
    elif computer ==0 and you ==-1:
        print("You Lose!") 
    elif computer==0 and you==1:
        print("you win")
            
    else:
        print("something went wrong")