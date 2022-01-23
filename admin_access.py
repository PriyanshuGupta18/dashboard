from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import os
class Admin_access:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#1e81b0")
        self.bg=ImageTk.PhotoImage(file="images/log.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        frame1=Frame(self.root,bg="white")
        frame1.place(x=320,y=100,width=700,height=500)


        title=Label(frame1,text="ADMIN LOGIN",font=("calibri",25,"bold"),bg="white",fg="orange").place(x=250,y=30)


        lbl_name=Label(frame1,text="NAME",font=("times new roman",15,"bold"),bg='white',fg='brown').place(x=150,y=150)
        self.txt_uname=ttk.Combobox(frame1,values='Admin',font=("goudy old style",15,'bold'))
        self.txt_uname.place(x=220,y=150,width=200)
        self.txt_uname.set("Select")

        lbl_pass=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg='white',fg='brown').place(x=100,y=250)
        self.txt_pass=Entry(frame1,font=("goudy old style",12),bg="#FEFFCE",show='*')
        self.txt_pass.place(x=220,y=250,width=250)

        btn_login=Button(frame1,text="LOGIN",cursor="hand2",command=self.login,font=("times new roman",15),bg="brown",fg="white").place(x=300,y=330)




    def login(self):
        if self.txt_uname.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
                cur=con.cursor()

                cur.execute("select NAME,PASSWORD from users where NAME=%s and PASSWORD=%s",(self.txt_uname.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid credentials",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome {self.txt_uname.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python purchase.py")
                    con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=Admin_access(root)
    root.mainloop()