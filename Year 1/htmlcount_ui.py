from banner import banner
import os
import time
def get_full_path(name):
    filename = os.path.join(".", "testing", f"{name}.html")
    return filename

def load(name):
    data = []
    filename = get_full_path(name)
    print(f"Loading {filename}")
    time.sleep(1)
    if os.path.exists(filename):
        with open(filename) as fin:
            for line in fin.readlines():
                data.append(line.rstrip())     
        print("File sucessfully loaded.")
        time.sleep(1)
    else:
        print("ERROR: File doesn't exist.")
    return data
def tag_calc(line):
    return line.count("<") - line.count("</")
   
#------------------------------------------------------------

def main():
    
    while True:
        filename = input("Please enter the name of an HTML file: ")
        tag_data = load(filename)
        finaltag_count = 0
        for line in tag_data:
            finaltag_count += tag_calc(line)
        print(f"The file {filename} has {finaltag_count} tags")
        start_again = input("Would you like to count another html file (Y/N)?")
        if start_again.upper() == "N":
            print("Thank you for using the HTML tag counter. Goodbye!")
            break


banner("HTML TAG COUNTER", "Nate Sherman")
print("Welcome to the HTML tag counter")
main()


