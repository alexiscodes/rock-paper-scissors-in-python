import random
player_score = 0
computer_score = 0
ties = 0

#this would store the result of every round
match_history = []

#to remember player's moves
player_moves = []

#to track consecutive rounds won
player_streak  = 0
computer_streak = 0

#to track the longest winning streak
longest_player_streak = 0
longest_computer_streak = 0

while True:
    try:
        total_rounds = int(input("How many rounds do you want to play? "))

        if total_rounds > 0:
            break
            print("Please enter a number greater than zero!")
    except ValueError:
        print("Please enter a whole number!")
        

for round_number in range(1, total_rounds + 1):
    print("\nround", round_number)

    while True:
        user_action = input(
            "choose one(rock,paper,scissors):"
        ).strip().lower()

        if user_action in ["rock", "paper", "scissors"]:
            break

        print("thats invalid! please choose any of the three options!")

    possible_actions = ["rock", "paper", "scissors"]
    
    if len(player_moves) >= 2:
        move_counts = {
            move: player_moves.count(move)
            for move in possible_actions
        }
    highest_count = max(move.counts.values())

    most_common_moves = [
        move for move,count in move_counts.items()
        if count == highest_count
    ] 

most_common_move = random.choice(most_common_moves)
if most_common_move == "rock":
    computer_action = "paper"
elif most_common_move == "paper": 
    computer_action == "scissors"
else:
    computer_action = "rock"
else:
    computer_action = random.choice(possible_actions)
    player_moves.append(user_action)
     
    print(f"Round number: {round_number}")
    print(f"\n you chose {user_action}, and the computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"both players have selected{user_action}.oh,it's a tie!")
        ties += 1
        result = "tie"
        player_streak = 0
        computer_streak = 0

    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock shatters scissors,which means that you win!")
            player_score += 1
            result = "Player won"
            player_streak += 1
            computer_streak = 0
            longest_player_streak = max(
                longest_player_streak, player_streak
            )
        else:
            print("paper covers rock,hence you losee.")
            computer_score += 1
            result = "computer won"
            computer_streak += 1
            player_streak = 0
            longest_computer_streak = max(
                longest_computer_streak, computer_streak
            )

    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock,yee you win a point!")
            player_score += 1
            result = "Player won"
        else:
            print("scissors cuts paper,oh no you lose!!.")
            computer_score += 1
            result = "computer won"

    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors chopped the paper in shreds,you winn!.")
            player_score += 1
            result = "Player won"
        else:
            print("rock smashes scissors,and so does your score!")
            computer_score += 1
            result = "computer won"
#to store match history ok?
    match_history.append(
        (round_number, user_action, computer_action, result)
    )

print("your score is:",player_score)
print("computer's score is:",computer_score)
print("ties,if any are",ties)

if player_score > computer_score:
    print("you won!!")
elif computer_score > player_score:
    print("computer won, you lose hehe.")
else:
    print("the game ended in a tie!")

print("\n========== MATCH HISTORY ==========")

for round_data in match_history:
    round_number, user_action, computer_action, result = round_data

    print(f"\nRound {round_number}")
    print(f"your move: {user_action}")
    print(f"computer move: {computer_action}")
    print(f"result: {result}")

print("\n========== STREAK RECORDS ==========")
print("Longest player winning streak:", longest_player_streak)
print("Longest computer winning streak:", longest_computer_streak)

print("\n========== PERFORMANCE RATING ==========")

total_rounds = len(match_history)

if total_rounds > 0:
    win_rate = (player_score / total_rounds) * 100

    print(f"your win percentage is {win_rate:.2f}%")

    if win_rate == 100:
        print("rating: PERFECT MATCH!")
    elif win_rate >= 60:
        print("rating: EXCELLENT!")
    elif win_rate >= 40:
        print("rating: GOOD EFFORT!")
    else:
        print("rating: KEEP PRACTISING!")

#achievements 
if player_score >= 1:
    print("🏆 achievement unlocked : FIRST VICTORY!")

if player_score == total_rounds:
    print("👑 achievement unlocked : PERFECT MATCH!")

if longest_player_streak >= 3:
    print("🔥 achievement unlocked: STREAK MASTER!")

if ties == total_rounds:
    print("🤝 achievement unlocked: PEACEFUL PLAYER!")

if player_score == 0 and computer_score == 0:
    print("🎲 achievement unlocked : THE GREAT EQUALIZER!")

print("rounds won:", player_score)
print("rounds lost:", computer_score)
print("rounds tied:", ties)

print("🎮 thanks for playing rock-papers-scissors!")
print(f"📊 total rounds played: {len(match_history)}")
print("✨come back and beat your high score when you're ready!")
