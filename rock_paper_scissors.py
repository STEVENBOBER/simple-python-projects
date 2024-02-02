import random

user_wins = 0
draws = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type rock/paper/scissors or Q to quit: ').lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"The computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw")
        draws += 1

    else:
        print("you lost!")
        computer_wins += 1

print(f"You won {user_wins} time.")
print(f"The computer won {computer_wins} time.")
print(f"It was a draw {draws} time.")
print("Let's play again soon!")
