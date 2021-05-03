from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import re
import os


def main():
    root = Tk()
    app = Window1(root)



class Window1:
    def __init__(self, master):
        self.master =master
        self.master.title("ADMIN LOGIN")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg ='powder blue')
        self.frame = Frame(self.master, bg ='powder blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'ADMIN LOGIN', font=('ariel',50,'bold'), bg='powder blue', fg='black')
        self.lblTitle.grid(row =0, column = 0, columnspan=2, pady = 40)
        
        #+++++++++++++++++++++++++++++++++++++++++
        self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600
                               ,font=('arial',20,'bold'),relief='ridge',bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600
                               ,font=('arial',20,'bold'),relief='ridge',bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        #=====label and entry
        self.lblUsername=Label(self.LoginFrame1, text = 'Username',font=('arial',20,'bold'),bd =22, bg ='cadet blue', fg='Cornsilk')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',20,'bold'),textvariable= self.Username)
        self.txtUsername.grid(row=0, column=1)
        
        self.lblPassword=Label(self.LoginFrame1, text = 'Password',font=('arial',20,'bold'),bd =22, bg ='cadet blue', fg='Cornsilk')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',20,'bold'), show='*', textvariable= self.Password)
        self.txtPassword.grid(row=1, column=1)
        #=================================buttons
        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 17, font=('arial',20,'bold'), command =self.Login_System)
        self.btnLogin.grid(row=3,column =0, pady = 20, padx =8)
        #=========================================definations
    def Login_System(self):
        u =(self.Username.get())
        p =(self.Password.get())
        if (u ==str("ANURAG") and p ==str(12345)):
            root.destroy()
            os.system('ok.py')
            
        else:
            tkinter.messagebox.askyesno("Login Systems", "Too Bad, invalid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

  
#=============================================== 

if __name__=='__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()