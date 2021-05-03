from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import re
import os
window=Tk()

window.title("Mobile Verification ")

window.geometry('1920x1080')
window.configure(background= "light blue");

v_fmno = StringVar()


lb_heading=Label(window, text='Mobile Validation screen',width=20, font=("bold",20), bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="Enter Mobile number to continue", width=20, font=("bold",10), bg="light blue")
lb_fullname.place(x=80,y=130)
entry_fullname=Entry(window, textvariable = v_fmno)
entry_fullname.place(x=240,y=130)
def validateUserr(user_fno):
    global ii
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    query="select name,phone from cust"
    cursor.execute(query)
    for(namme,no) in cursor:
        ii=namme
        if user_fno==no:
            return True
            break
    return False

def validate():
    if v_fmno.get() == "":
        messagebox.showinfo('Information', 'Please Enter registered mobile number to proceed')
    
    else:
        status = validateUserr(v_fmno.get())
        if(status):
            messagebox.showinfo('Information', 'LOGIN SUCCESSFUL')
            window.destroy()      

        else:
            messagebox.showinfo('Information', 'Invalid CREDENTIALS')

def clearAllFields():
    v_fmno.set("")
 
def callNewScreen():
    window.destroy()

    os.system('homepage.py')   

btn_login = Button(window, text="CONFIRM", command=validate, bg="dark blue", fg="white", font=("bold",10)).place(x=120, y=210)
btn_clear = Button(window, text="CLEAR", command=clearAllFields, bg="dark blue", fg="white", font=("bold",10)).place(x=200, y=210)
btn_newuser = Button(window, text="Exit", command=callNewScreen, bg="dark blue", fg="white", font=("bold",10)).place(x=280, y=210)

window.mainloop()
