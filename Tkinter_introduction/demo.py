from tkinter import *

window = Tk()
window.title("Demo Project")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = Label()
my_label.config(text="This is a label")
my_label.grid(column=0, row=0)

button = Button(text="Button")
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
entry.grid(column=3, row=3)


window.mainloop()
