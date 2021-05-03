from tkinter import *
import webbrowser 
from tkinter import messagebox
import mysql.connector as mysql
import tkinter as tk
from PIL import Image, ImageTk
from numberver import ii,pp
import re
import os

root = Tk()
root.minsize(1200, 600)
root.title("Travel Agency")
root.configure(bg='black')
root.iconphoto(False, tk.PhotoImage(file='icon.ico'))
current = 0
image_list = ['Goa.png', 'Raj.png', 'Ker.png','Mal.png', 'Au.png', 'Nada.png']
#varibles
goaday = IntVar()
rajday= IntVar()
kerday= IntVar()
aerday= IntVar()
berday= IntVar()
cerday= IntVar()



  

def profile():
    text="nil"
    name= StringVar()
    email = StringVar()
    phone = StringVar()
    addr = StringVar()

        
    new_frame= Frame(root, bg="black")
    new_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    lab_heading=Label(new_frame, text='Your Profile', width=20, font=("HELVETICA", 30), bg="darkorange", borderwidth=9, relief="groove",highlightcolor="white")
    lab_heading.place(relx=0.23,rely=0.0)

    lab_name=Label(new_frame,text="Full Name         : ", anchor=W, font=("Arial BLACK", 15), bg="black",fg="white")
    lab_name.place(relx=0.27,rely=0.2)
    name_entry = Entry(new_frame,font=("Comic Sans MS",12),width=24)
    name_entry.place(relx=0.50,rely=0.2)
    lab_email=Label(new_frame,text="Email Address   : ",anchor=W, font=("Arial BLACK", 15), bg="black",fg="white")
    lab_email.place(relx=0.27,rely=0.35)
    email_entry = Entry(new_frame,font=("Comic Sans MS",12),width=24)
    email_entry.place(relx=0.50,rely=0.35)
    lab_no=Label(new_frame,text="Mobile Number  : ", anchor=W, font=("Arial BLACK", 15), bg="black",fg="white")
    lab_no.place(relx=0.27,rely=0.5)
    mob_entry = Entry(new_frame,font=("Comic Sans MS",12),width=24)
    mob_entry.place(relx=0.50,rely=0.5)
    lab_add=Label(new_frame,text="Bookings            : ",anchor=W, font=("Arial BLACK", 15), bg="black",fg="white")
    lab_add.place(relx=0.27,rely=0.65)
    book_entry = Entry(new_frame,font=("Comic Sans MS",12),width=10)
    book_entry.place(relx=0.50,rely=0.65)

    lab_add2=Label(new_frame,text="On :",anchor=W, font=("Arial BLACK", 15), bg="black",fg="white")
    lab_add2.place(relx=0.63,rely=0.65)
    date_entry = Entry(new_frame,font=("Comic Sans MS",12),width=11)
    date_entry.place(relx=0.69,rely=0.65)
    lab_add2=Label(new_frame,text="For:",anchor=W, font=("Arial BLACK", 15), bg="black",fg="white")
    lab_add2.place(relx=0.80,rely=0.65)
    day_entry = Entry(new_frame,font=("Comic Sans MS",12),width=5)
    day_entry.place(relx=0.86,rely=0.65)
    lab_add2=Label(new_frame,text="days",anchor=W, font=("Arial BLACK", 15), bg="black",fg="white")
    lab_add2.place(relx=0.91,rely=0.65)
    name_entry.insert(0,ii)
    name_entry.config(state = "readonly")

    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    query="select email,phone from cust"
    cursor.execute(query)
    for(ema,ph) in cursor:
        if ph==pp:
            global eeee
            eeee=ema
            break
    con.close()
    email_entry.insert(0,eeee)
    email_entry.config(state = "readonly")
    mob_entry.insert(0,pp)
    mob_entry.config(state = "readonly")
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    query="select mobile,dest,date1,days from pay"
    cursor.execute(query)
    if(cursor):
        for(mo,de,da,dat) in cursor:
            if mo==pp:
                date_entry.insert(0,da)
                date_entry.config(state = "readonly")
                book_entry.insert(0,de)
                book_entry.config(state = "readonly")
                day_entry.insert(0,dat)
                day_entry.config(state = "readonly")

                break
    else:
        date_entry.insert(0,text)
        date_entry.config(state = "readonly")
        book_entry.insert(0,text)
        book_entry.config(state = "readonly")
        day_entry.insert(0,text)
        day_entry.config(state = "readonly")
    con.close()
    g_tt = Button(new_frame,text='Cancel Booking',command=cancel,bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    g_tt.place(relx =0.82, rely = 0.86)
def cancel():
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    cursor.execute("delete from pay where mobile=%s",(pp,))
    cursor.execute("commit");
    messagebox.showinfo('Information', 'Deleted successfully')
    con.close()
def pay_frame():
    root.withdraw()
    window=Tk()
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    query="select pid,paname from Pack"
    cursor.execute(query)
    for(nna,naaam) in cursor:
        if nna==pidd:
            global desti
            desti=naaam
            break  
    con.close()
    v_pidd= StringVar()
    v_mobile= StringVar()
    v_custna=StringVar()
    v_cName = StringVar()
    v_cvv = StringVar()
    v_cardNo = StringVar()
    v_valid = StringVar()
    v_date = StringVar()
    v_amount = StringVar()
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
        
            v_mobile=pp
            mobile=v_mobile
            v_custna=ii
            custna=v_custna

            con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
            cursor = con.cursor()
            cursor.execute("insert into pay (pid,mobile,custnam,dest,days,amount1,date1,name1,cardno1,valid1,cvv1) values ('"+pidd+"','"+mobile+"','"+ custna +"','"+desti+"',%s,'"+ amount1 +"','"+ date1 +"','"+ name1 +"','"+ cardNo1 + "','" + valid1 + "','"+ cvv1+"')",(day,))
            
            cursor.execute("commit");
            

            messagebox.showinfo('Information', 'Payment Successful!')
            con.close();
    def calll():
        root.deiconify()
        home_frame()
        window.destroy()
        
    def callNewScreen():
        window.destroy()
        root.destroy()
        os.system('LoginScreen.py')   
    window.title("PAYMENT")

    window.geometry('1920x1080')
    window.configure(background = "black");

    lb_heading=Label(window,text="PAY HERE ", width=30, font=("HELVETICA", 30), bg="orange", borderwidth=9, relief="groove",highlightcolor="white")
    lb_heading.place(x=400,y=132)

    lb_amount=Label(window,text="AMOUNT*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
    lb_amount.place(x=480,y=340)
    entry_amount=Entry(window, textvariable = v_amount,width=20,font=("Arial BLACK",15))
    entry_amount.place(x=700,y=340)
    entry_amount.delete(0,END)

    lb_date=Label(window,text="Start Date(yyyy-mm-dd)*",  width=19, font=("Arial BLACK", 14), bg="black", fg="white")
    lb_date.place(x=438,y=390)
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

    lb_valid=Label(window,text="VALID UNTIL(yyyy-mm)*", width=19, font=("Arial BLACK", 14), bg="black", fg="white")
    lb_valid.place(x=420,y=540)
    entry_valid=Entry(window, textvariable = v_valid,font=("Arial BLACK",15))
    entry_valid.place(x=700,y=540)


    lb_cvv=Label(window,text="CVV*", width=15, font=("Arial BLACK", 15), bg="black", fg="white")
    lb_cvv.place(x=480,y=590)
    entry_cvv=Entry(window, show="*", textvariable = v_cvv, font=("Arial BLACK",15))
    entry_cvv.place(x=700,y=590)
    entry_cvv.delete(0,END)

    entry_amount.insert(0,cc)
    entry_amount.config(state = "readonly")


    date1=v_date.get()
    name1=v_cName.get()
    cardNo1=v_cardNo.get()
    valid1=v_valid.get()
    cvv1=v_cvv.get()
    print(cvv1)
        
    bt_logout = Button(window, text="HOME",command=calll, bg="dark blue", fg = "white", width=10,borderwidth=9,relief="groove", font=("bold", 10)).place(x=300,y=600)

    btn_logout = Button(window, text="LOGOUT",command=callNewScreen, bg="dark blue", fg = "white", width=10,borderwidth=9,relief="groove", font=("bold", 10)).place(x=1425,y=1)


    btn_pay = Button(window, text="PAY", command = validateAllFields, bg="dark blue", fg = "white", width=30,borderwidth=9,relief="groove", font=("bold", 10)).place(x=620,y=680)
    
    pay_img = Image.open("p1.png")
    pay_img = pay_img.resize((400,80), Image.ANTIALIAS)
    pay_img = ImageTk.PhotoImage(pay_img)
    i = Label(window,image=pay_img,borderwidth=0)
    i.photo = pay_img
    i.place(relx=0.326,rely=0.27)


    txt1 = Label(window,text = "Travel Geeks",bg="black",fg='khaki',font=("Broadway",28,"bold"))
    txt1.place(relx =0.06, rely = 0.06)

    hellov = IntVar()

    window.mainloop()



#Home Code
def home_frame():
    home_frame= Frame(root, bg="black")
    home_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    tr = Image.open("m5.png")
    tr = tr.resize((700,480), Image.ANTIALIAS)
    tr = ImageTk.PhotoImage(tr)
    tr1 = Label(home_frame, image=tr,borderwidth=0)
    tr1.photo =tr
    tr1.pack()
    tr1.place(relx =0.13, rely = 0.06)
    
    y=Label(home_frame, text="'Cover the earth before it covers you...'",bg="black",borderwidth=0,fg='darkkhaki',font=("Cooper Black",25))
    y.place(relx=0.15,rely=0.0)
    
#About Us Code
def ua_frame():
    ua_frame= Frame(root, bg="black")
    ua_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    ua1=Label(ua_frame,text='About Us',bg="black",borderwidth=0,fg='darkkhaki',font=("Cooper Black",26))
    ua1.place(relx=0.42,rely=0.0)

    ua2=Label(ua_frame,text='  Since 2001, Travel Geeks has been committed to bringing our clients the best in value and quality\n travel arrangements.We’ve been travelling the world for over 15 years, building a reputation\n for providing quality travel content that’s inspiring, engaging and informative. ',bg="black",borderwidth=0,fg='antiquewhite',font=("Comic Sans MS",14))
    ua2.place(relx=0.0,rely=0.27)
    
    ua4=Label(ua_frame,text='The company bagged its first major honour by receiving the PATA \n(Pacific Asia Travel Association) Award in the year 2011, also felicitated by the \nGovernment of India with the National Tourism Award in following year (2012).',bg="black",borderwidth=0,fg='antiquewhite',font=("Comic Sans MS",14))
    ua4.place(relx=0.13,rely=0.53)

    ua3=Label(ua_frame,text='Founders : ',bg="black",borderwidth=0,fg='lightgreen',font=("Comic Sans MS",15,'bold'))
    ua3.place(relx=0.0,rely=0.15)

    ua5=Label(ua_frame,text='Ms.Anushree Rege , Mr.Anurag Dash , Mr.Harmeet Singh & Ms.Sakshi Jetley.',bg="black",borderwidth=0,fg='thistle',font=("Comic Sans MS",14))
    ua5.place(relx=0.135,rely=0.155)

    ua3=Label(ua_frame,text='Call : ',bg="black",borderwidth=0,fg='lightgreen',font=("Comic Sans MS",15,'bold'))
    ua3.place(relx=0.18,rely=0.85)

    ua3=Label(ua_frame,text='Visit : ',bg="black",borderwidth=0,fg='lightgreen',font=("Comic Sans MS",15,'bold'))
    ua3.place(relx=0.57,rely=0.85)

    tr = Image.open("tro.png")
    tr = tr.resize((100,100), Image.ANTIALIAS)
    tr = ImageTk.PhotoImage(tr)
    tr1 = Label(ua_frame, image=tr,borderwidth=0)
    tr1.photo =tr
    tr1.pack()
    tr1.place(relx =0.0, rely = 0.51)

    tr = Image.open("all.png")
    tr = tr.resize((20,25), Image.ANTIALIAS)
    tr = ImageTk.PhotoImage(tr)
    tr1 = Label(ua_frame, image=tr,borderwidth=0)
    tr1.photo =tr
    tr1.pack()
    tr1.place(relx =0.15, rely = 0.86)

    tr = Image.open("int.png")
    tr = tr.resize((30,30), Image.ANTIALIAS)
    tr = ImageTk.PhotoImage(tr)
    tr1 = Label(ua_frame, image=tr,borderwidth=0)
    tr1.photo =tr
    tr1.pack()
    tr1.place(relx =0.52, rely = 0.85)

    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))
        return

    lbl = tk.Label(ua_frame, text=r"http://www.travelgeeks.com", cursor="hand2",bg="black",borderwidth=0,fg='deepskyblue',font=("Comic Sans MS",13,'underline'))
    lbl.place(relx =0.65, rely = 0.86)

    lb2 = tk.Label(ua_frame, text=r"+ (91) 98672 31451", cursor="hand2",bg="black",borderwidth=0,fg='deepskyblue',font=("Comic Sans MS",13))
    lb2.place(relx =0.25, rely = 0.86)

    lbl.bind("<Button-1>", callback)
    
#Gallery Code
def gal_frame():
    gal_frame=Frame(root,bg="black")
    gal_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)
    def move(delta):
        global current, image_list
        current += delta
        if current==0:
            a1=Button(gal_frame, text='<<',bg="black",fg='white',font=("Cooper Black",20,"bold"),borderwidth=0,state='disabled').place(relx=0.0,rely=0.4)
        elif current==5:
            a2=Button(gal_frame, text='>>',bg="black",fg='white',font=("Cooper Black",20,"bold"),borderwidth=0,state='disabled').place(relx=0.92,rely=0.4)
        else :
            a1=Button(gal_frame, text='<<',bg="black",fg='white',font=("Cooper Black",20,"bold"),borderwidth=0,state='normal',command=lambda: move(-1)).place(relx=0.0,rely=0.4)
            a2=Button(gal_frame, text='>>',bg="black",fg='white',font=("Cooper Black",20,"bold"),borderwidth=0,state='normal',command=lambda: move(+1)).place(relx=0.92,rely=0.4)
         
        image = Image.open(image_list[current])
        image = image.resize((710,450), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label['image'] = photo
        label.photo = photo
        return
    label = Label(gal_frame,borderwidth=0)
    label.place(relx=0.085,rely=0.0)

    a1=Button(gal_frame, text='<<',bg="black",fg='white',font=("Cooper Black",20,"bold"),borderwidth=0,activebackground='white',activeforeground='black', command=lambda: move(-1)).place(relx=0.0,rely=0.4)
    a2=Button(gal_frame, text='>>', bg="black",fg='white',font=("Cooper Black",20,"bold"),borderwidth=0,activebackground='white',activeforeground='black',command=lambda: move(+1)).place(relx=0.92,rely=0.4)
    move(0)
    

#Goa Code    
def goa_frame():
    
    goa_frame = Frame(root, bg="black")
    goa_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    go=Label(goa_frame,bg="black",borderwidth=0,text="\n'If you have an adventurous soul \nbut your mind wants to relax \nadmist calm surroundings,\nGoa is the place to go'",fg='khaki',font=("Comic Sans MS",16,"bold"))
    go.place(relx =0.5, rely = -0.05)

    go1=Label(goa_frame,bg="black",borderwidth=0,text="Places for Sight Seeing !!!",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    go1.place(relx =0.05, rely = 0.465)

    go2=Label(goa_frame,bg="black",borderwidth=0,text="1.Aguada Fort - History Lovers    \n\n2.Basilica of Bom Jesus - Church  \n\n3.Miramar Beach - Scenic Seaside\n\n4.Vasco Da Gama - Old City         ",fg='antiquewhite',font=("Comic Sans MS",14))
    go2.place(relx =0.01, rely = 0.55)

    go3=Label(goa_frame,bg="black",borderwidth=0,text="Package Details",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    go3.place(relx =0.6, rely = 0.465)

    go4=Label(goa_frame,bg="black",borderwidth=0,text="Hotel rent,Sight Seeing and Breakfast included.",fg='thistle',font=("Comic Sans MS",14))
    go4.place(relx =0.47, rely = 0.55)

    go5=Label(goa_frame,bg="black",borderwidth=0,text="Nights to Stay : ",fg='lightgreen',font=("Comic Sans MS",14))
    go5.place(relx =0.47, rely = 0.63)


    go7=Label(goa_frame,bg="black",borderwidth=0,text="Estimated Amount : ",fg='lightgreen',font=("Comic Sans MS",14))
    go7.place(relx =0.47, rely = 0.87)

    go8=Label(goa_frame,bg="black",borderwidth=0,text="Rs.",fg='antiquewhite',font=("Comic Sans MS",14))
    go8.place(relx =0.67, rely = 0.87)

    g_entry1 = Spinbox(goa_frame,textvariable = goaday, from_=1, to=6,font=("Comic Sans MS",12), width=3,justify=CENTER)
    g_entry1.place(relx =0.67, rely = 0.64)

    g_entry2 = Entry(goa_frame,font=("Comic Sans MS",12),width=12)
    g_entry2.place(relx =0.71, rely = 0.87)

    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    na="GOA"
    query="select pid,paname,price from Pack"
    cursor.execute(query)
    for(piddd,namme,pas) in cursor:
        if na==namme:
            global pidd
            global cc
            global day
            pidd=piddd
            day=goaday.get()
            cc=goaday.get()*pas
            g_entry2.insert(0,cc)
            g_entry2.config(state = "readonly")

            break
    con.close()
  
    
    
    
    g_tt = Button(goa_frame,text='Book Now',command=pay_frame,bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    g_tt.place(relx =0.88, rely = 0.86)
    g_t = Button(goa_frame,command=goa_framec,text='Check Price',bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    g_t.place(relx =0.75, rely = 0.62)

    g = Image.open("goa1.png")
    g = g.resize((350,200), Image.ANTIALIAS)
    g = ImageTk.PhotoImage(g)
    g1 = Label(goa_frame, image=g,borderwidth=0)
    g1.photo =g
    g1.pack()
    g1.place(relx =0.0, rely = 0.0)
def goa_framec():
    goa_frame()


#Rajasthan Code
def raj_frame():
    raj_frame = Frame(root, bg="black")
    raj_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    ra=Label(raj_frame,bg="black",borderwidth=0,text="\nPadharo Mhare Des..\n\n'The desert tells a different story \nevery time one ventures on it'",fg='khaki',font=("Comic Sans MS",16,"bold"))
    ra.place(relx =0.5, rely = -0.05)

    ra1=Label(raj_frame,bg="black",borderwidth=0,text="Places for Sight Seeing !!!",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    ra1.place(relx =0.05, rely = 0.465)

    ra2=Label(raj_frame,bg="black",borderwidth=0,text="1.Jaipur - The Pink City                   \n\n2.Ranthambore - Green Paradise      \n\n3.Mount Abu - Solitude Guaranteed! \n\n4.Jaisalmer - The Golden City          ",fg='antiquewhite',font=("Comic Sans MS",14))
    ra2.place(relx =0.01, rely = 0.55)

    ra3=Label(raj_frame,bg="black",borderwidth=0,text="Package Details",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    ra3.place(relx =0.6, rely = 0.465)

    ra4=Label(raj_frame,bg="black",borderwidth=0,text="Sight Seeing,Hotel rent and Breakfast included.",fg='thistle',font=("Comic Sans MS",14))
    ra4.place(relx =0.47, rely = 0.55)

    ra5=Label(raj_frame,bg="black",borderwidth=0,text="Nights to Stay : ",fg='lightgreen',font=("Comic Sans MS",14))
    ra5.place(relx =0.47, rely = 0.63)

    ra7=Label(raj_frame,bg="black",borderwidth=0,text="Estimated Amount : ",fg='lightgreen',font=("Comic Sans MS",14))
    ra7.place(relx =0.47, rely = 0.87)

    ra8=Label(raj_frame,bg="black",borderwidth=0,text="Rs.",fg='antiquewhite',font=("Comic Sans MS",14))
    ra8.place(relx =0.67, rely = 0.87)

    r_entry1 = Spinbox(raj_frame,textvariable=rajday, from_=1, to=100,font=("Comic Sans MS",12), width=3,justify=CENTER)
    r_entry1.place(relx =0.67, rely = 0.64)

    r_entry2 = Entry(raj_frame,font=("Comic Sans MS",12),width=12)
    r_entry2.place(relx =0.71, rely = 0.87)
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    na="RAJASTHAN"
    query="select pid,paname,price from Pack"
    cursor.execute(query)
    for(piddd,namme,pas) in cursor:
        if na==namme:
            global pidd
            global cc
            global day
            pidd=piddd
            day=rajday.get()
            cc=rajday.get()*pas
            r_entry2.insert(0,cc)
            r_entry2.config(state = "readonly")

            break
    con.close()
    r_tt = Button(raj_frame,text='Book Now',command=pay_frame,bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    r_tt.place(relx =0.88, rely = 0.86)
    r_t = Button(raj_frame,command=raj,text='Check Price',bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    r_t.place(relx =0.75, rely = 0.62)
 
    r = Image.open("raj1.png")
    r = r.resize((350,200), Image.ANTIALIAS)
    r = ImageTk.PhotoImage(r)
    r1 = Label(raj_frame, image=r,borderwidth=0)
    r1.photo =r
    r1.pack()
    r1.place(relx =0.0, rely = 0.0)
def raj():
    raj_frame()
#Kerala Code    
def ker_frame():
    ker_frame = Frame(root, bg="black")
    ker_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)
    
    ker1=Label(ker_frame,bg="black",borderwidth=0,text="\n'Known as God’s own Country.\n'Kera' means Coconut tree\n 'Alam' means land;\nThus a Land of Coconut Trees.'",fg='khaki',font=("Comic Sans MS",16,"bold"))
    ker1.place(relx =0.5, rely = -0.05)

    ker1=Label(ker_frame,bg="black",borderwidth=0,text="Places for Sight Seeing !!!",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    ker1.place(relx =0.05, rely = 0.465)

    ker2=Label(ker_frame,bg="black",borderwidth=0,text="1.Alleppey – Backwater Hot Spot         \n\n2.Kovalam – For Some Beach Fun        \n\n3.Munnar - A Perfect Hillstation         \n\n4.Thekkady – The Love Of Wildlife     ",fg='antiquewhite',font=("Comic Sans MS",14))
    ker2.place(relx =0.01, rely = 0.55)

    ker3=Label(ker_frame,bg="black",borderwidth=0,text="Package Details",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    ker3.place(relx =0.6, rely = 0.465)

    ker4=Label(ker_frame,bg="black",borderwidth=0,text="Hotel rent,Sight Seeing and Breakfast included.",fg='thistle',font=("Comic Sans MS",14))
    ker4.place(relx =0.47, rely = 0.55)

    ker5=Label(ker_frame,bg="black",borderwidth=0,text="Nights to Stay : ",fg='lightgreen',font=("Comic Sans MS",14))
    ker5.place(relx =0.47, rely = 0.63)

    ker7=Label(ker_frame,bg="black",borderwidth=0,text="Estimated Amount : ",fg='lightgreen',font=("Comic Sans MS",14))
    ker7.place(relx =0.47, rely = 0.87)

    ker8=Label(ker_frame,bg="black",borderwidth=0,text="Rs.",fg='antiquewhite',font=("Comic Sans MS",14))
    ker8.place(relx =0.67, rely = 0.87)

    k_entry1 = Spinbox(ker_frame,textvariable=kerday, from_=1, to=100,font=("Comic Sans MS",12), width=3,justify=CENTER)
    k_entry1.place(relx =0.67, rely = 0.64)

    k_entry2 = Entry(ker_frame,font=("Comic Sans MS",12),width=12)
    k_entry2.place(relx =0.71, rely = 0.87)
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    na="KERALA"
    query="select pid,paname,price from Pack"
    cursor.execute(query)
    for(piddd,namme,pas) in cursor:
        if na==namme:
            global pidd
            global cc
            global day
            pidd=piddd
            day=kerday.get()
            cc=kerday.get()*pas
            k_entry2.insert(0,cc)
            k_entry2.config(state = "readonly")

            break
    con.close()

    k_tt = Button(ker_frame,text='Book Now',command=pay_frame,bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    k_tt.place(relx =0.88, rely = 0.86)
    k_t = Button(ker_frame,command=kstar,text='Check Price',bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    k_t.place(relx =0.75, rely = 0.62)

    k = Image.open("ker3.png")
    k = k.resize((350,200), Image.ANTIALIAS)
    k = ImageTk.PhotoImage(k)
    k1 = Label(ker_frame, image=k,borderwidth=0)
    k1.photo =k
    k1.pack()
    k1.place(relx =0.0, rely = 0.0)
def kstar():
    ker_frame()
#Malaysia Code        
def mala_frame():
    mala_frame = Frame(root, bg="black")
    mala_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    mala=Label(mala_frame,bg="black",borderwidth=0,text="\n'Hospitality is not a trend here\nIt is a tradition that \nMalaysians follow without remark'",fg='khaki',font=("Comic Sans MS",16,"bold"))
    mala.place(relx =0.5, rely = -0.05)

    mala1=Label(mala_frame,bg="black",borderwidth=0,text="Places for Sight Seeing !!!",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    mala1.place(relx =0.05, rely = 0.465)

    mala2=Label(mala_frame,bg="black",borderwidth=0,text="1.Langkawi – Land Of Azure Waters   \n\n2.Mount Kinabalu – Hiker’s Paradise    \n\n3.Kuala Lumpur - Scenic Twin Towers \n\n4.Perhentian – Witness Colorful Corals",fg='antiquewhite',font=("Comic Sans MS",14))
    mala2.place(relx =0.01, rely = 0.55)

    mala3=Label(mala_frame,bg="black",borderwidth=0,text="Package Details",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    mala3.place(relx =0.6, rely = 0.465)

    mala4=Label(mala_frame,bg="black",borderwidth=0,text="Sight Seeing,Hotel rent and Breakfast included.",fg='thistle',font=("Comic Sans MS",14))
    mala4.place(relx =0.47, rely = 0.55)

    mala5=Label(mala_frame,bg="black",borderwidth=0,text="Nights to Stay : ",fg='lightgreen',font=("Comic Sans MS",14))
    mala5.place(relx =0.47, rely = 0.63)



    mala7=Label(mala_frame,bg="black",borderwidth=0,text="Estimated Amount : ",fg='lightgreen',font=("Comic Sans MS",14))
    mala7.place(relx =0.47, rely = 0.87)

    mala8=Label(mala_frame,bg="black",borderwidth=0,text="Rs.",fg='antiquewhite',font=("Comic Sans MS",14))
    mala8.place(relx =0.67, rely = 0.87)

    m_entry1 = Spinbox(mala_frame,textvariable=berday, from_=1, to=100,font=("Comic Sans MS",12), width=3,justify=CENTER)
    m_entry1.place(relx =0.67, rely = 0.64)

    m_entry2 = Entry(mala_frame,font=("Comic Sans MS",12),width=12)
    m_entry2.place(relx =0.71, rely = 0.87)
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    na="MALAYSIA"
    query="select pid,paname,price from Pack"
    cursor.execute(query)
    for(piddd,namme,pas) in cursor:
        if na==namme:
            global pidd
            global cc
            global day
            pidd=piddd
            day=berday.get()
            cc=berday.get()*pas
            m_entry2.insert(0,cc)
            m_entry2.config(state = "readonly")

            break
    con.close()
    m_tt = Button(mala_frame,text='Book Now',command=pay_frame,bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    m_tt.place(relx =0.88, rely = 0.86)
    m_t = Button(mala_frame,command=mstar,text='Check Price',bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    m_t.place(relx =0.75, rely = 0.62)
    m = Image.open("mal1.png")
    m = m.resize((350,200), Image.ANTIALIAS)
    m = ImageTk.PhotoImage(m)
    m1 = Label(mala_frame, image=m,borderwidth=0)
    m1.photo =m
    m1.pack()
    m1.place(relx =0.0, rely = 0.0)
def mstar():
    mala_frame()
#Australia Code    
def au_frame():
    au_frame = Frame(root, bg="black")
    au_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    au=Label(au_frame,bg="black",borderwidth=0,text="\n'Australia welcomes you\n in a world of natural splendor.\n The moment you enter,\nyou fall in love for it'",fg='khaki',font=("Comic Sans MS",16,"bold"))
    au.place(relx =0.5, rely = -0.05)

    au1=Label(au_frame,bg="black",borderwidth=0,text="Places for Sight Seeing !!!",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    au1.place(relx =0.05, rely = 0.465)

    au2=Label(au_frame,bg="black",borderwidth=0,text="1.Sydney - The Land of Opera House     \n\n2.Great Barrier Reef – Scuba Diving Hub\n\n3.Kakadu Wildlife – Rich Wilderness       \n\n4.Melbourne – For Shopaholics               ",fg='antiquewhite',font=("Comic Sans MS",14))
    au2.place(relx =0.01, rely = 0.55)

    au3=Label(au_frame,bg="black",borderwidth=0,text="Package Details",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    au3.place(relx =0.6, rely = 0.465)

    au4=Label(au_frame,bg="black",borderwidth=0,text="Hotel rent,Sight Seeing and Breakfast included.",fg='thistle',font=("Comic Sans MS",14))
    au4.place(relx =0.47, rely = 0.55)

    au5=Label(au_frame,bg="black",borderwidth=0,text="Nights to Stay : ",fg='lightgreen',font=("Comic Sans MS",14))
    au5.place(relx =0.47, rely = 0.63)

    au7=Label(au_frame,bg="black",borderwidth=0,text="Estimated Amount : ",fg='lightgreen',font=("Comic Sans MS",14))
    au7.place(relx =0.47, rely = 0.87)

    au8=Label(au_frame,bg="black",borderwidth=0,text="Rs.",fg='antiquewhite',font=("Comic Sans MS",14))
    au8.place(relx =0.67, rely = 0.87)

    a_entry1 = Spinbox(au_frame,textvariable=aerday, from_=1, to=100,font=("Comic Sans MS",12), width=3,justify=CENTER)
    a_entry1.place(relx =0.67, rely = 0.64)

    a_entry2 = Entry(au_frame,font=("Comic Sans MS",12),width=12)
    a_entry2.place(relx =0.71, rely = 0.87)
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    na="AUSTRALIA"
    query="select pid,paname,price from Pack"
    cursor.execute(query)
    for(piddd,namme,pas) in cursor:
        if na==namme:
            global pidd
            global cc
            global day
            pidd=piddd
            day=aerday.get()
            cc=aerday.get()*pas
            a_entry2.insert(0,cc)
            a_entry2.config(state = "readonly")

            break
    con.close()
  
    a_tt = Button(au_frame,text='Book Now',command=pay_frame,bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    a_tt.place(relx =0.88, rely = 0.86)
    a_t = Button(au_frame,command=astar,text='Check Price',bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    a_t.place(relx =0.75, rely = 0.62)


    a = Image.open("aue.png")
    a = a.resize((350,200), Image.ANTIALIAS)
    a = ImageTk.PhotoImage(a)
    a1 = Label(au_frame, image=a,borderwidth=0)
    a1.photo =a
    a1.pack()
    a1.place(relx =0.0, rely = 0.0)
def astar():
    au_frame()
#Canada Code
def nada_frame():
    nada_frame = Frame(root, bg="black")
    nada_frame.place(relx=0.26,rely=0.26,relheight=0.72,relwidth=0.72)

    nada=Label(nada_frame,bg="black",borderwidth=0,text="\n'Canada is like a Loft Apartment\nover a really great party\nIts a feeling that defines thrill\n in an amazing way '",fg='khaki',font=("Comic Sans MS",16,"bold"))
    nada.place(relx =0.5, rely = -0.05)

    nada1=Label(nada_frame,bg="black",borderwidth=0,text="Places for Sight Seeing !!!",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    nada1.place(relx =0.05, rely = 0.465)

    nada2=Label(nada_frame,bg="black",borderwidth=0,text="1.Niagara Falls - An Elegant View    \n\n2.Toronto - For A Remarkable Time\n\n3.St. John’s - An Artist’s Retreat    \n\n4.Quebec City - A Magical Delight   ",fg='antiquewhite',font=("Comic Sans MS",14))
    nada2.place(relx =0.01, rely = 0.55)

    nada3=Label(nada_frame,bg="black",borderwidth=0,text="Package Details",fg='powderblue',font=("Comic Sans MS",16,"bold"))
    nada3.place(relx =0.6, rely = 0.465)

    nada4=Label(nada_frame,bg="black",borderwidth=0,text="Sight Seeing,Hotel rent and Breakfast included.",fg='thistle',font=("Comic Sans MS",14))
    nada4.place(relx =0.47, rely = 0.55)

    nada5=Label(nada_frame,bg="black",borderwidth=0,text="Nights to Stay : ",fg='lightgreen',font=("Comic Sans MS",14))
    nada5.place(relx =0.47, rely = 0.63)

    nada7=Label(nada_frame,bg="black",borderwidth=0,text="Estimated Amount : ",fg='lightgreen',font=("Comic Sans MS",14))
    nada7.place(relx =0.47, rely = 0.87)

    nada8=Label(nada_frame,bg="black",borderwidth=0,text="Rs.",fg='antiquewhite',font=("Comic Sans MS",14))
    nada8.place(relx =0.67, rely = 0.87)

    n_entry1 = Spinbox(nada_frame,textvariable=cerday, from_=1, to=100,font=("Comic Sans MS",12), width=3,justify=CENTER)
    n_entry1.place(relx =0.67, rely = 0.64)

    n_entry2 = Entry(nada_frame,font=("Comic Sans MS",12),width=12)
    n_entry2.place(relx =0.71, rely = 0.87)
    con = mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
    cursor = con.cursor()
    na="CANADA"
    query="select pid,paname,price from Pack"
    cursor.execute(query)
    for(piddd,namme,pas) in cursor:
        if na==namme:
            global pidd
            global cc
            global day
            pidd=piddd
            day=cerday.get()
            cc=cerday.get()*pas
            n_entry2.insert(0,cc)
            n_entry2.config(state = "readonly")

            break
    con.close()
    n_tt = Button(nada_frame,text='Book Now',command=pay_frame,bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    n_tt.place(relx =0.88, rely = 0.86)
    nn_tt = Button(nada_frame,command=cstar,text='Check Price',bg="thistle",fg='black',borderwidth=2,font=("Comic Sans MS",12))
    nn_tt.place(relx =0.75, rely = 0.62)

    n = Image.open("nada1.png")
    n = n.resize((350,200), Image.ANTIALIAS)
    n = ImageTk.PhotoImage(n)
    n1 = Label(nada_frame, image=n,borderwidth=0)
    n1.photo =n
    n1.pack()
    n1.place(relx =0.0, rely = 0.0)
    
def cstar():
    nada_frame()

def rootdest():
    messagebox.showinfo('Information', 'You are successfully logged out')
    os.system('homepage.py')  
    root.destroy()
#redirects++++++++++++++++++++++++++++++++
 
#Horizontal buttons

hellov = IntVar()

btn1 = tk.Radiobutton(root,text = "Home",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=1,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=home_frame)
btn1.place(relx =0.48, rely = 0.065)

btn2 = tk.Radiobutton(root,text = "About Us",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=2,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=ua_frame)
btn2.place(relx =0.57, rely = 0.065)

btn3 = tk.Radiobutton(root,text = "Gallery",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=3,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=gal_frame)
btn3.place(relx =0.7, rely = 0.065)

btn4 = tk.Radiobutton(root,text = ii,command=profile,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=4,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn4.place(relx =0.8, rely = 0.065)

btn5 = tk.Radiobutton(root,text = "LOG OUT",command=rootdest,padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=5,bg="black",fg='white',font=("Lucida Calligraphy",12,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white')
btn5.place(relx =0.88, rely = 0.065)

#Vertical buttons
btn6 = tk.Radiobutton(root,text = "Goa",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=6,bg="black",fg='white',font=("Lucida Calligraphy",14,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=goa_frame)
btn6.place(relx =0.04, rely = 0.32)

btn7 = tk.Radiobutton(root,text = "Rajasthan",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=7,bg="black",fg='white',font=("Lucida Calligraphy",14,"bold"), borderwidth=0,activebackground='gray25',activeforeground='white',command=raj_frame)
btn7.place(relx =0.04, rely = 0.4202)

btn8 = tk.Radiobutton(root,text = "Kerala",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=8,bg="black",fg='white',font=("Lucida Calligraphy",14,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=ker_frame)
btn8.place(relx =0.04, rely = 0.5204)

btn9 = tk.Radiobutton(root,text = "Malaysia",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=9,bg="black",fg='white',font=("Lucida Calligraphy",14,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=mala_frame)
btn9.place(relx =0.04, rely = 0.6998)

btn10 = tk.Radiobutton(root,text = "Australia",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=10,bg="black",fg='white',font=("Lucida Calligraphy",14,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=au_frame)
btn10.place(relx =0.04, rely = 0.8)

btn11 = tk.Radiobutton(root,text = "Canada",padx=5,selectcolor='gray25',indicator=0,variable=hellov,value=11,bg="black",fg='white',font=("Lucida Calligraphy",14,"bold"),borderwidth=0,activebackground='gray25',activeforeground='white',command=nada_frame)
btn11.place(relx =0.04, rely = 0.9002)

hellov.set(1)

#Button Events
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
for b in [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11]:
    b.bind("<Enter>", enter)
    b.bind("<Leave>", leave)

#Horizontal labels

home_img = Image.open("home.png")
home_img = home_img.resize((20,20), Image.ANTIALIAS)
home_img = ImageTk.PhotoImage(home_img)
i1 = Label(root, image=home_img,borderwidth=0)
i1.photo =home_img
i1.pack()
i1.place(relx =0.46, rely = 0.07)

inf_img = Image.open("info.png")
inf_img = inf_img.resize((20,20), Image.ANTIALIAS)
inf_img = ImageTk.PhotoImage(inf_img)
i2 = Label(root, image=inf_img,borderwidth=0)
i2.photo =inf_img
i2.pack()
i2.place(relx =0.55, rely = 0.07)

gal_img = Image.open("gallery.png")
gal_img = gal_img.resize((20,20), Image.ANTIALIAS)
gal_img = ImageTk.PhotoImage(gal_img)
i3 = Label(root, image=gal_img,borderwidth=0)
i3.photo =gal_img
i3.pack()
i3.place(relx =0.67, rely = 0.07)

log_img = Image.open("login.png")
log_img = log_img.resize((20,20), Image.ANTIALIAS)
log_img = ImageTk.PhotoImage(log_img)
i4 = Label(root, image=log_img,borderwidth=0)
i4.photo =log_img
i4.pack()
i4.place(relx =0.78, rely = 0.07)



#Flag

ind_img = Image.open("india.png")
ind_img = ind_img.resize((40,25), Image.ANTIALIAS)
ind_img = ImageTk.PhotoImage(ind_img)
f1 = Label(root, image=ind_img,borderwidth=0)
f1.photo =ind_img
f1.pack()
f1.place(relx =0.16, rely = 0.33)

f2 = Label(root, image=ind_img,borderwidth=0)
f2.photo =ind_img
f2.pack()
f2.place(relx =0.16, rely = 0.43)

f2 = Label(root, image=ind_img,borderwidth=0)
f2.photo =ind_img
f2.pack()
f2.place(relx =0.16, rely = 0.53)

mal_img = Image.open("mala.png")
mal_img = mal_img.resize((40,25), Image.ANTIALIAS)
mal_img = ImageTk.PhotoImage(mal_img)
f1 = Label(root, image=mal_img,borderwidth=0)
f1.photo =mal_img
f1.pack()
f1.place(relx =0.16, rely = 0.71)

au_img = Image.open("auau.png")
au_img = au_img.resize((40,25), Image.ANTIALIAS)
au_img = ImageTk.PhotoImage(au_img)
f1 = Label(root, image=au_img,borderwidth=0)
f1.photo =au_img
f1.pack()
f1.place(relx =0.16, rely = 0.81)

du_img = Image.open("du.png")
du_img = du_img.resize((40,25), Image.ANTIALIAS)
du_img = ImageTk.PhotoImage(du_img)
f1 = Label(root, image=du_img,borderwidth=0)
f1.photo =du_img
f1.pack()
f1.place(relx =0.16, rely = 0.91)


#Title label
glo_img = Image.open("glo2.png")
glo_img = glo_img.resize((60,55), Image.ANTIALIAS)
glo_img = ImageTk.PhotoImage(glo_img)
i = Label(root, image=glo_img,borderwidth=0)
i.photo =glo_img
i.pack()
i.place(relx =0.009, rely = 0.055)

txt1 = Label(root,text = "Travel Geeks",bg="black",fg='khaki',font=("Broadway",28,"bold"))
txt1.place(relx =0.06, rely = 0.06)

txt2 = Label(root,text = "Domestic Packages",bg="black",fg='lightgreen',font=("Script MT Bold",22,"bold"))
txt2.place(relx =0.02, rely = 0.23)

txt3 = Label(root,text = "International Packages",bg="black",fg='lightgreen',font=("Script MT Bold",22,"bold"))
txt3.place(relx =0.02, rely = 0.62)


#Stars
s1 = Label(root,text = "*",bg="black",fg='white',font=("Arial Black",20))
s1.place(relx =0.023, rely = 0.32)

s2 = Label(root,text = "*",bg="black",fg='white',font=("Arial Black",20))
s2.place(relx =0.023, rely = 0.42)

s3 = Label(root,text = "*",bg="black",fg='white',font=("Arial Black",20))
s3.place(relx =0.023, rely = 0.52)

s4 = Label(root,text = "*",bg="black",fg='white',font=("Arial Black",20))
s4.place(relx =0.023, rely = 0.6985)

s5 = Label(root,text = "*",bg="black",fg='white',font=("Arial Black",20))
s5.place(relx =0.023, rely = 0.7985)

s6 = Label(root,text = "*",bg="black",fg='white',font=("Arial Black",20))
s6.place(relx =0.023, rely = 0.8985)

home_frame()

root.mainloop()
