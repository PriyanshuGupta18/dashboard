from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk,ImageDraw
from company import Company
from medicine import medicine
from datetime import *
from math import *
from bill import Bill
from show_bill import Generate
from admin_access import Admin_access
import time
import os
class DSMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Drug Store Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#1e81b0")
        #window icon
        self.logo_dash=ImageTk.PhotoImage(file=".\images\dash_icon.png")
    


        #window title
        title=Label(self.root,text="Drug Store Management System",padx=50,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#e28743",fg="#eeeee4").place(x=0,y=0,relwidth=1,height=50)

        
        #Menu
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="White")
        M_Frame.place(x=10,y=70,width=1340,height=72)


        #Buttons
        btn_company=Button(M_Frame,text="Company",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.add_company).place(x=10,y=5,width=180,height=40)
        btn_drug=Button(M_Frame,text="Medicine",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.add_medicine).place(x=200,y=5,width=180,height=40)
        btn_sales=Button(M_Frame,text="Sales",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.add_bill).place(x=390,y=5,width=180,height=40)
        btn_generate=Button(M_Frame,text="Generate Bill",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.show_bill).place(x=580,y=5,width=180,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.logout).place(x=770,y=5,width=180,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.quit).place(x=960,y=5,width=180,height=40)
        btn_purchase=Button(M_Frame,text="Purchase",font=("goudy old style",15,"bold"),bg="#e28743",fg="#eeeee4",cursor="hand2",command=self.purchase).place(x=1150,y=5,width=180,height=40)


        #content
        self.bg_img=Image.open("images/content_window.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=195,width=920,height=350)

        self.lbl=Label(self.root,bg="white",bd=20,relief=RAISED)
        self.lbl.place(x=10,y=170,height=400,width=350)


        self.working()

        #Footer
        title=Label(self.root,text="Drug Store Management System\nDBMS Mini Project\nAcharya Institute of Technology\nDesigned By Priyanshu Gupta (1AY19CS081)",font=("goudy old style",15),bg="#e28743",fg="#eeeee4").pack(side="bottom",fill=X)

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        mint=(m/60)*360
        sec=(s/60)*360
        self.clock_img(hr,mint,sec)
        self.img=ImageTk.PhotoImage(file="images/clock_image1.png")
        self.lbl.config(image=self.img)
        self.lbl.after(100,self.working)



    def clock_img(self,hr,mint,sec):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        bg=Image.open("images/clock2.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="brown",width=3)
        draw.line((200,200,200+80*sin(radians(mint)),200-80*cos(radians(mint))),fill="brown",width=3)
        draw.line((200,200,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="green",width=3)
        clock.save("images/clock_image1.png")


    def add_company(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Company(self.new_win)
    

    def add_medicine(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=medicine(self.new_win)


    def add_bill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Bill(self.new_win)


    def purchase(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Admin_access(self.new_win)

    def show_bill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Generate(self.new_win)

        
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you want to logout",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")


    def quit(self):
        op=messagebox.askyesno("Confirm","Do you want to Exit",parent=self.root)
        if op==True:
            self.root.destroy()



if __name__=="__main__":
    root=Tk()
    obj=DSMS(root)
    root.mainloop()
