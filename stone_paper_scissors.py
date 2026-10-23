import random
user_action = input("choose one (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\n you chose {user_action}, and the computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"both players  selected{user_action}.oh,it's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("rock smashes scissors,which means you win!")
    else:
        print("paper covers rock,you lose hehe.")
elif user_action == "paper":
    if computer_action == "rock":
        print("paper covers rock,yee you win!")
    else:
        print("scissors cuts paper,oh no you lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("scissors cuts paper and you win for this time.")
    else:
        print("rock smashes scissors,and so you lose!")
