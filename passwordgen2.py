import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

# Initialize and set up the database
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
db.commit()
db.close()

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password_length = IntVar()
        self.generated_password = StringVar()

        self.setup_ui()

    def setup_ui(self):
        self.master.title('Password Generator')
        self.master.geometry('680x400')
        self.master.config(bg='#2C3E50')
        self.master.resizable(False, False)

        title_label = Label(self.master, text="Password Generator", font='Helvetica 24 bold', bg='#2C3E50', fg='#ECF0F1')
        title_label.pack(pady=20)

        frame = Frame(self.master, bg='#2C3E50')
        frame.pack(pady=10)

        username_label = Label(frame, text="Enter User Name:", font='Helvetica 14', bg='#2C3E50', fg='#ECF0F1')
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
        username_entry = Entry(frame, textvariable=self.username, font='Helvetica 14', bd=5, relief='groove')
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_length_label = Label(frame, text="Password Length:", font='Helvetica 14', bg='#2C3E50', fg='#ECF0F1')
        password_length_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
        password_length_entry = Entry(frame, textvariable=self.password_length, font='Helvetica 14', bd=5, relief='groove')
        password_length_entry.grid(row=1, column=1, padx=10, pady=10)

        generated_password_label = Label(frame, text="Generated Password:", font='Helvetica 14', bg='#2C3E50', fg='#ECF0F1')
        generated_password_label.grid(row=2, column=0, padx=10, pady=10, sticky=E)
        generated_password_entry = Entry(frame, textvariable=self.generated_password, font='Helvetica 14', bd=5, relief='groove', fg='#E74C3C')
        generated_password_entry.grid(row=2, column=1, padx=10, pady=10)

        button_frame = Frame(self.master, bg='#2C3E50')
        button_frame.pack(pady=10)

        generate_button = Button(button_frame, text="Generate Password", font='Helvetica 14 bold', bg='#27AE60', fg='#ECF0F1', command=self.generate_password)
        generate_button.grid(row=0, column=0, padx=10, pady=10)

        accept_button = Button(button_frame, text="Accept", font='Helvetica 14 bold', bg='#2980B9', fg='#ECF0F1', command=self.accept_fields)
        accept_button.grid(row=0, column=1, padx=10, pady=10)

        reset_button = Button(button_frame, text="Reset", font='Helvetica 14 bold', bg='#C0392B', fg='#ECF0F1', command=self.reset_fields)
        reset_button.grid(row=0, column=2, padx=10, pady=10)

    def generate_password(self):
        username = self.username.get().strip()
        try:
            length = int(self.password_length.get())
        except ValueError:
            messagebox.showerror("Error", "Password length must be an integer")
            return

        if not username:
            messagebox.showerror("Error", "Username cannot be empty")
            return
        if not username.isalpha():
            messagebox.showerror("Error", "Username must be a string")
            self.username.set("")
            return
        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            return

        characters = string.ascii_letters + string.digits + "@#%&()\"?!"
        password = ''.join(random.choice(characters) for _ in range(length))
        self.generated_password.set(password)

    def accept_fields(self):
        username = self.username.get().strip()
        generated_password = self.generated_password.get().strip()

        if not username or not generated_password:
            messagebox.showerror("Error", "Username and generated password cannot be empty")
            return

        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE Username = ?", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "This username already exists! Please use another username")
            else:
                cursor.execute("INSERT INTO users (Username, GeneratedPassword) VALUES (?, ?)", (username, generated_password))
                db.commit()
                messagebox.showinfo("Success", "Password generated successfully")

    def reset_fields(self):
        self.username.set("")
        self.password_length.set(0)
        self.generated_password.set("")


if __name__ == '__main__':
    root = Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
