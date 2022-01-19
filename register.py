from multiprocessing import parent_process
from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign Up")
        self.root.geometry("1350x700+0+0")
        
        self.bg=ImageTk.PhotoImage(file="images/register.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #register window frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=320,y=100,width=700,height=500)


        title=Label(frame1,text="REGISTER HERE",font=("calibri",20,"bold"),bg="white",fg="orange").place(x=50,y=30)

        lbl_id=Label(frame1,text="ID",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=50,y=100)

        self.txt_id=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_id.place(x=50,y=130,width=250)


        lbl_name=Label(frame1,text="NAME",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=370,y=100)

        self.txt_name=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_name.place(x=370,y=130,width=250)

        lbl_dob=Label(frame1,text="D.O.B",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=50,y=170)

        self.txt_dob=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_dob.place(x=50,y=200,width=250)


        lbl_address=Label(frame1,text="ADDRESS",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=370,y=170)

        self.txt_address=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_address.place(x=370,y=200,width=250)


        lbl_phone=Label(frame1,text="PHONE",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=50,y=240)

        self.txt_phone=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_phone.place(x=50,y=270,width=250)


        lbl_salary=Label(frame1,text="SALARY",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=370,y=240)

        self.txt_salary=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_salary.place(x=370,y=270,width=250)


        lbl_password=Label(frame1,text="ENTER PASSWORD",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=50,y=310)

        self.txt_password=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_password.place(x=50,y=350,width=250)


        lbl_confirm=Label(frame1,text="CONFIRM PASSWORD",font=("goudy old style",15,'bold'),fg='black',bg='white').place(x=370,y=310)

        self.txt_confirm=Entry(frame1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_confirm.place(x=370,y=350,width=250)


        btn_register=Button(frame1,text="SIGN UP",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.register_data).place(x=50,y=420,width=200,height=40)
        btn_login=Button(frame1,text="LOG IN",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.login_window).place(x=300,y=420,width=200,height=40)




    def register_data(self):
        if self.txt_id.get()=="" or self.txt_address.get()=="" or self.txt_confirm.get()=="" or self.txt_dob.get()=="" or self.txt_name.get()=="" or self.txt_password.get()=="" or self.txt_phone.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_confirm.get():
            messagebox.showerror("Error","Password and confirm passwords dont match",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
                cur=con.cursor()

                cur.execute("select * from users where ID=%s",(self.txt_id.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already present",parent=self.root)
                else:
                    cur.execute("INSERT into users values(%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.txt_id.get(),
                            self.txt_name.get(),
                            self.txt_dob.get(),
                            self.txt_address.get(),
                            self.txt_phone.get(),
                            self.txt_salary.get(),
                            self.txt_password.get()
                        )
                        )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.clear()
                    self.login_window()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)




    def login_window(self):
        self.root.destroy()
        os.system("python login.py")



    def clear(self):
        self.txt_id.delete(0,END)
        self.txt_address.delete(0,END)
        self.txt_confirm.delete(0,END)
        self.txt_dob.delete(0,END)
        self.txt_name.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_salary.delete(0,END)


if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
