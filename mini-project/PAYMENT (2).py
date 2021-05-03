from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import tkinter as tk

import re
import os

def validate_cardno(user_cardno):
    if user_cardno.isdigit():
        return True
    elif user_cardno == "":
        return True
    else:
        messagebox.showinfo('Information','enter only digits')
        return False

def validate_cvv(user_cvv):
    if user_cvv.isdigit():
        return True
    elif user_cvv == "":
        return True
    else:
        messagebox.showinfo('Information','enter only digits')
        return False

def validate_amount(user_amount):
    if user_amount.isdigit():
        return True
    elif user_amount == "":
        return True
    else:
        messagebox.showinfo('Information','enter only digits')
        return False

def validateAllFields():
    if v_cName.get() == "":
        messagebox.showinfo('Information', 'Please enter the card name to proceed')
    elif v_cvv.get() == "":
        messagebox.showinfo('Information', 'Please enter cvv to proceed')
    elif v_cardNo.get() == "":
        messagebox.showinfo('Information', 'Please enter phone number to proceed')
    elif len(v_cardNo.get()) != 16:
        messagebox.showinfo('Information', 'Please enter 16 digit card number to proceed')
    elif v_valmonth.get() == "" or v_valmonth.get() == "Select month":
        messagebox.showinfo('Information', 'Please enter month of expiry to proceed')
    elif v_valyear.get() == "" or v_valyear.get() == "Select year":
        messagebox.showinfo('Information', 'Please enter year of expiry to proceed')
    elif v_amount.get() == "":
        messagebox.showinfo('Information', 'Please enter the amount to proceed')
    elif v_date.get() == "":
        messagebox.showinfo('Information', 'Please enter start date to proceed')




def callNewScreen():
    window.destroy()
    os.system('LoginScreen.py')

window=Tk()

window.title("Payment")

window.geometry('1920x1080')
window.configure(background = "black");

v_cName = StringVar()
v_cvv = IntVar()
v_cardNo = IntVar()
v_valmonth = StringVar()
v_valyear = StringVar()
v_amount = IntVar()
v_date = IntVar()


lb_heading=Label(window,text="PAY HERE ", width=25, font=("HELVETICA", 25), bg="darkorange", borderwidth=9, relief="groove",highlightcolor="white")
lb_heading.place(relx=0.29,rely=0.165)

lb_amount=Label(window,text="AMOUNT*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_amount.place(relx=0.28,rely=0.42)
entry_amount=Entry(window, textvariable = v_amount,width=20,font=("Arial BLACK",15))
entry_amount.place(relx=0.47,rely=0.42)

lb_date=Label(window,text="Start Date*",  width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_date.place(relx=0.28,rely=0.48)
entry_date=Entry(window, textvariable = v_date,width=20,font=("Arial BLACK",15))
entry_date.place(relx=0.47,rely=0.48)

lb_cardname=Label(window,text="CARD Name*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_cardname.place(relx=0.28,rely=0.54)
entry_cardname=Entry(window, textvariable = v_cName ,width=20,font=("Arial BLACK",15))
entry_cardname.place(relx=0.47,rely=0.54)

lb_cardno=Label(window,text="Card No.*",width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_cardno.place(relx=0.28,rely=0.6)
entry_cardno=Entry(window, textvariable = v_cardNo,font=("Arial BLACK",15))
entry_cardno.place(relx=0.47,rely=0.6)

lb_valyear=Label(window,text="VALID UNTIL*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_valyear.place(relx=0.28,rely=0.66)
list_valyear = ['2002', '2001', '2000', '1999', '1998','1997','1996','1995','1994','1993','1992','1991','1990'];

droplist=OptionMenu(window, v_valyear, *list_valyear)
droplist.config(width=24, bg="white",font=("Arial BLACK",10))
v_valyear.set(' YEAR ')
droplist.place(relx=0.47,rely=0.66)

lb_valmonth=Label(window,text="VALID UNTIL*",width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_valmonth.place(relx=0.28,rely=0.72)
list_valmonth = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER'];

droplist=OptionMenu(window, v_valmonth, *list_valmonth)
droplist.config(width=24,  bg="white",font=("Arial BLACK",10))
v_valmonth.set(' Month ')
droplist.place(relx=0.47,rely=0.72)

lb_cvv=Label(window,text="CVV*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_cvv.place(relx=0.28,rely=0.78)
entry_cvv=Entry(window, show="*", textvariable = v_cvv, font=("Arial BLACK",15))
entry_cvv.place(relx=0.47,rely=0.78)


valid_amount = window.register(validate_amount)

entry_amount.config(validate="key", validatecommand=(valid_amount, '%P'))

valid_cvv = window.register(validate_cvv)

entry_cvv.config(validate="key", validatecommand=(valid_cvv, '%P'))


valid_cardno = window.register(validate_cardno)

entry_cardno.config(validate="key", validatecommand=(valid_cardno, '%P'))

btn_pay = Button(window, text="PAY", command = validateAllFields, bg="darkslateblue", fg = "white", width=30,borderwidth=9,relief="groove", font=("bold", 10)).place(relx=0.38,rely=0.86)

pay_img = Image.open("p1.png")
pay_img = pay_img.resize((400,80), Image.ANTIALIAS)
pay_img = ImageTk.PhotoImage(pay_img)
i = Label(window, image=pay_img,borderwidth=0)
i.photo =pay_img
i.place(relx=0.325,rely=0.27)

home_img = Image.open("home.png")
home_img = home_img.resize((20,20), Image.ANTIALIAS)
home_img = ImageTk.PhotoImage(home_img)
i1 = Label(window, image=home_img,borderwidth=0)
i1.photo =home_img
i1.pack()
i1.place(relx =0.75, rely = 0.07)

out_img = Image.open("logout.png")
out_img = out_img.resize((20,20), Image.ANTIALIAS)
out_img = ImageTk.PhotoImage(out_img)
i2 = Label(window, image=out_img,borderwidth=0)
i2.photo =out_img
i2.pack()
i2.place(relx =0.86, rely = 0.072)

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

btn4 = tk.Radiobutton(window,text = "Home",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=4,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn4.place(relx =0.77, rely = 0.065)

btn5 = tk.Radiobutton(window,text = "Logout",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=5,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn5.place(relx =0.88, rely = 0.065)

def enter(event):
    event.widget.config(
        borderwidth=3,
        highlightbackground="white",
        )
def leave(event):
    event.widget.config(
        borderwidth=0,
        highlightbackground="black",
        )   
for b in [btn4,btn5]:
    b.bind("<Enter>", enter)
    b.bind("<Leave>", leave)


window.mainloop()
