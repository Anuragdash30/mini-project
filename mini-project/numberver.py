from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import re
import os
window=Tk()

window.title("Mobile Verification ")

window.geometry('1920x1080')
window.configure(background= "black");

v_fmno = StringVar()


lb_heading=Label(window, text='Mobile Validation screen', width=30, font=("HELVETICA", 30), bg="orange", borderwidth=9, relief="groove",highlightcolor="white")
lb_heading.place(x=400,y=163)

lb_fullname=Label(window,text="Enter Mobile number to continue", width=25, font=("Arial BLACK", 15), bg="black",fg="white")
lb_fullname.place(x=450,y=300)
entry_fullname=Entry(window, textvariable = v_fmno,font=("Arial Black",12))
entry_fullname.place(x=860,y=305)
def validateUserr(user_fno):
    global ii
    global pp
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    query="select name,phone from cust"
    cursor.execute(query)
    for(namme,no) in cursor:
        ii=namme
        pp=no
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

btn_login = Button(window, text="CONFIRM", command=validate, bg="dark blue", fg="white", width=20,borderwidth=9,relief="groove",font=("bold",10)).place(x=450, y=410)
btn_clear = Button(window, text="CLEAR", command=clearAllFields, bg="dark blue", fg="white", width=20,borderwidth=9,relief="groove",font=("bold",10)).place(x=650, y=410)
btn_newuser = Button(window, text="Exit", command=callNewScreen, bg="dark blue", fg="white",width=20,borderwidth=9,relief="groove", font=("bold",10)).place(x=850, y=410)

window.mainloop()
