import tkinter as gui
from tkinter import messagebox
import mysql.connector as mysql

# Connect to MYSQL database
cn = mysql.connect(database='STUDENT',user='root',password='Shaeeb@1881',host='localhost')
print(cn)

def register(cn):  # pass the database connection from login.py
    reg_win = gui.Toplevel()   # create a new window
    reg_win.title("Register")
    reg_win.geometry("350x250")

    # Labels
    gui.Label(reg_win, text="Name", font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    gui.Label(reg_win, text="Username", font=('Arial', 14)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    gui.Label(reg_win, text="Password", font=('Arial', 14)).grid(row=2, column=0, padx=10, pady=5, sticky='w')

    # Entry fields
    e1 = gui.Entry(reg_win, width=20, font=('Arial', 14))
    e2 = gui.Entry(reg_win, width=20, font=('Arial', 14))
    e3 = gui.Entry(reg_win, width=20, font=('Arial', 14), show='*')

    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)

    # Function to register user
    def save_user():
        name = e1.get().strip()
        uname = e2.get().strip()
        pwd = e3.get().strip()

        if not name or not uname or not pwd:
            messagebox.showerror("Error", "All fields are required!")
            return

        c = None
        try:
            c = cn.cursor()
            c.execute(
                "INSERT INTO user_register (name, uname, pwd) VALUES (%s, %s, %s)",
                (name, uname, pwd)
            )
            cn.commit()
            messagebox.showinfo("Success", "User registered successfully!")
            e1.delete(0, gui.END)
            e2.delete(0, gui.END)
            e3.delete(0, gui.END)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"MySQL Error: {e}")
        finally:
            if c:
                c.close()

    # Buttons
    gui.Button(reg_win, text="Register", font=('Arial', 14), command=save_user).grid(row=3, column=0, padx=10, pady=10)
    gui.Button(reg_win, text="Close", font=('Arial', 14), command=reg_win.destroy).grid(row=3, column=1, padx=10, pady=10)
