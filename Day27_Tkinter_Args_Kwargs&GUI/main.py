# from tkinter import Tk, Label
from tkinter import *

def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)
window.config(padx=10,pady=10)

#Label
my_label = Label(text='I am a label', font=('Arial',24,'bold'))
my_label.config(text='New Text')
my_label.grid(column=0,row=0)

# Button
button = Button(text='Click Me', command=button_clicked)
button.grid(column=1,row=1)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)

# Button
new_button = Button(text='Click Me', command=button_clicked)
new_button.grid(column=2,row=0)

mainloop()