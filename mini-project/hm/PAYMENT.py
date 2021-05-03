from tkinter import *  
from tkinter import messagebox
import mysql.connector as mysql
from PIL import Image, ImageTk
import tkinter as tk

import re
import os




def validateAllFields():
    if v_cName.get() == "":
        messagebox.showinfo('Information', 'Please enter the card name to proceed')
    elif v_cvv.get() == "":
        messagebox.showinfo('Information', 'Please enter cvv to proceed')
    elif v_cardNo.get() == "":
        messagebox.showinfo('Information', 'Please enter card number to proceed')
    elif len(v_cardNo.get()) != 16:
        messagebox.showinfo('Information', 'Please enter 16 digit card number to proceed')
    elif v_valid.get() == "" :
        messagebox.showinfo('Information', 'Please enter expiry to proceed')
    elif v_amount.get() == "":
        messagebox.showinfo('Information', 'Please enter the amount to proceed')
    elif v_date.get() == "":
        messagebox.showinfo('Information', 'Please enter start date to proceed')
    else:
        amount1=v_amount.get();
        date1=v_date.get();
        name1=v_cName.get()
        cardNo1=v_cardNo.get();
        valid1=v_valid.get();
        cvv1=v_cvv.get();
        cc="10"
        

        con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
        cursor = con.cursor()
        cursor.execute("insert into pay values('"+cc+"','"+ amount1 +"','"+ date1 +"','"+ name1 +"','"+ cardNo1 + "','" + valid1 + "','"+ cvv1+"')")
        cursor.execute("commit");

        messagebox.showinfo('Information', 'Payment Successful!')
        con.close();

   


def callNewScreen():
    window.destroy()
    os.system('LoginScreen.py')

window=Tk()

window.title("PAYMENT")

window.geometry('1920x1080')
window.configure(background = "black");

v_cName = StringVar()
v_cvv = StringVar()
v_cardNo = StringVar()
v_valid = StringVar()
v_amount = StringVar()
v_date = StringVar()


lb_heading=Label(window,text="PAY HERE ", width=30, font=("HELVETICA", 30), bg="orange", borderwidth=9, relief="groove",highlightcolor="white")
lb_heading.place(x=400,y=132)

lb_amount=Label(window,text="AMOUNT*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_amount.place(x=480,y=340)
entry_amount=Entry(window, textvariable = v_amount,width=20,font=("Arial BLACK",15))
entry_amount.place(x=700,y=340)
entry_amount.delete(0,END)

lb_date=Label(window,text="Start Date*",  width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_date.place(x=480,y=390)
entry_date=Entry(window, textvariable = v_date,width=20,font=("Arial BLACK",15))
entry_date.place(x=700,y=390)
entry_date.delete(0,END)

lb_cardname=Label(window,text="CARD Name*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_cardname.place(x=480,y=440)
entry_cardname=Entry(window, textvariable = v_cName ,width=20,font=("Arial BLACK",15))
entry_cardname.place(x=700,y=440)

lb_cardno=Label(window,text="Card No.*",width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_cardno.place(x=480,y=490)
entry_cardno=Entry(window, textvariable = v_cardNo,font=("Arial BLACK",15))
entry_cardno.place(x=700,y=490)
entry_cardno.delete(0,END)

lb_valid=Label(window,text="VALID UNTIL*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_valid.place(x=480,y=540)
entry_valid=Entry(window, textvariable = v_valid,font=("Arial BLACK",15))
entry_valid.place(x=700,y=540)


lb_cvv=Label(window,text="CVV*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
lb_cvv.place(x=480,y=590)
entry_cvv=Entry(window, show="*", textvariable = v_cvv, font=("Arial BLACK",15))
entry_cvv.place(x=700,y=590)
entry_cvv.delete(0,END)






btn_logout = Button(window, text="LOGOUT", bg="dark blue", fg = "white", width=10,borderwidth=9,relief="groove", font=("bold", 10)).place(x=1425,y=1)


btn_pay = Button(window, text="PAY", command = validateAllFields, bg="dark blue", fg = "white", width=30,borderwidth=9,relief="groove", font=("bold", 10)).place(x=620,y=680)

pay_img = Image.open("p1.png")
pay_img = pay_img.resize((400,80), Image.ANTIALIAS)
pay_img = ImageTk.PhotoImage(pay_img)
i = Label(window, image=pay_img,borderwidth=0)
i.photo =pay_img
i.place(relx=0.325,rely=0.27)


txt1 = Label(window,text = "Travel Geeks",bg="black",fg='khaki',font=("Broadway",28,"bold"))
txt1.place(relx =0.06, rely = 0.06)

hellov = IntVar()

window.mainloop()


    

         
    
            
