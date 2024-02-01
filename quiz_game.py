print('Welcome to my random joke quiz!')

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Awesome! Let's play!")
score = 0

# 1
answer = input("What do you call an intelligent bottle of water? ")
if answer.lower() == "smart water":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 2
answer = input("What do you call an alligator in a vest? ")
if answer.lower() == "investigator":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 3
answer = input("What do you call cheese that isn't yours? ")
if answer.lower() == "nacho cheese":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 4
answer = input("What's a ghost's favorite fruit? ")
if answer.lower() == "booberries":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 4) * 100) + "%.")
