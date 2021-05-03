from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk

import re
import os

window=Tk()

fr=Frame(window,bg='white')
fr.place(relx=0.18,rely=0.2,relheight=0.61,relwidth=0.65)

fr1=Frame(window,bg='darkslateblue')
fr1.place(relx=0.185,rely=0.21,relheight=0.59,relwidth=0.64)

fr2=Frame(window,bg='white')
fr2.place(relx=0.19,rely=0.22,relheight=0.57,relwidth=0.63)

def validateAllFields():
    messagebox.showinfo('Information', 'Click on home to go back')

def callNewScreen():
    window.destroy()
    os.system('LoginScreen.py')

def callNewScreem():
    window.destroy()
    os.system('UpdateScreen.py')

window.title("Ticket")
window.geometry('1920x1080')
window.configure(background = "black");

v_fName = StringVar()
v_packid = StringVar()
v_payid = StringVar()
v_phoneNo = StringVar()
v_amount = StringVar()
v_dest = StringVar()

lb_heading=Label(window,text="TOUR TICKET", width=32, font=("Courier New", 30,'bold'), bg="powderblue", borderwidth=9,highlightcolor="navy")
lb_heading.place(relx=0.26,rely=0.24)

lb_fullname=Label(window,text="Full Name   : ", width=15, font=("Courier New", 20,'bold'), fg="navy", bg="white",anchor=W)
lb_fullname.place(relx=0.34,rely=0.37)
entry_fullname=Label(window, textvariable = v_fName, font=("Courier New",18,'bold'), fg="maroon", bg="white",highlightthickness=0,anchor=W)
entry_fullname.place(relx=0.54,rely=0.37)

lb_packid=Label(window,text="Package ID  : ", width=15, font=("Courier New", 20,'bold'),fg="navy", bg="white",anchor=W)
lb_packid.place(relx=0.34,rely=0.435)
entry_packid=Label(window, textvariable = v_packid,font=("Courier New", 18,'bold'),fg="maroon", bg="white",highlightthickness=0,anchor=W)
entry_packid.place(relx=0.54,rely=0.435)

lb_payid=Label(window,text="Payment ID  : ", width=15, font=("Courier New", 20,'bold'),fg="navy", bg="white",anchor=W)
lb_payid.place(relx=0.34,rely=0.5)
entry_payid=Label(window, textvariable = v_payid,font=("Courier New", 18,'bold'),fg="maroon", bg="white",highlightthickness=0,anchor=W)
entry_payid.place(relx=0.54,rely=0.5)

lb_phoneno=Label(window,text="Phone No.   : ", width=15, font=("Courier New", 20,'bold'),fg="navy", bg="white",anchor=W)
lb_phoneno.place(relx=0.34,rely=0.565)
entry_phoneno=Label(window, textvariable = v_phoneNo,font=("Courier New", 18,'bold'),fg="maroon", bg="white",highlightthickness=0,anchor=W)
entry_phoneno.place(relx=0.54,rely=0.565)

lb_amount=Label(window,text="Amount      : ", width=15, font=("Courier New", 20,'bold'),fg="navy", bg="white",anchor=W)
lb_amount.place(relx=0.34,rely=0.63)
entry_amount=Label(window, textvariable = v_amount,font=("Courier New", 18,'bold'),fg="maroon", bg="white",highlightthickness=0,anchor=W)
entry_amount.place(relx=0.54,rely=0.63)


lb_dest=Label(window,text="Destination : ", width=15, font=("Courier New", 20,'bold'),fg="navy", bg="white",anchor=W)
lb_dest.place(relx=0.34,rely=0.695)
entry_dest=Label(window, textvariable = v_dest,font=("Courier New", 18,'bold'),fg="maroon", bg="white",highlightthickness=0,anchor=W)
entry_dest.place(relx=0.54,rely=0.695)

btn_clear = Button(window, text="DONE", command = validateAllFields, bg="darkslateblue", fg = "white",width=20, borderwidth=9, relief="groove", font=("bold", 10)).place(relx=0.44,rely=0.85)

home_img = Image.open("home.png")
home_img = home_img.resize((20,20), Image.ANTIALIAS)
home_img = ImageTk.PhotoImage(home_img)
i1 = Label(window, image=home_img,borderwidth=0)
i1.photo =home_img
i1.pack()
i1.place(relx =0.86, rely = 0.072)
hom_img = Image.open("1.png")
hom_img = hom_img.resize((130,130), Image.ANTIALIAS)
hom_img = ImageTk.PhotoImage(hom_img)
i1 = Label(window, image=hom_img,borderwidth=0)
i1.photo =hom_img
i1.pack()
i1.place(relx =0.71, rely = 0.35)
glo_img = Image.open("glo2.png")
glo_img = glo_img.resize((60,55), Image.ANTIALIAS)
glo_img = ImageTk.PhotoImage(glo_img)
i = Label(window, image=glo_img,borderwidth=0)
i.photo =glo_img
i.pack()
i.place(relx =0.009, rely = 0.055)

txt1 = Label(window,text = "Travel Geeks",bg="black",fg='khaki',font=("Broadway",28,"bold"))
txt1.place(relx =0.06, rely = 0.06)

btn1 = tk.Radiobutton(window,text = "Home",padx=5,selectcolor='gray25',indicator=0,value=1,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn1.place(relx =0.88, rely = 0.065)

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
for b in [btn1]:
    b.bind("<Enter>", enter)
    b.bind("<Leave>", leave)

window.mainloop()
