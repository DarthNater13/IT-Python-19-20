import datetime

from banner import banner

banner("BIRTHDAY", "Nate Sherman")

# Process
# 1. Find out birthday from user
# 2. Calculate how many days apart that is from now
# 3. Print the birthday info, Days to go, Days ago, or Happy BDAY!

def main():
    birthday = get_birthday_from_user()
    now = datetime.date.today()
    calulate_days_between_dates(birthday, now)
    print_birthday_info()

def get_birthday_from_user():
    print("What is your birthday?")
    year = int(input("Year [YYYY]? "))
    month = int(input("Month [MM]? "))
    day = int(input("Day [DD]? "))

    birthday = datetime.date(year, month, day)
    return birthday

def calulate_days_between_dates(date1, date2):
    pass

def print_birthday_info():
    pass

main()