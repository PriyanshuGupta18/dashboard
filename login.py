from cgitb import text
from datetime import datetime
from textwrap import fill
import time
from datetime import date
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import title
from PIL import Image,ImageTk,ImageDraw
from math import*
import pymysql
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#1e81b0")
        self.bg=ImageTk.PhotoImage(file="images/log.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
        login_frame=Frame(self.root,bg='white',bd=0)
        login_frame.place(x=300,y=76,height=550,width=800)

        self.today=StringVar()
        self.today=date.today()
        self.now=StringVar()
        self.now=datetime.now()

        title=Label(login_frame,text="LOGIN",font=("times new roman",30,"bold"),bg='white',fg='brown').place(x=300,y=50)
        lbl_name=Label(login_frame,text="NAME",font=("times new roman",15,"bold"),bg='white',fg='brown').place(x=250,y=150)
        self.txt_name=Entry(login_frame,font=("goudy old style",12),bg="#FEFFCE")
        self.txt_name.place(x=320,y=150,width=250)

        lbl_pass=Label(login_frame,text="PASSWORD",font=("times new roman",15,"bold"),bg='white',fg='brown').place(x=200,y=250)
        self.txt_pass=Entry(login_frame,font=("goudy old style",12),bg="#FEFFCE",show='*')
        self.txt_pass.place(x=320,y=250,width=250)

        lbl_type=Label(login_frame,text="TYPE",font=("times new roman",15,"bold"),bg='white',fg='brown').place(x=250,y=350)
        self.txt_type=ttk.Combobox(login_frame,values=('Employee','Admin'),font=("goudy old style",15,'bold'))
        self.txt_type.place(x=320,y=350,width=250)

        btn_reg=Button(login_frame,text="register new user?",cursor="hand2",command=self.register_window,font=("times new roman",15),bg="white",bd=0,fg="brown").place(x=250,y=450)
        btn_login=Button(login_frame,text="LOGIN",cursor="hand2",command=self.login,font=("times new roman",15),bg="brown",fg="white").place(x=500,y=450)


        self.lbl=Label(self.root,bg="black")
        self.lbl.place(x=90,y=120,height=450,width=350)


        self.working()



    def register_window(self):
        self.root.destroy()
        os.system("python register.py")





    def login(self):
        if self.txt_name.get()=="" or self.txt_pass.get()=="" or self.txt_type.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
                cur=con.cursor()

                cur.execute("select * from users where NAME=%s and PASSWORD=%s",(self.txt_name.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid credentials",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome {self.txt_name.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                    con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)


    def clock_img(self,hr,mint,sec):
        clock=Image.new("RGB",(400,400),(0,0,0))
        draw=ImageDraw.Draw(clock)
        bg=Image.open("images/clock.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#9D00FF",width=3)
        draw.line((200,200,200+80*sin(radians(mint)),200-80*cos(radians(mint))),fill="#9D00FF",width=3)
        draw.line((200,200,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="#FF0000",width=3)
        clock.save("images/clock_image.png")


    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        mint=(m/60)*360
        sec=(s/60)*360
        self.clock_img(hr,mint,sec)
        self.img=ImageTk.PhotoImage(file="images/clock_image.png")
        self.lbl.config(image=self.img)
        self.lbl.after(100,self.working)




if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
