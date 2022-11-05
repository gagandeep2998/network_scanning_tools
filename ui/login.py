from tkinter import *
from tkinter import messagebox
import ui.registration
import requests


class Auth:
    def __init__(self):
        self.is_auth = False
        self.window = Tk()
        self.window.geometry("1024x720")
        self.window.title("Login")
        self.window.config(padx=350, pady=200)

        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file='ui/assets/images/logo.png')
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(column=1, row=0)

        self.email_label = Label(text='Email: ')
        self.email_label.grid(column=0, row=1, padx=10, pady=10)

        self.email_entry = Entry(width=35)
        self.email_entry.grid(column=1, row=1, padx=10, pady=10)
        self.email_entry.focus()

        self.password_label = Label(text='Password: ')
        self.password_label.grid(column=0, row=2, padx=10, pady=10, sticky='EW')

        self.pass_entry = Entry(width=35, show='*')
        self.pass_entry.grid(column=1, row=2, padx=10, pady=10, sticky='EW')

        self.login_button = Button(text='Login', command=self.authentication)
        self.login_button.grid(column=1, row=3, padx=10, pady=10)

        self.registration_button = Button(text='Register New User', command=self.registration_window)
        self.registration_button.grid(column=1, row=4, padx=10, pady=10)

        self.window.mainloop()

    def authentication(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()
        user_data = {
            'email': email,
            'password': password,
        }
        response = requests.get('http://127.0.0.1:5000/login',
                                params=user_data)

        if response.status_code == 200:
            messagebox.showinfo(title='Success', message='Welcome!')
        elif response.status_code == 404:
            messagebox.showinfo(title='Error', message='User not found!')
        else:
            messagebox.showinfo(title='Error',
                                message='Email or Password incorrect, try again!')

        # if username == 'admin' and password == 'password':
        #
        #     self.is_auth = True
        #     self.window.destroy()
        # else:
        #     messagebox.showinfo(title='Error', message='Wrong username or password!')
        #     self.username_entry.delete(0, END)
        #     self.pass_entry.delete(0, END)
        #     self.username_entry.focus()

    def registration_window(self):
        self.window.destroy()
        register = ui.registration.Register()
