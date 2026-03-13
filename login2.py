import mysql.connector as mysql
import tkinter as gui
from tkinter import messagebox
from Registration_2 import register as open_register  # import the register function

# Connect to MySQL database
cn = mysql.connect(
    host="localhost",
    user="root",
    password="Shaeeb@1881",
    database="STUDENT"
)

# ------------------- Main Login Window ------------------- #
w = gui.Tk()
w.title("Login")
w.geometry("300x200")

# Labels
gui.Label(w, text="Username", font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
gui.Label(w, text="Password", font=('Arial', 14)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
gui.Label(w, text="Don't have an account?", font=('Arial', 10)).grid(row=3, column=0, padx=10, pady=5, sticky='w')

# Entry fields
user_entry = gui.Entry(w, width=20, font=('Arial', 14))
pwd_entry = gui.Entry(w, width=20, font=('Arial', 14), show='*')
user_entry.grid(row=0, column=1, padx=10, pady=5)
pwd_entry.grid(row=1, column=1, padx=10, pady=5)

# Login function
def login():
    user = user_entry.get().strip()
    pwd = pwd_entry.get().strip()

    if not user or not pwd:
        messagebox.showerror("Error", "Please enter both Username and Password")
        return

    c = None
    try:
        c = cn.cursor()
        c.execute("SELECT * FROM user_register WHERE uname=%s AND pwd=%s", (user, pwd))
        row = c.fetchone()

        if row is None:
            messagebox.showinfo("Info", "Invalid Username or Password")
        else:
            messagebox.showinfo("Welcome", f"Welcome {row[1]}!")  # row[1] = name
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"MySQL Error: {e}")
    finally:
        if c:
            c.close()

# Button functions
def exit_app():
    w.destroy()

# Buttons
gui.Button(w, text="Login", font=('Arial', 14), command=login).grid(row=2, column=0, padx=10, pady=10)
gui.Button(w, text="Exit", font=('Arial', 14), command=exit_app).grid(row=2, column=1, padx=10, pady=10)
gui.Button(w, text="Register", font=('Arial', 10), command=lambda: open_register(cn)).grid(row=3, column=1, padx=10, pady=5)

w.mainloop()
