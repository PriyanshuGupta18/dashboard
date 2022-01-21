from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import datetime
import pymysql
class Bill:
    def __init__(self,root):
        self.root=root
        self.root.title("Drug Store Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#1e81b0")
        self.root.focus_force()


         #window title
        title=Label(self.root,text="Billing",font=("goudy old style",20,"bold"),bg="#e28743",fg="#eeeee4").place(x=10,y=15,width=1180,height=50)



        #variables
        self.var_user=StringVar()
        self.user_list=[]
        self.fetch_uname()
        self.var_barcode=StringVar()
        self.var_name=StringVar()
        self.med_list=[]
        self.fetch_mname()
        self.var_type=StringVar()
        self.var_dose=StringVar()
        self.var_quantity=DoubleVar()
        self.var_price=DoubleVar()
        self.var_total=DoubleVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_rct=StringVar()




        #fields
        lbl_User=Label(self.root,text="User Name",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=100)
        lbl_barcode=Label(self.root,text="Barcode",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=160)
        lbl_name=Label(self.root,text="Drug Name",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=220)
        lbl_type=Label(self.root,text="Drug Type",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=280)
        lbl_dose=Label(self.root,text="Dosage",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=340)
        lbl_quantity=Label(self.root,text="Quantity",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=100)
        lbl_price=Label(self.root,text="Unit Price",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=160)
        lbl_total=Label(self.root,text="Net Amount",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=220)
        lbl_date=Label(self.root,text="Date",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=280)
        lbl_time=Label(self.root,text="Time",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=340)
        lbl_time=Label(self.root,text="Reciept No.",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=400)


        self.txt_uname=ttk.Combobox(self.root,textvariable=self.var_user,values=self.user_list,font=("goudy old style",15,'bold'))
        self.txt_uname.place(x=180,y=100,width=200)
        self.txt_uname.set("Select")


        self.txt_mname=ttk.Combobox(self.root,textvariable=self.var_name,values=self.med_list,font=("goudy old style",15,'bold'))
        self.txt_mname.place(x=180,y=220,width=170)
        self.txt_mname.set("Select")

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.search).place(x=380,y=220,width=105,height=30)


        txt_barcode=Entry(self.root,textvariable=self.var_barcode,font=("goudy old style",15,'bold'),bg="#FEFFCE",state="readonly").place(x=180,y=160,width=200)
        txt_type=Entry(self.root,textvariable=self.var_type,font=("goudy old style",15,'bold'),bg="#FEFFCE",state='readonly').place(x=180,y=280,width=200)
        txt_dose=Entry(self.root,textvariable=self.var_dose,font=("goudy old style",15,'bold'),bg="#FEFFCE",state='readonly').place(x=180,y=340,width=200)
        txt_quantity=Entry(self.root,textvariable=self.var_quantity,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=620,y=100,width=200)
        txt_price=Entry(self.root,textvariable=self.var_price,font=("goudy old style",15,'bold'),bg="#FEFFCE",state='readonly').place(x=620,y=160,width=200)
        txt_total=Entry(self.root,textvariable=self.var_total,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=620,y=220,width=200)
        txt_date=Entry(self.root,textvariable=self.var_date,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=620,y=280,width=200)
        txt_time=Entry(self.root,textvariable=self.var_time,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=620,y=340,width=200)
        txt_rct=Entry(self.root,textvariable=self.var_rct,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=620,y=400,width=200)


        #buttons
        self.btn_add=Button(self.root,text="Submit",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.submit).place(x=180,y=420,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.clear).place(x=320,y=420,width=110,height=40)



        self.bg_img=Image.open("images/bills.png")
        self.bg_img=self.bg_img.resize((300,260),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=850,y=100)



    def fetch_uname(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute("select NAME from users")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.user_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    
    def fetch_mname(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute("select NAME from drugs")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.med_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')




    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute(f"select BARCODE,DOSE,SELLING_PRICE,TYPE from drugs where NAME=%s",(self.var_name.get(),))
            rows=cur.fetchone()
            if rows!=None:
                self.var_barcode.set(rows[0])
                self.var_dose.set(rows[1])
                self.var_price.set(rows[2])
                self.var_type.set(rows[3])
            else :
                messagebox.showerror("Error","No record found",parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    def submit(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            if self.var_quantity.get()=="" or self.var_total.get()=="" or self.var_date.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :

                    cur.execute("INSERT into history_sales values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_user.get(),
                        self.var_rct.get(),
                        self.var_barcode.get(),
                        self.var_name.get(),
                        self.var_type.get(),
                        self.var_dose.get(),
                        self.var_quantity.get(),
                        self.var_price.get(),
                        self.var_total.get(),
                        self.var_date.get(),
                        self.var_time.get(),
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Data saved successfully")
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')




    def clear(self):
        self.var_user.set("")
        self.var_barcode.set("")
        self.var_type.set("")
        self.var_dose.set("")
        self.var_quantity.set("")
        self.var_price.set("")
        self.var_total.set("")
        self.var_name.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_rct.set("")







if __name__=="__main__":
    root=Tk()
    obj=Bill(root)
    root.mainloop()