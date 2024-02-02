name = input("Type your name: ")
print(f"Welcome {name} to choosing your own adventure.")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a dense forest. Do you want to venture through it or go back? Type venture to go through and back to return: ")
    if answer == "venture":
        print("You ventured through the forest and found a hidden dragon lair.")
        answer = input("Do you want to sneak in (sneak) or challenge the dragon openly (challenge)? ")
        if answer == "sneak":
            print("You sneakily entered the lair, but the dragon caught you and you lose.")
        elif answer == "challenge":
            print("You challenged the dragon and, after a fierce battle, you defeated it. You WIN!")
        else:
            print('Not a valid option. You lose.')
    elif answer == "back":
        print("You went back and lost the chance for a great adventure. You lose.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a mountain with a cave. Do you want to explore the cave or continue walking (explore/continue)? ")
    
    if answer == "continue":
        print("You continued walking and missed out on an epic adventure. You lose.")
    elif answer == "explore":
        print("You explored the cave and found a sleeping dragon.")
        answer = input("Do you want to try to steal the dragon's treasure (steal) or leave quietly (leave)? ")
        if answer == "steal":
            print("You tried to steal the treasure, but the dragon woke up and you lose.")
        elif answer == "leave":
            print("You left quietly and avoided a dangerous confrontation. However, you also missed out on the treasure. You lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
