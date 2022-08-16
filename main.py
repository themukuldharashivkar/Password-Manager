from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_entered = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='ERROR', message='No Data File Found')
    else:
         if website_entered in data:
            email_req = data[website_entered]['email']
            pass_req = data[website_entered]['password']
            messagebox.showinfo(title=website_entered, message=f"Email: {email_req} \nPassword: {pass_req}")
         else:
             messagebox.showinfo(title='ERROR', message=f'No details found for the {website_entered}entered.')



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Error', message="PLease make sure you haven't left any fields empty")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website = Label(text='Website:')
website.grid(row=1, column=0)
email = Label(text='Email/Username:')
email.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'dharashivkarmukul@gmail.com')
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# buttons
generate_password_btn = Button(text='Generate Pass', width=11, command=generate_password)
generate_password_btn.grid(row=3, column=2)
add_btn = Button(text='Add', width=39, command=save)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn = Button(text='Search', width=11, command=find_password)
search_btn.grid(row=1, column=2)

window.mainloop()
