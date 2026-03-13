import mysql.connector as mysql
import tkinter as gui
import tkinter.messagebox as messagebox

# Established connection with db
cn = mysql.connect(database='STUDENT',user='root',password='Shaeeb@1881',host='localhost')

# GUI Window
w = gui.Tk()
w.geometry("300x200")

def save(e1,e2,e3,e4):
    rno = e1.get()
    name= e2.get()
    s1 = int(e3.get()) # integer 
    s2 = int(e4.get()) # covert to integer

    c = cn.cursor()
    try:
        c.execute("INSERT INTO student_marks(rollno,name,sub1,sub2) VALUES(%s,%s,%s,%s)", params=(rno,name,s1,s2))

        cn.commit()
        messagebox.showinfo(title ='Info', message="Marks detailed are saved")
        e1.delete(0,gui.END)
        e2.delete(0,gui.END)
        e3.delete(0,gui.END)
        e4.delete(0,gui.END)
    except mysql.Error as e:
        messagebox.showerror(title='Error', message ='Error saving marks:{}'.format(e))

def marks_window():
    w1 = gui.Toplevel(w)
    w1.geometry("300x200")

    l1 = gui.Label(w1,text='Rollno', font=('Arial',14))
    l2 = gui.Label(w1,text='Name', font=('Arial',14))
    l3 = gui.Label(w1,text='Subject1', font=('Arial',14))
    l4 = gui.Label(w1,text='Subject2', font=('Arial',14))

    e1 = gui.Entry(w1,width=10,font=('Arial',12))
    e2 = gui.Entry(w1,width=10,font=('Arial',12))
    e3 = gui.Entry(w1,width=10,font=('Arial',12))
    e4 = gui.Entry(w1,width=10,font=('Arial',12))

    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    l3.grid(row=3,column=1)
    l4.grid(row=4,column=1)
    e1.grid(row=1,column=2)
    e2.grid(row=2,column=2)
    e3.grid(row=3,column=2)
    e4.grid(row=4,column=2)
    
    # Button
    b1 = gui.Button(w1,text = 'Save',command=lambda: save(e1,e2,e3,e4))
    b1.grid(row=5,column=1)
        
def find_window():
    w2 = gui.Toplevel(w)
    w2.geometry("300x200")
    w2.title('Find Result')

    l1 = gui.Label(w2,text='Rollno', font=('Arial',14))
    e1 = gui.Entry(w2,width=10,font=('Arial',12))

    l1.grid(row=1,column=1)
    e1.grid(row=1, column=2)
    

    def find():
        c = cn.cursor()
        c.execute('SELECT rollno,name,sub1,sub2, sub1+sub2 from student_marks WHERE rollno =%s',(e1.get(),))

        row = c.fetchone() # name,sub1,sub2
        if row == None:
            messagebox.showinfo(title='Info', message ='Invalid Rollno')
        else:
            result = 'Pass' if row[2] >= 40 and row[3] >=40 else'Fail' # row[2] =sub1,row[3]=sub2
            a = map(str,row)
            s=" ".join(a)
            s=s+' '+result

            l2 = gui.Label(w2,text=s,font=('Arial',14))
            l2.grid(row=2,column=1)
    b1 = gui.Button(w2,text='Find Result',command=find)
    b1.grid(row=3,column=1)
        
b1 = gui.Button(w,text='Marks Entry',font=('Arial',14),command=marks_window)
b2 = gui.Button(w,text='Find Result',font=('Arial',14),command=find_window)

b1.pack(fill=gui.BOTH, expand=True)
b2.pack(fill=gui.BOTH, expand =True)

w.mainloop()
cn.close()
        