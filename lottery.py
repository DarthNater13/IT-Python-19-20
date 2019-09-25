from banner import banner
import random
import time
#-------------------------------*_VARIABLES_*---------------------------------------------
balance = int(20)
#-------------------------------*_FUNCTIONS_*---------------------------------------------
def bet(bet_amount, guess, the_number):
    global balance
    if guess == the_number:
        balance += (bet_amount * 10)
        print(f"Awesome, you chose {guess}, and so did the computer! You win ${(bet_amount * 10)} this round.")
    else:
        balance -= bet_amount
        print(f"I'm sorry, but you chose {guess} and the computer chose {the_number}. You lose ${bet_amount} this round.")
#---------------------------*_START OF GAMEPLAY_*-----------------------------------------
#------------------------------*_INTRODUCTION_*-------------------------------------------
banner("LOTTERY","Nate Sherman")
print("Welcome to the Lottery Game. Choose a number between 1 and 5. If you choose the")
print("same number as the computer, you will win 10 times your bet amount.")
time.sleep(1)
#__--------------------------------*_MAIN_*-----------------------------------------------
while True:
    print(f"BALANCE: ${balance}")
    bet_amount = int(input("How much do you want to bet? "))
    player_number = int(input("What number do you want to pick? "))
    the_number = random.randint(1, 5)
    time.sleep(1)
    bet(bet_amount, player_number, the_number)
    time.sleep(1)
    if balance >= 999999:
        print("Congratulations, you're rich now!")
        play_again = input("Would you like to play again (Y/N)?")
        if play_again.upper() == "N":
            print("Thank you for playing!")
            break
        else:
            balance = 20
    elif balance <= 1:
        print("Sorry, but you have no money. You lose.")
        play_again = input("Would you like to play again (Y/N)?")
        if play_again.upper() == "N":
            print("Thank you for playing!")
            break
        else:
            balance = 20
    else:
        continue