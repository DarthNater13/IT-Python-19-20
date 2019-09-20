import journal
from banner import banner
banner("DEEP THOUGHTS", "Nate Sherman")

def main():
    run_event_loop()

def run_event_loop():
    filename = "default"
    journal_data = journal.load(filename)#[]

    while True:
        command = input("[L]ist entries, [A]dd an entry, E[x]it: ")
        if command.upper() == "L":
            list_entry(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() == "X":
            break
        else:
            print("Sorry, I don't understand")
    journal.save(filename, journal_data)

def list_entry(data):
    print("Your journal entries:")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"{num+1} - {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: \n")
    journal.add_entry(entry, data)
    #data.append(entry)
    

main()