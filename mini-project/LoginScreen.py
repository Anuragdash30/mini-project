from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
from PIL import Image, ImageTk
import tkinter as tk

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
            messagebox.showinfo('Information', 'SUCCESS PLEASE ENTER MOBILE NUMEBER TO CONTINUE')
            window.destroy()
            os.system('homescreen.py')           

        else:
            messagebox.showinfo('Information', 'Invalid CREDENTIALS')
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

def callNewScreen():
    window.destroy()

    os.system('RegistrationScreen1.py')

window.title("User Login Screen")

window.geometry('1920x1080')
window.configure(background= "black");

v_fName = StringVar()
v_pwd = StringVar()

lb_heading=Label(window, text='Login Screen', width=30, font=("HELVETICA", 30), bg="orange", borderwidth=9, relief="groove",highlightcolor="white")
lb_heading.place(x=450,y=163)

lb_fullname=Label(window,text="FullName", width=15, font=("Arial BLACK", 15), bg="black",fg="white")
lb_fullname.place(x=530,y=280)
entry_fullname=Entry(window, textvariable = v_fName,font=("Arial Black",15))
entry_fullname.place(x=770,y=280)

lb_pwd=Label(window,text="Password",width=15, font=("Arial BLACK", 15), bg="black",fg="white")
lb_pwd.place(x=530,y=330)
entry_pwd=Entry(window,show="*", textvariable = v_pwd,font=("Arial Black",15))
entry_pwd.place(x=770,y=330)

btn_login = Button(window, text="LOGIN", command=validateAllFields, bg="dark blue", fg="white", width=20,borderwidth=9,relief="groove",font=("bold",10)).place(x=530, y=430)
btn_clear = Button(window, text="CLEAR", command=clearAllFields, bg="dark blue", fg="white",width=20,borderwidth=9,relief="groove", font=("bold",10)).place(x=730, y=430)
btn_newuser = Button(window, text="NEW USER?", command=callNewScreen, bg="dark blue", fg="white", width=20,borderwidth=9,relief="groove",font=("bold",10)).place(x=930, y=430)

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

btn4 = tk.Radiobutton(window,text = "Login",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=4,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn4.place(relx =0.8, rely = 0.065)

btn5 = tk.Radiobutton(window,text = "Register",command=callNewScreen,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=5,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn5.place(relx =0.88, rely = 0.065)


window.mainloop()
