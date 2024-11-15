from tkinter import Tk, Label, Canvas, Button, PhotoImage, Entry
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = [choice(letters) for _ in range(randint(8, 10))]
  password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
  password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

  shuffle(password_list)

  password = "".join(password_list)

  password_entry.insert(0, string=password)

  pyperclip.copy(password)
  
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    print(len(website))
    print(len(email_username))
    print(len(password))

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning(title='OOPS', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email_username} \nPassword: {password} \nIs it ok to save?')
        
        if is_ok:
            with open(r'Day29_PswMangrGUIApp/data.txt',mode='a') as data_saver:
                data_saver.write(f'{website} || {email_username} || {password}\n')

            website_entry.delete(0,'end')
            password_entry.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title('Password Manager')
window.config(padx=30,pady=30)

# Canvas And Image
img_path = r'Day29_PswMangrGUIApp\logo.png'
logo_img = PhotoImage(file=img_path)
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# Website Label
website_label = Label()
website_label.config(text='Website:',font=('Times New Roman',10,'bold'))
website_label.grid(column=0, row=1)

# Email/Username Label
email_username_label = Label()
email_username_label.config(text='Email/Username:',font=('Times New Roman',10,'bold'))
email_username_label.grid(column=0, row=2)

# Password Label
password_label = Label()
password_label.config(text='Password:',font=('Times New Roman',10,'bold'))
password_label.grid(column=0, row=3)

# Website Entry
website_entry = Entry()
website_entry.config(width=38)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2, sticky='w')

# Email/Username Entry
email_username_entry = Entry()
email_username_entry.config(width=38)
email_username_entry.grid(column=1,row=2,columnspan=2, sticky='w')
email_username_entry.insert(0,'btc2themoon@gmail.com')

# Password Entry
password_entry = Entry()
password_entry.config(width=22)
password_entry.grid(column=1,row=3, sticky='w')

# GeneratePassword Button
generate_password_button = Button()
generate_password_button.config(text='Generate Password',font=('Times New Roman',10,'bold'), command=generate_password)
generate_password_button.grid(column=2,row=3, sticky='e')

# Add Button
add_button = Button()
add_button.config(text='Add',font=('Times New Roman',10,'bold'), width=32, command=save)
add_button.grid(column=1,row=4,columnspan=2, sticky='w')

window.mainloop()