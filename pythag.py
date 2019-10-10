from banner import banner
import math

#Collect a, b, and c function
def pythag(a,b,c):
    if a == "":
        side_to_solve = "a"
        b = float(b)
        c = float(c)
        answer = math.sqrt(pow(c, 2) - pow(b, 2))
    elif b == "":
        side_to_solve = "b"
        a = float(a)
        c = float(c)
        answer = math.sqrt(pow(c, 2) - pow(a, 2))
    elif c == "":
        side_to_solve = "c"
        a = float(a)
        b = float(b)
        answer = math.sqrt(pow(a, 2) + pow(b, 2))
    else:
        answer = "ERROR"
    return answer
    

#Collect a, b, and c program
if __name__=="__main__":
    #Banner
    banner("PYTHAGOREAN CALCULATOR", "Nate Sherman")
    #intro
    print("We will help you find the missing side of a right triangle. The lengths of the two")
    print("legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
    print('')
    print('')
    while True:
        print("Please inter the length of each side, or leave it blank if you don't know.")
        a_input = input("a = ")
        b_input = input("b = ")
        c_input = input("c = ")
        if a_input == "":
            side_to_solve = "a"
        elif b_input == "":
            side_to_solve = "b"
        elif c_input == "":
            side_to_solve = "c"
        answer = pythag(a_input, b_input, c_input)
        if answer == "ERROR":
            print("ERROR: Check your data and try again")
        else:
            print(f"Your missing side is {side_to_solve} and its length is {answer}.")
        # Run Again?
        again = input("Would you like to calculate another triangle (Y/N)")
        if again.upper() == "N":
            print("Thank you for using the Pythagorean Calculator.")
            break
        elif again.upper() == "Y":
            continue
        else:
            print("ERROR: Unsupported input. This program will continue.")
            continue