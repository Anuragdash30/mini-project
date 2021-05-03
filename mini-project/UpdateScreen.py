from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk

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
    clearAllFields()
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

def newhome():
    window.destroy()
    os.system('homepage.py') 

def newgal():
    window.destroy()
    os.system('home.py') 

def newabout():
    window.destroy()
    os.system('about.py') 
def clearAllFields():
    v_fName.set("")
    v_pwd.set("")
window=Tk()

window.title("UPDATE")

window.geometry('1980x1080')
window.configure(background = "black");

v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_places = StringVar()


lb_heading=Label(window,text="Updation screen", width=30, font=("HELVETICA", 30), bg="orange", borderwidth=9,relief="groove",highlightcolor="white")
lb_heading.place(x=400,y=163)

lb_heading=Label(window,text="(enter name and password and search your record)", width=50,bg="black", font=("HELVETICA", 20),fg="white")
lb_heading.place(x=350,y=238)

lb_fullname=Label(window,text="FullName", width=15, font=("Arial BLACK", 15), bg="black",fg="white")
lb_fullname.place(x=480,y=310)
entry_fullname=Entry(window, textvariable = v_fName,font=("Arial BLACK",15))
entry_fullname.place(x=770,y=310)

lb_pwd=Label(window,text="Password", width=15, font=("Arial BLACK", 15), bg="black",fg="white")
lb_pwd.place(x=480,y=360)
entry_pwd=Entry(window, show="*", textvariable = v_pwd,font=("Arial BLACK",15))
entry_pwd.place(x=770,y=360)

lb_phoneno=Label(window,text="Phone No.", width=15, font=("Arial BLACK", 15), bg="black",fg="white")
lb_phoneno.place(x=480,y=410)
entry_phoneno=Entry(window, textvariable = v_phoneNo,font=("Arial BLACK",15))
entry_phoneno.place(x=770,y=410)

valid_phoneno = window.register(validate_phoneno)

entry_phoneno.config(validate="key", validatecommand=(valid_phoneno, '%P'))

lb_email=Label(window,text="Email ID", width=15, font=("Arial BLACK", 15), bg="black",fg="white")
lb_email.place(x=480,y=460)
entry_email=Entry(window, textvariable = v_emailId,font=("Arial BLACK",15))
entry_email.place(x=770,y=460)


btn_register = Button(window, text="REGISTER", command = callNewScreem, bg="dark blue", fg = "white",width=20,borderwidth=9,relief="groove", font=("bold", 10)).place(x=480,y=550)
btn_clear = Button(window, text="UPDATE", command = updateme, bg="dark blue", fg = "white",width=20,borderwidth=9,relief="groove", font=("bold", 10)).place(x=680,y=550)
btn_existinguser = Button(window, text="Search User", command = Search, bg="dark blue", fg = "white",width=20,borderwidth=9,relief="groove", font=("bold", 10)).place(x=880,y=550)

home_img = Image.open("home.png")
home_img = home_img.resize((20,20), Image.ANTIALIAS)
home_img = ImageTk.PhotoImage(home_img)
i1 = Label(window, image=home_img,borderwidth=0)
i1.photo =home_img
i1.pack()
i1.place(relx =0.46, rely = 0.07)

inf_img = Image.open("info.png")
inf_img = inf_img.resize((20,20), Image.ANTIALIAS)
inf_img = ImageTk.PhotoImage(inf_img)
i2 = Label(window, image=inf_img,borderwidth=0)
i2.photo =inf_img
i2.pack()
i2.place(relx =0.55, rely = 0.07)

gal_img = Image.open("gallery.png")
gal_img = gal_img.resize((20,20), Image.ANTIALIAS)
gal_img = ImageTk.PhotoImage(gal_img)
i3 = Label(window, image=gal_img,borderwidth=0)
i3.photo =gal_img
i3.pack()
i3.place(relx =0.67, rely = 0.07)

log_img = Image.open("login.png")
log_img = log_img.resize((20,20), Image.ANTIALIAS)
log_img = ImageTk.PhotoImage(log_img)
i4 = Label(window, image=log_img,borderwidth=0)
i4.photo =log_img
i4.pack()
i4.place(relx =0.78, rely = 0.07)

reg_img = Image.open("reg.png")
reg_img = reg_img.resize((20,20), Image.ANTIALIAS)
reg_img = ImageTk.PhotoImage(reg_img)
i5 = Label(window, image=reg_img,borderwidth=0)
i5.photo =reg_img
i5.pack()
i5.place(relx =0.86, rely = 0.072)

glo_img = Image.open("glo2.png")
glo_img = glo_img.resize((60,55), Image.ANTIALIAS)
glo_img = ImageTk.PhotoImage(glo_img)
i = Label(window, image=glo_img,borderwidth=0)
i.photo =glo_img
i.pack()
i.place(relx =0.009, rely = 0.055)

txt1 = Label(window,text = "Travel Geeks",bg="black",fg='khaki',font=("Broadway",28,"bold"))
txt1.place(relx =0.06, rely = 0.06)

hellov = IntVar()

btn1 = tk.Radiobutton(window,text = "Home",command=newhome,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=1,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn1.place(relx =0.48, rely = 0.065)

btn2 = tk.Radiobutton(window,text = "About Us",command=newabout,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=2,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn2.place(relx =0.57, rely = 0.065)

btn3 = tk.Radiobutton(window,text = "Gallery",command=newgal,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=3,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn3.place(relx =0.7, rely = 0.065)

btn4 = tk.Radiobutton(window,text = "Login",command=callNewScreen,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=4,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn4.place(relx =0.8, rely = 0.065)

btn5 = tk.Radiobutton(window,text = "Register",command=callNewScreem,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=5,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn5.place(relx =0.88, rely = 0.065)
window.mainloop()
