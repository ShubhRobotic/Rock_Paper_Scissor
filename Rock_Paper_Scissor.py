import random

Hand_sign = ["Rock","Paper","Scissor"]

Playerscore = 0
Computerscore = 0
print("Do you want to play Rock, Paper, Scissor?")
player = input("Type yes to start: ")
if player.lower() != "yes":
    quit()

print("""Let's get started!
Rules: Paper > Rock, Scissor > Paper, Rock > Scissor
Type 'q' to exit""")

while True:
    answer = input("Type your guess: ")
    if answer.lower() == "q":
        break
    random_number = random.randint(0,2)
    computer_pick = Hand_sign[random_number]
    print("computer_picked", computer_pick + ".")

    if answer == "Paper" and computer_pick == "Rock":
        Playerscore += 1
        print("won")
        
    elif answer == "Scissor" and computer_pick ==  "Paper":
        Playerscore += 1
        print("won")

    elif answer == "Rock" and computer_pick == "Scissor":
        Playerscore += 1
        print("won")
    
    elif computer_pick == answer:
        print("Draw")

    else:
        Computerscore +=1
        print("Loss")
    
