import mysql.connector as mysql
import tkinter as gui
import tkinter.messagebox as messagebox

# Connect to MYSQL database
cn = mysql.connect(database='STUDENT',user='root',password='Shaeeb@1881',host='localhost')
print(cn)


# GUI window
w = gui.Tk()
w.geometry("300x200")
w.title('Login')

# creating labels

l1 = gui.Label(w, text = 'Username',font=('Arial',14))
l2 = gui.Label(w, text = 'Password',font=('Arial',14))

e1 = gui.Entry(w,width=20,font=('Arial',14))
e2 = gui.Entry(w,width=20,font=('Arial',14))

# login method

def login():
    try:
        
        user=e1.get().strip()
        pwd = e2.get().strip()

        if not user or not pwd:
            messagebox.showerror(title='Error', message='Please enter both Username and Password')
            return

        c = cn.cursor()
        
        c.execute("select*from user_register where uname = %s and pwd =%s",(user,pwd))
        row = c.fetchone()

        if row==None:
            messagebox.showinfo(title='info',message='Invalid Username or password')
        else:
            messagebox.showinfo(title='Welcome',message='Welcom to Application')
    except mysql.Error as e:
        messagebox.showinfo(title='Error',message=f'MySQL Error: {e}')
    finally:
        if c:
            c.close()

def close():
    w.destroy()

b1 = gui.Button(w, text ='Login',font=('Arial',14), command = login)
b2 = gui.Button(w, text ='Exit',width=10,font=('Arial',14), command = close)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)

e1.grid(row=1,column=2)
e2.grid(row=2,column=2)

b1.grid(row=3,column=1)
b2.grid(row=3,column=2)

w.mainloop()

