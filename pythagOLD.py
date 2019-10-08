from banner import banner
import math

#Banner
banner("PYTHAGOREAN CALCULATOR", "Nate Sherman")
#intro
print("We will help you find the missing side of a right triangle. The lengths of the two")
print("legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
print('')
print('')
#Collect a, b, and c
while True:
    print("Please inter the length of each side, or leave it blank if you don't know.")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    if a == "":
        b = float(b)
        c = float(c)
        answer = math.sqrt(pow(c, 2) - pow(b, 2))
        print(f"Your missing side is a and its length is {answer}.")
    elif b == "":
        a = float(a)
        c = float(c)
        answer = math.sqrt(pow(c, 2) - pow(a, 2))
        print(f"Your missing side is b and its length is {answer}.")
    elif c == "":
        a = float(a)
        b = float(b)
        answer = math.sqrt(pow(a, 2) + pow(b, 2))
        print(f"Your missing side is c and its length is {answer}.")
    else:
        print("ERROR: Invalid entry. Please try again.")
    again = input("Would you like to calculate another triangle (Y/N)")
    if again.upper() == "N":
        print("Thank you for using the Pythagorean Calculator.")
        break
    elif again.upper() == "Y":
        continue
    else:
        print("ERROR: Unsupported input. This program will continue.")
        continue