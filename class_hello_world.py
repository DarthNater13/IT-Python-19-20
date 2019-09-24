# Write your code here :-)
from os import system, name
from time import sleep
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def error():
    print ('ERROR: Please try again.')
    sleep(5)
    restart == True

def start():
    print('=========================')
    print('         WELCOME         ')
    print('  Press enter to begin   ')
    print('=========================')
    start = input ('')
def main():
    print ("Hello!")
    print ("I'm so excited to meet you!")
    YourName = input ('What is your name?')
    if YourName == ('' or ' '):
        error()
    else:
        print (f'Nice to meet you, {YourName}')
    Location = input ('Where do you go to school? : A)Fremont B)Grant C)Newaygo D)Tri County E)White Cloud')
    if Location == "A":
        print ('Go Packers!')
    elif Location == "B":
        print ('Go Tigers!')
    elif Location == "C":
        print ('Go Lions!')
    elif Location == "D":
        print ('Go Vikings!')
    elif Location == "E":
        print ('Go Indians!')
    else:
        error()
while True:
    start()
    main()