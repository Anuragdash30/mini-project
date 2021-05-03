from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import re
import os

window=Tk()

def validateUser(user_fName, user_Pwd):
    
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    query="select name,passw from cust"
    cursor.execute(query)
    for(namme,pas) in cursor:
        if user_fName==namme and user_Pwd==pas:
            return True
            break
    
    return False
   

def validateAllFields():
    if v_fName.get() == "":
        messagebox.showinfo('Information', 'Please Enter FullName to proceed')
    elif v_pwd.get() == "":
        messagebox.showinfo('Information', 'Please Enter Password to proceed')
    else:
        status = validateUser(v_fName.get(), v_pwd.get())
        if(status):
            messagebox.showinfo('Information', 'LOGIN SUCCESSFUL')
            window.destroy()
            os.system('homescreen.py')           

        else:
            messagebox.showinfo('Information', 'Invalid CREDENTIALS')


def clearAllFields():
    v_fName.set("")
    v_pwd.set("")

def callNewScreen():
    window.destroy()

    os.system('RegistrationScreen1.py')

window.title("User Login Screen")

window.geometry('1920x1080')
window.configure(background= "light blue");

v_fName = StringVar()
v_pwd = StringVar()

lb_heading=Label(window, text='Login Screen',width=20, font=("bold",20), bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="FullName", width=20, font=("bold",10), bg="light blue")
lb_fullname.place(x=80,y=130)
entry_fullname=Entry(window, textvariable = v_fName)
entry_fullname.place(x=240,y=130)

lb_pwd=Label(window,text="Password", width=20, font=("bold",10), bg="light blue")
lb_pwd.place(x=80,y=170)
entry_pwd=Entry(window, show="*", textvariable = v_pwd)
entry_pwd.place(x=240,y=170)

btn_login = Button(window, text="LOGIN", command=validateAllFields, bg="dark blue", fg="white", font=("bold",10)).place(x=120, y=210)
btn_clear = Button(window, text="CLEAR", command=clearAllFields, bg="dark blue", fg="white", font=("bold",10)).place(x=200, y=210)
btn_newuser = Button(window, text="NEW USER?", command=callNewScreen, bg="dark blue", fg="white", font=("bold",10)).place(x=280, y=210)


window.mainloop()

