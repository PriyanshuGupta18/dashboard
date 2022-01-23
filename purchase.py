from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import datetime
import pymysql
class Purchase:
    def __init__(self,root):
        self.root=root
        self.root.title("Drug Store Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#1e81b0")
        self.root.focus_force()


         #window title
        title=Label(self.root,text="Inventory",font=("goudy old style",20,"bold"),bg="#e28743",fg="#eeeee4").place(x=10,y=15,width=1180,height=50)



        #data entry
        self.var_barcode=StringVar()
        self.var_name=StringVar()
        self.med_list=[]
        self.fetch_mname()
        self.var_type=StringVar()
        self.var_company=StringVar()
        self.var_quantity=DoubleVar()
        self.var_cp=DoubleVar()
        self.var_total=DoubleVar()



        #fields
        lbl_barcode=Label(self.root,text="Barcode",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=160)
        lbl_type=Label(self.root,text="Drug Type",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=50,y=220)
        lbl_company=Label(self.root,text="Company Name",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=100)
        lbl_quantity=Label(self.root,text="Qunatity",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=160)
        lbl_cp=Label(self.root,text="Cost Price",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=220)
        lbl_total=Label(self.root,text="Total Amount",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=500,y=300)




        self.txt_mname=ttk.Combobox(self.root,textvariable=self.var_name,values=self.med_list,font=("goudy old style",15,'bold'))
        self.txt_mname.place(x=180,y=160,width=170)
        self.txt_mname.set("Select")

        btn_search=Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.search).place(x=360,y=160,width=105,height=30)


        txt_barcode=Entry(self.root,textvariable=self.var_barcode,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=180,y=100,width=200)
        txt_type=Entry(self.root,textvariable=self.var_type,font=("goudy old style",15,'bold'),bg="#FEFFCE",state='readonly').place(x=180,y=220,width=200)
        txt_company=Entry(self.root,textvariable=self.var_company,font=("goudy old style",15,'bold'),bg="#FEFFCE",state='readonly').place(x=650,y=100,width=200)
        txt_quantity=Entry(self.root,textvariable=self.var_quantity,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=650,y=160,width=200)
        txt_cp=Entry(self.root,textvariable=self.var_cp,font=("goudy old style",15,'bold'),bg="#FEFFCE",state='readonly').place(x=650,y=220,width=200)
        txt_total=Entry(self.root,textvariable=self.var_total,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=650,y=300,width=200)


        self.btn_add=Button(self.root,text="Submit",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.submit).place(x=180,y=300,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.clear).place(x=320,y=300,width=110,height=40)




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
            cur.execute(f"select TYPE,COMPANY_NAME,COST_PRICE from drugs where NAME=%s",(self.var_name.get(),))
            rows=cur.fetchone()
            if rows!=None:
                self.var_type.set(rows[0])
                self.var_company.set(rows[1])
                self.var_cp.set(rows[2])
            else :
                messagebox.showerror("Error","No record found",parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')





    def submit(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            if self.var_quantity.get()=="" or self.var_barcode.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :

                    cur.execute("INSERT into purchase values(%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_barcode.get(),
                        self.var_name.get(),
                        self.var_type.get(),
                        self.var_company.get(),
                        self.var_quantity.get(),
                        self.var_cp.get(),
                        self.var_total.get()
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Data saved successfully")
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')





    def clear(self):
        self.var_barcode.set("")
        self.var_type.set("")
        self.var_name.set("")
        self.var_company.set("")
        self.var_cp.set("")
        self.var_total.set("")
        self.var_quantity.set("")



if __name__=="__main__":
    root=Tk()
    obj=Purchase(root)
    root.mainloop()