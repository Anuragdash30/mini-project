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



window.title("Registration")
window.geometry('1920x1080')
window.configure(background = "black");

v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_places = StringVar()




lb_heading=Label(window,text="Registration Screen", width=30, font=("HELVETICA", 30), bg="orange", borderwidth=9, relief="groove",highlightcolor="white")
lb_heading.place(x=400,y=163)

lb_fullname=Label(window,text="FullName", width=15, font=("Arial BLACK", 15), bg="black",fg="white")
lb_fullname.place(x=480,y=280)
entry_fullname=Entry(window, textvariable = v_fName, font=("Arial Black", 15))
entry_fullname.place(x=700,y=280)

lb_pwd=Label(window,text="Password", width=15, font=("Arial Black", 15), fg="white", bg="black")
lb_pwd.place(x=480,y=330)
entry_pwd=Entry(window, show="*", textvariable = v_pwd,font=("Arial Black", 15))
entry_pwd.place(x=700,y=330)

lb_confirm_pwd=Label(window,text="Confirm Password", width=15, font=("Arial Black", 15), fg="white", bg="black")
lb_confirm_pwd.place(x=440,y=380)
entry_confirm_pwd=Entry(window, show="*", textvariable = v_confirmPwd,font=("Arial Black", 15))
entry_confirm_pwd.place(x=700,y=380)

lb_phoneno=Label(window,text="Phone No.", width=15, font=("Arial Black", 15), fg="white",bg="black")
lb_phoneno.place(x=480,y=430)
entry_phoneno=Entry(window, textvariable = v_phoneNo,font=("Arial Black", 15))
entry_phoneno.place(x=700,y=430)

valid_phoneno = window.register(validate_phoneno)

entry_phoneno.config(validate="key", validatecommand=(valid_phoneno, '%P'))

lb_email=Label(window,text="Email ID", width=15, font=("Arial Black", 15), fg="white", bg="black")
lb_email.place(x=480,y=480)
entry_email=Entry(window, textvariable = v_emailId,font=("Arial Black", 15))
entry_email.place(x=700,y=480)


btn_register = Button(window, text="REGISTER", command = validateAllFields, bg="dark blue", fg = "white",width=20, borderwidth=9, relief="groove", font=("bold", 10)).place(x=480,y=590)
btn_clear = Button(window, text="MODIFY", command = callNewScreem, bg="dark blue", fg = "white",width=20, borderwidth=9, relief="groove", font=("bold", 10)).place(x=680,y=590)
btn_existinguser = Button(window, text="EXISTING USER?", command = callNewScreen, bg="dark blue",width=20, borderwidth=9, relief="groove", fg = "white", font=("bold", 10)).place(x=880,y=590)

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

btn5 = tk.Radiobutton(window,text = "Register",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=5,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn5.place(relx =0.88, rely = 0.065)

window.mainloop()


scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
Package_table=ttk.Treeview(Table_Frame,columns=("Package ID","Place Name","No of Days","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=Package_table.xview)
scroll_y.config(command=Package_table.yview)
Package_table.heading("Package ID",text="Package ID")
Package_table.heading("Place Name",text="Place Name")
Package_table.heading("No of Days",text="No of days")
Package_table.heading("price",text="Price")
Package_table['show']='headings'
Package_table.pack()
