import attendence
import tkinter

window = tkinter.Tk()
window.title("Attendence")

# creating 2 text labels and input labels

tkinter.Label(window, text = "Student ID").grid(row = 0) # this is placed in 0 0
# 'Entry' is used to display the input-field
tkinter.Entry(window).grid(row = 0, column = 1) # this is placed in 0 1
# 'Checkbutton' is used to create the check buttons
tkinter.Checkbutton(window, text = "Leaving Early").grid(columnspan = 2) # 'columnspan' tells to take the width of 2 columns
tkinter.Button(window, text = "Sign me in!").grid(row = 1)
window.mainloop()