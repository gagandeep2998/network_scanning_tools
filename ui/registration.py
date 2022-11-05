from tkinter import *
from tkinter import messagebox
import ui.login
import requests


class Register:
    def __init__(self):
        self.is_auth = False
        self.window = Tk()
        self.window.geometry("1024x720")
        self.window.title("Register New User")
        self.window.config(padx=350, pady=200)

        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file='ui/assets/images/logo.png')
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0)

        self.name_label = Label(text='Name: ')
        self.name_label.grid(column=0, row=1, padx=10, pady=10)

        self.name_entry = Entry(width=35)
        self.name_entry.grid(column=1, row=1, padx=10, pady=10)
        self.name_entry.focus()

        self.email_label = Label(text='Email: ')
        self.email_label.grid(column=0, row=2, padx=10, pady=10)

        self.email_entry = Entry(width=35)
        self.email_entry.grid(column=1, row=2, padx=10, pady=10)

        self.password_label = Label(text='Password: ')
        self.password_label.grid(column=0, row=3, padx=10, pady=10, sticky='EW')

        self.pass_entry = Entry(width=35, show='*')
        self.pass_entry.grid(column=1, row=3, padx=10, pady=10, sticky='EW')

        self.signup_button = Button(text='Sign Up', command=self.registration)
        self.signup_button.grid(column=1, row=4, padx=10, pady=10)

        self.login_screen_button = Button(text='Have account, Login', command=self.login_window)
        self.login_screen_button.grid(column=1, row=5, padx=10, pady=10)

        self.window.mainloop()

    def registration(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.pass_entry.get()
        new_user_data = {
            'name': name,
            'email': email,
            'password': password,
        }
        response = requests.post('http://127.0.0.1:5000/register',
                                 params=new_user_data)
        print(response.status_code)
        if response.status_code == 201:
            messagebox.showinfo(title='Success',
                                message='New User Registered Successfully!')
            self.login_window()
        elif response.status_code == 409:
            messagebox.showinfo(title='Error',
                                message='You are already registered with this email, login instead !')
            self.name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.pass_entry.delete(0, END)
            self.name_entry.focus()

        # if email == 'admin' and password == 'password':
        #
        #     self.is_auth = True
        #     self.window.destroy()
        # else:
        #
        #     self.email_entry.delete(0, END)
        #     self.pass_entry.delete(0, END)
        #     self.email_entry.focus()

    def login_window(self):
        self.window.destroy()
        auth = ui.login.Auth()

# register = Register()
