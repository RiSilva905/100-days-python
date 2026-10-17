# Day 4 of 100
# Rock, paper, scissors game
import random

player = input("What do you choose? \n1.- rock \n2.- paper \n3.- scissors? ")
computer = random.randint(1,3)
print("Computer choose " + str(computer))

if int(player) == computer:
    print("It's a tie!")
elif int(player) == 1 and computer == 2:
    print("You loose")
elif int(player) == 1 and computer == 3:
    print("You win!")
elif int(player) == 2 and computer == 1:
    print("You win!")
elif int(player) == 2 and computer == 3:
    print("You loose")
elif int(player) == 3 and computer == 1:
    print("You loose")
elif int(player) == 3 and computer == 2:
    print("You Win!")