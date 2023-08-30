from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def search():
    web= website_entry.get()
    try:
        with open('passwords.json') as file:
            data = json.load(file)
            if web in data:
                messagebox.showinfo(title=web, message=f'Username: {data[web]["username"]}\nPassword: {data[web]["password"]}')
            else:
                messagebox.showinfo(title='Website not found!',message='No details for the website exist')    
    except FileNotFoundError:
        messagebox.showerror(title='File not found!',message='File not found')  
            


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_random = [random.choice(letters) for char in range(nr_letters)]
   
    sym_random = [random.choice(symbols) for char in range(nr_symbols)]
    
    num_random = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = letters_random+sym_random+num_random
    random.shuffle(password_list)

    password = "".join(password_list)
    
    if len(password_entry.get()) != 0:
        password_entry.delete(0,END) 
        password_entry.insert(END, password)
        pyperclip.copy(password)
    else:
        password_entry.insert(END, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web= website_entry.get()
    username= email_username_entry.get()
    passs = password_entry.get()
    loaded_data = {}
    data = {web:{
        "username" :username,
        "password" : passs
    }}
    if len(web) == 0 or len(passs) == 0:
        messagebox.showinfo(title='oops', message='Please don\'t leave any entry empty!')
    else:
        is_ok = messagebox.askokcancel(title=web, message=f'Are you sure you want to save this? \nwebsite: {web}\nemail: {username}\npassword: {passs}')
        if is_ok:
            try:
                with open('passwords.json', 'r') as file:
                    loaded_data = json.load(file)
                    loaded_data.update(data)
            except FileNotFoundError:
                with open('passwords.json','w') as file:
                    json.dump(data,file,indent=2)  
            except Exception:
                with open('passwords.json','w') as file:
                    json.dump(data,file,indent=2)               
            else:
                with open('passwords.json','w') as file:
                    json.dump(loaded_data,file,indent=2)


            website_entry.delete(0,END)  
            password_entry.delete(0,END)   
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
canvas.grid(column=1,row=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo)

website = Label(text='Website:')
website.grid(column=0,row=1,sticky=NSEW)
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1,row=1,sticky=NSEW)
search_button = Button(text='Search',width=14,command=search)
search_button.grid(column=2,row=1,sticky=NSEW)

email_username = Label(text='Email/Username:')
email_username.grid(column=0,row=2,sticky=NSEW)
email_username_entry = Entry(width=35)
email_username_entry.insert(0,'maachouhicham093@gmail.com')
email_username_entry.grid(column=1,row=2,columnspan=2,sticky=NSEW)

password = Label(text='Password:')
password.grid(column=0,row=3,sticky=NSEW)
password_entry= Entry(width=21)
password_entry.grid(column=1,row=3,sticky=NSEW)

generate_pass = Button(text='Generate Password',width=14,command=generator)
generate_pass.grid(column=2,row=3,sticky=NSEW)


add = Button(text='Add', width=35,command=add)
add.grid(column=1,row=4,columnspan=2,sticky=NSEW)



window.mainloop()