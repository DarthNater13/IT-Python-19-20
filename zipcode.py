from banner import banner
banner('ZIP CODE SORTER','Nate Sherman')
location = 'Undefined'
zcode = 0
repeat = "N"
def zipcode():
    global location
    global zcode
    zcode = int(input("Please enter a zip code: "))
    if zcode == 49309:
        location = "Bitely"
    elif zcode == 49312:
        location = "Brohman"
    elif zcode == 49337:
        location = "Croton and Newaygo"
    elif zcode == 49412:
        location = "Fremont"
    elif zcode == 49413:
        location = "Fremont"
    elif zcode == 49327:
        location = "Grant"
    elif zcode == 49349:
        location = "White Cloud"
    else:
        location = "nothing"       
def lreturn():
    global location
    global zcode
    global repeat
    print(f"The zip code {zcode} is for {location}.")
    repeat = input("Would you like to enter another zip code (Y/N)?")
    if repeat == 'Y' or "y":
        zipcode()
        lreturn()
    else:
        print('Thank you for using the Newaygo County zip code sorter. Goodbye!')
zipcode()
lreturn()