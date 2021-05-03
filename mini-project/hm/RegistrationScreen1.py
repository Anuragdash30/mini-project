from tkinter import *  
import mysql.connector as mysql
from tkinter import messagebox

import re
import os


def validate_phoneno(user_phoneno):
    if user_phoneno.isdigit():
        return True
    elif user_phoneno == "":
        return True
    else:
        messagebox.showinfo('Information','enter only digits')
        return False


def isValidEmail(user_email):
    if len(user_email) > 7:
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$",user_email) !=None:
            return True
        return False
    else:
        messagebox.showinfo('Information','invalid email id')
        return False


def validateAllFields():
    if v_fName.get() == "":
        messagebox.showinfo('Information', 'Please enter the full name to proceed')
    elif v_pwd.get() == "":
        messagebox.showinfo('Information', 'Please enter password to proceed')
    elif v_confirmPwd.get() == "":
        messagebox.showinfo('Information', 'Please confirm password to proceed')
    elif v_phoneNo.get() == "":
        messagebox.showinfo('Information', 'Please enter phone number to proceed')
    elif len(v_phoneNo.get()) != 10:
        messagebox.showinfo('Information', 'Please enter 10 digit phone number to proceed')
    elif v_emailId.get() == "":
        messagebox.showinfo('Information', 'Please enter email id to proceed')
   
    elif v_pwd.get() != v_confirmPwd.get():
        messagebox.showinfo('Information', 'Password not matched')
    else:
        name=v_fName.get()
        passw=v_pwd.get();
        phone=v_phoneNo.get();
        email=v_emailId.get();

        con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
        cursor = con.cursor()
        cursor.execute("insert into cust values('"+ name +"','"+ passw +"','"+ phone +"','"+ email +"')")
        cursor.execute("commit");

        messagebox.showinfo('Information', 'User registered Successfully!')
        con.close();



def callNewScreen():
    window.destroy()
    os.system('LoginScreen.py')

def callNewScreem():
    window.destroy()
    os.system('UpdateScreen.py')

window=Tk()

window.title("Registration")

window.geometry('1920x1080')
window.configure(background = "light blue");

v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_places = StringVar()

lb_heading=Label(window,text="Registration Screen", width=20, font=("bold", 20), bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="FullName", width=20, font=("bold", 10), bg="light blue")
lb_fullname.place(x=80,y=130)
entry_fullname=Entry(window, textvariable = v_fName)
entry_fullname.place(x=240,y=130)

lb_pwd=Label(window,text="Password", width=20, font=("bold", 10), bg="light blue")
lb_pwd.place(x=80,y=170)
entry_pwd=Entry(window, show="*", textvariable = v_pwd)
entry_pwd.place(x=240,y=170)

lb_confirm_pwd=Label(window,text="Confirm Password", width=20, font=("bold", 10), bg="light blue")
lb_confirm_pwd.place(x=80,y=210)
entry_confirm_pwd=Entry(window, show="*", textvariable = v_confirmPwd)
entry_confirm_pwd.place(x=240,y=210)

lb_phoneno=Label(window,text="Phone No.", width=20, font=("bold", 10), bg="light blue")
lb_phoneno.place(x=80,y=250)
entry_phoneno=Entry(window, textvariable = v_phoneNo)
entry_phoneno.place(x=240,y=250)

valid_phoneno = window.register(validate_phoneno)

entry_phoneno.config(validate="key", validatecommand=(valid_phoneno, '%P'))

lb_email=Label(window,text="Email ID", width=20, font=("bold", 10), bg="light blue")
lb_email.place(x=80,y=290)
entry_email=Entry(window, textvariable = v_emailId)
entry_email.place(x=240,y=290)


btn_register = Button(window, text="REGISTER", command = validateAllFields, bg="dark blue", fg = "white", font=("bold", 10)).place(x=150,y=450)
btn_clear = Button(window, text="MODIFY", command = callNewScreem, bg="dark blue", fg = "white", font=("bold", 10)).place(x=250,y=450)
btn_existinguser = Button(window, text="EXISTING USER?", command = callNewScreen, bg="dark blue", fg = "white", font=("bold", 10)).place(x=330,y=450)

window.mainloop()

 

         
    
            
