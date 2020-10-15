from banner import banner
import random

# 1. Make a banner
# 2. Print Intro
# 3. Play the game, best of 3
    # 1. Display current score
    # 2. Present Player with options of r, p, and s
    # 3. Compare the players choice with computer's random choice
# 4. Print game results
# ------------------------------------------------------------------

#Print Banner from Banner.py / Intro
banner("ROCK PAPER SCISSORS", "Nate Sherman")

print('')
print("We are going to play Rock, Paper, Scissors. The first to win two out of the three")
print("rounds is the winner.")
print('')
# Scoring Variables (Global)
player_total = 0
computer_total = 0
player_choice = 0
computer_choice = 0
round_result = "loss"

# Functions
#  Prints Score
def score():
    print(f"SCORE: Player: {player_total} Computer: {computer_total}")
    print('')
# Selection of rock, paper, or scissors
def choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    global player_choice
    global computer_choice
    player_choice = int(input("What is your choice? "))
    computer_choice = random.randint(1, 3)


#calculates values of round outcome
def game_calc():
    global player_choice
    global computer_choice
    global round_result
    if player_choice == 1 and computer_choice == 2:
        round_result = "loss"
    elif player_choice == 1 and computer_choice == 3:
        round_result = "win"
    elif player_choice == 2 and computer_choice == 1:
        round_result = "win"
    elif player_choice == 2 and computer_choice == 3:
        round_result = "loss"
    elif player_choice == 3 and computer_choice == 1:
        round_result = "loss"
    elif player_choice == 3 and computer_choice == 2:
        round_result = "win"
    else:
        round_result = "tie"

#Prints Results
def results():
    global round_result
    global player_total
    global computer_total
    # Calculates results
    if player_choice == 1:
        player_choice_txt = "Rock"
    elif player_choice == 2:
        player_choice_txt = "Paper"
    else:
        player_choice_txt = "Scissors"

    if computer_choice == 1:
        computer_choice_txt = "Rock"
    elif computer_choice == 2:
        computer_choice_txt = "Paper"
    else:
        computer_choice_txt = "Scissors"

    #Prints results
    if round_result == "win":
        print(f"You chose {player_choice_txt}, and the computer chose {computer_choice_txt}. You win this round.")
        player_total = player_total + 1
    elif round_result == "loss":
        print(f"You chose {player_choice_txt}, and the computer chose {computer_choice_txt}. You lost this round.")
        computer_total = computer_total + 1
    else:
        print(f"You chose {player_choice_txt}, and the computer chose {computer_choice_txt}. It is a tie.")

# Gameplay
def main():
    score()
    choice()
    game_calc()
    results()
    reset_game()
# Resets the game if needed
def reset_game():
    if player_total == 3:
        print("You have defeated the computer in honorable battle! It was pure hubris for the")
        print("computer to think it could win against such a formidable opponent. Congratulations!")
    elif computer_total == 3:
        print("You have lost to the computer in honorable battle! It was a tough battle")
        print("for you to take on. Keep practicing and better luck next time! See you soon!")
    else:
        main()
# Starts game for first time
main()