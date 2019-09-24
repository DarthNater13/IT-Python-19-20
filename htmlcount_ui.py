from banner import banner
import os
def get_full_path(name):
    filename = os.path.join(".", "testing", f"{name}.html")
    return filename

def load(name):
    data = []
    filename = get_full_path(name)
    print(f"Loading {filename}")
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                alltag_count = data.count("<")
                endtag_count = data.count("</")
                tag_calc(alltag_count, endtag_count, filename)
        return data
        print("File sucessfully loaded.")
    else:
        print("ERROR: File doesn't exist.")

def tag_calc(all_tag, end_tag, filename):
    finaltag_count = int(all_tag - end_tag)
    print(f"The file {filename} has {finaltag_count} tags")
   
#------------------------------------------------------------

def main():
    filename = input("Please enter the name of an HTML file: ")
    tag_data = load(filename)
    while True:
        start_again = input("Would you like to count another html file (Y/N)?")
        if start_again.upper() == "Y":
            main()
            break
        elif start_again.upper() == "N":
            print("Thank you for using the HTML tag counter. Goodbye!")
            break
        else:
            print("Sorry, I don't understand")

banner("HTML TAG COUNTER", "Nate Sherman")
print("Welcome to the HTML tag counter")
main()


