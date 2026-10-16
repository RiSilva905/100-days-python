# Day 3 of 100
# Basic treasure game

print("Welcome to treasure island. \n Your mission is to find the treasure.")
lor = input("Do you wanna go left or right? ")
if lor == "right":
    print("Game Over")
else:
    swim = input("Do you swim or wait? ")
    if swim == "swim":
        print("Game Over")
    else:
        door = input("Which door do you choose? red, blue or yellow ")
        if door == "red":
            print("Game Over")
        elif door == "blue":
            print("Game Over")
        elif door == "yellow":
            print("You win!")