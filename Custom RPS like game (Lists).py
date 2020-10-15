from banner import banner
import time
import random

# Process
# 1. Create a banner
# 2. Create a defined list of options like RPS
# 3. Play the game, best of 3
    # 1. Display current score
    # 2. Present Player with options of r, p, and s
    # 3. Compare the players choice with computer's random choice
# 4. Print game results
# ------------------------------------------------------------------

# List (MUST NUMBER STARING WITH 0)
choicelist = ["Fire", "Wood", "Poison", "Water"]


#Clear the screen
def clearscreen():
    print("\033[H\033[J")

# Banner
banner("LISTS AND STUFF", "Nate Sherman")
time.sleep(2)
clearscreen()

# Pregame
first = choicelist[0]
last_int = len(choicelist) -1
last_convert = choicelist[last_int]
first_int = 0
startinglist = 0
playerscore = 0
computerscore = 0
playerchoice = 0
computerchoice = 0

# Rules
print(f"In this game, there are {len(choicelist)} choices.")
time.sleep(1)
print('The choices are:')
for num, item in enumerate(choicelist):
    print(f"{num}. {item}")

print("These options are ordered in the way that they beat each other.")
print("The choice at the top beats the choice at the bottom", end="")
print(f", with the excepton of {choicelist[-1]} beating {first}.")
ex = input("Do you understand? (y/n) ")
if ex == 'n' or 'no':
    print("Example:")
    print(f"If you play {choicelist[1]}, and the computer plays {choicelist[0]}, the computer would win the round.")
if ex == 'y' or 'yes':
    print("Let's begin!")
time.sleep(1)
clearscreen()
# Fix if than statements

#Gameplay (Round)
def round():
    global playerscore
    global computerscore
    global last_int
    global choicelist
    global playerchoice
    global computerchoice
    print(f"SCORE: You: {playerscore} Computer: {computerscore}")
    for num, item in enumerate(choicelist):
        print(f"{num}. {item}")
    playerchoice = int(input("Select a number corresponding to one of the following options: "))
    computerchoice = random.randint(0, last_int)
    time.sleep(1)
    clearscreen()

#RuleSet
def ruleset():
    global playerchoice
    global computerchoice
    global last_int
    num, item in enumerate(choicelist)
    if playerchoice == num:
        pass
round()