from banner import banner
import time

# Process
# 1. Create a banner
# 2. Create a defined list of options like RPS
# 3. Play the game, best of 3
    # 1. Display current score
    # 2. Present Player with options of r, p, and s
    # 3. Compare the players choice with computer's random choice
# 4. Print game results
# ------------------------------------------------------------------

# Banner
banner("CREATE YOUR OWN GAME", "Nate Sherman")

# List
choicelist = ["Fire", "Wood", "Poison", "Water"]

# Pregame
first = choicelist[0]
last_int = len(choicelist) -1
last = choicelist[last_int]
startinglist = 0


# Rules
print(f"In this game, there are {len(choicelist)} choices.")
time.sleep(1)
print('The choices are:')
print(*choicelist, sep='\n')
print("These options are ordered in the way that they beat each other.")
print("The choice at the top beats the choice at the bottom", end="")
print(f", with the excepton of {last} beating {first}.")
ex = input("Do you understand? (y/n) ")
if ex = "n" or "no":
    print("Example:")
    print(f"If you play {choicelist[1]}, and the computer plays {choicelist[0]}, the computer would win the round.")
else:
    break





















