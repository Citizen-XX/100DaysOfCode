from tkinter import *

def button_clicked():
    print('I got clicked')
    miles = float(entry.get())
    kms = str(round(miles*1.60934,2))
    my_label.config(text=kms)

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=285,height=100)
window.config(padx=10,pady=10)

my_label = Label(text='0', font=('Times New Roman',16,'bold'))
my_label.grid(column=1,row=1)

equal_to_label = Label(text='Is equal to:', font=('Times New Roman',16))
equal_to_label.grid(column=0,row=1)

km_label = Label(text='Km', font=('Times New Roman',16))
km_label.grid(column=2,row=1)

miles_label = Label(text='Miles', font=('Times New Roman',16))
miles_label.config(padx=5)
miles_label.grid(column=2,row=0)

entry = Entry(width=6)
print(entry.get())
entry.grid(column=1,row=0)

button = Button(text='Calculate', command=button_clicked)
button.grid(column=1,row=2)

mainloop()