from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web= website_entry.get()
    username= email_username_entry.get()
    passs = password_entry.get()

    if len(username) == 0 or len(passs) == 0:
        messagebox.showinfo(title='oops', message='Please don\'t leave any entry empty!')
    else:
        is_ok = messagebox.askokcancel(title=web, message=f'Are you sure you want to save this? \nemail: {username}\npassword: {passs}')
        if is_ok:
            with open('passwords.txt', 'a') as file:
                file.write(f'Website: {web} /Username,email: {username} /Password: {passs}\n')

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
website.grid(column=0,row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2)

email_username = Label(text='Email/Username:')
email_username.grid(column=0,row=2)
email_username_entry = Entry(width=35)
email_username_entry.insert(0,'maachouhicham093@gmail.com')
email_username_entry.grid(column=1,row=2,columnspan=2)

password = Label(text='Password:')
password.grid(column=0,row=3)
password_entry= Entry(width=21)
password_entry.grid(column=1,row=3)

generate_pass = Button(text='Generate Password',width=14)
generate_pass.grid(column=2,row=3)


add = Button(text='Add', width=35,command=add)
add.grid(column=1,row=4,columnspan=2)



window.mainloop()