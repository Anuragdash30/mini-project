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


def Search():

    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    id = v_pwd.get();
    cursor.execute("SELECT * FROM cust WHERE passw = " + id)
    records = cursor.fetchall()

    for record in records:
        entry_fullname.insert(0,record[0])
        entry_pwd.insert(0,record[1])
        entry_phoneno.insert(0,record[2])
        entry_email.insert(0,record[3])

def updateme():
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    name=v_fName.get()
    passw=v_pwd.get();
    phone=v_phoneNo.get();
    email=v_emailId.get();
    cursor.execute("update cust set name='"+ name +"',passw='"+ passw +"',phone='"+phone+"',email='"+ email +"' where passw ='"+ passw +"'")
    cursor.execute("commit");
    messagebox.showinfo('Information', 'User Updated successfully!')
    con.close();  


    name=v_fName.get()
    passw=v_pwd.get();
    phone=v_phoneNo.get();
    email=v_emailId.get();

    


def callNewScreen():
    window.destroy()
    os.system('LoginScreen.py')

def callNewScreem():
    window.destroy()
    os.system('RegistrationScreen1.py')

window=Tk()

window.title("UPDATE")

window.geometry('1980x1080')
window.configure(background = "light blue");

v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_places = StringVar()


lb_heading=Label(window,text="Updation screen(enter name and password and search your record)", width=0, font=("bold", 10), bg="light blue")
lb_heading.place(x=50,y=53)

lb_fullname=Label(window,text="FullName", width=20, font=("bold", 10), bg="light blue")
lb_fullname.place(x=80,y=130)
entry_fullname=Entry(window, textvariable = v_fName)
entry_fullname.place(x=240,y=130)

lb_pwd=Label(window,text="Password", width=20, font=("bold", 10), bg="light blue")
lb_pwd.place(x=80,y=170)
entry_pwd=Entry(window, show="*", textvariable = v_pwd)
entry_pwd.place(x=240,y=170)

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


btn_register = Button(window, text="REGISTER", command = callNewScreem, bg="dark blue", fg = "white", font=("bold", 10)).place(x=150,y=450)
btn_clear = Button(window, text="UPDATE", command = updateme, bg="dark blue", fg = "white", font=("bold", 10)).place(x=250,y=450)
btn_existinguser = Button(window, text="Search User", command = Search, bg="dark blue", fg = "white", font=("bold", 10)).place(x=330,y=450)

window.mainloop()


    

         
    
            
