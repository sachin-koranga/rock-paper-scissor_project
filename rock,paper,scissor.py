import random 

choices = ["rock","paper","scissor"]

#for generating comp choice
def comp_choice():
    choice = random.choice(choices)
    return choice

#draw function
def draw():
    print("draw")

userscore = 0
compscore = 0
totaldraw = 0
while True:
    userchoice = input("enter your choice or Q for quit ")
    compchoice = comp_choice()

#For exiting the ganee
    if(userchoice == "Q"):
        print("quit")
        print(f"userscore :{userscore}")
        print(f"compscore : {compscore}")
        print(f"totaldraw {totaldraw}")
        break

#check for draw
    elif(userchoice in choices):
        if(userchoice == compchoice):
            totaldraw += 1
            draw()

#check for winner
        else:
            if(userchoice == "paper" and compchoice == "rock") or (userchoice == "rock" and compchoice == "scissor") or (userchoice == "scissor" and compchoice == "paper"):
                print("user win")
                userscore += 1
            else:
                print("computer win")
                compscore += 1

#handle error
    else:
        print(f"invlid characters {userchoice}")

