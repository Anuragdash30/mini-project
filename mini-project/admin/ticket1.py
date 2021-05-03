from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import re
import os

class Admin:
    def __init__(self,root):
        self.root=root
        self.root.title("Bookings")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="BOOKING PAGE",bd=10,relief=GROOVE,font=("Helvetica",30,"bold"),bg="light blue",fg="black")
        title.pack(side=TOP,fill=X)
#variables++++++++++++++++++++++++++++++++++++++++
        self.payid=StringVar()
        self.dest=StringVar()
        self.days=StringVar()
        self.amount1=StringVar()
        self.custnam=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

#manage=============================================== 
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cadet blue")
        Manage_Frame.place(x=20,y=70,width=500,height=560)

        m_title=Label(Manage_Frame,text="Manage Bookings",bg="cadet blue",fg="black",font=("Helvetica",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Package ID",bg="cadet blue",fg="black",font=("Helvetica",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.payid,font=("Helvetica",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_roll=Label(Manage_Frame,text="Place Name",bg="cadet blue",fg="black",font=("Helvetica",15,"bold"))
        lbl_roll.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.dest,font=("Helvetica",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        
        lbl_days=Label(Manage_Frame,text="No of Days",bg="cadet blue",fg="black",font=("Helvetica",15,"bold"))
        lbl_days.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_days=Entry(Manage_Frame,textvariable=self.days,font=("Helvetica",15,"bold"),bd=5,relief=GROOVE)
        txt_days.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_price=Label(Manage_Frame,text="Price",bg="cadet blue",fg="black",font=("Helvetica",15,"bold"))
        lbl_price.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_price=Entry(Manage_Frame,textvariable=self.amount1,font=("Helvetica",15,"bold"),bd=5,relief=GROOVE)
        txt_price.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        lbl_cust=Label(Manage_Frame,text="Customer name",bg="cadet blue",fg="black",font=("Helvetica",15,"bold"))
        lbl_cust.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_cust=Entry(Manage_Frame,textvariable=self.custnam,font=("Helvetica",15,"bold"),bd=5,relief=GROOVE)
        txt_cust.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        #======button++++++++++++++++++
       
        Addbtn = Button(text="ADD",command=self.add_pack, bg="navy blue", fg = "white", font=("bold", 15)).place(x=50,y=450)   
        updatebtn = Button(text="UPDATE",command=self.update_data, bg="navy blue", fg = "white", font=("bold", 15)).place(x=130,y=450)   
        deletebtn = Button(text="DELETE",command=self.delete_data, bg="navy blue", fg = "white", font=("bold", 15)).place(x=250,y=450)  
        clearbtn = Button(text="CLEAR",command=self.clear, bg="navy blue", fg = "white", font=("bold", 15)).place(x=370,y=450)  
        btn_login = Button(text="LOGOUT",command=self.exit,  bg="dark blue", fg="white", font=("bold",16)).place(x=1225, y=10)
        btn_login = Button(text="PACKAGES",command=self.exit1,  bg="dark blue", fg="white", font=("bold",16)).place(x=1090, y=10)


#detail=======================================================        
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cadet blue")
        Detail_Frame.place(x=550,y=70,width=750,height=560)

        lbl_Search=lbl_price=Label(Detail_Frame,text="Search By",bg="cadet blue",fg="black",font=("Helvetica",15,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("Helvetica",13,"bold"),state='readonly')
        combo_search['values']=("ID","Place Name")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("Helvetica",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn = Button(text="Search",command= self.search_data, bg="light blue", fg = "black", font=("bold", 12)).place(x=1120,y=87)  
        showbtn = Button(text="Show All",command= self.fetch_data, bg="light blue", fg = "black", font=("bold", 12)).place(x=1200,y=87) 
        
#==========================TABLE FRAME++++++++++++++++++++++++++
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="cadet blue")
        Table_Frame.place(x=10,y=70,width=720,height=470)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Package_table=ttk.Treeview(Table_Frame,columns=("Package ID","Place Name","No of Days","price","Customer Name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Package_table.xview)
        scroll_y.config(command=self.Package_table.yview)
        self.Package_table.heading("Package ID",text="Package ID")
        self.Package_table.heading("Place Name",text="Place Name")
        self.Package_table.heading("No of Days",text="No of days")
        self.Package_table.heading("price",text="Price")
        self.Package_table.heading("Customer Name",text="Customer Name")
        self.Package_table['show']='headings'
        self.Package_table.column("Package ID",width=150)
        self.Package_table.column("Place Name",width=180)
        self.Package_table.column("No of Days",width=200)
        self.Package_table.column("price",width=180)
        self.Package_table.column("Customer Name",width=180)
        self.Package_table.pack(fill=BOTH,expand=1)
        self.Package_table.bind("<ButtonRelease-1>",self.get_cursor)


        self.fetch_data()
   

    def exit1(self):
        root.destroy()
        os.system('ok.py')      
        

    def add_pack(self):
        if self.payid.get()=="":
                messagebox.showerror("Error","Package Id in required")
        elif self.dest.get()=="":
                messagebox.showerror("Error","Place Name in required")
        elif self.days.get()=="":
                messagebox.showerror("Error","No of Days in required")
        elif self.amount1.get()=="":
                messagebox.showerror("Error","Price in required")
        elif self.custnam.get()=="":
                messagebox.showerror("Error","Price in required")
        else:
                con=mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
                cur=con.cursor()
                cur.execute("insert into pay values(%s,%s,%s,%s,%s)",(self.payid.get(),
                                                                self.dest.get(),
                                                                self.days.get(),
                                                                self.amount1.get(),
                                                                self.custnam.get()
                ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
        cur=con.cursor()
        cur.execute("select payid,dest,days,amount1,custnam from Pay")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Package_table.delete(*self.Package_table.get_children())
                for row in rows:
                        self.Package_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.payid.set("")
        self.dest.set("")
        self.days.set("")
        self.amount1.set("")
        self.custnam.set("")

    def get_cursor(self,ev):
        cursor_row=self.Package_table.focus()
        content=self.Package_table.item(cursor_row)
        row=content['values']
        self.payid.set(row[0])
        self.dest.set(row[1])
        self.days.set(row[2])
        self.amount1.set(row[3])
        self.custnam.set(row[4])
    def update_data(self):
        con=mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
        cur=con.cursor()
        cur.execute("update pay set dest=%s,days=%s,amount1=%s,custnam=%s where pid=%s",(
                                                           self.dest.get(),
                                                           self.days.get(),
                                                           self.amount1.get(),
                                                           self.custnam.get(),
                                                           self.payid.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been updated")
    def delete_data(self):
        con=mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
        cur=con.cursor()
        cur.execute("delete from pay where payid=%s",(self.payid.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been deleted")

    def search_data(self):
        con=mysql.connect(host="localhost",user="root",passwd="anurag",database="regdb")
        cur=con.cursor()

        p=self.search_by.get()
        if 'ID' in p:   
                cur.execute("SELECT * FROM pay WHERE payid=%s",(self.search_txt.get(),))
        else:
                cur.execute("SELECT * FROM pay WHERE dest=%s",(self.search_txt.get(),))
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Package_table.delete(*self.Package_table.get_children())
                for row in rows:
                        self.Package_table.insert('',END,values=row)
                con.commit()
        con.close()

    def exit(self):
        root.destroy()

        

root=Tk()
ob=Admin(root)
root.mainloop()


