from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import datetime
import pymysql
class medicine:
    def __init__(self,root):
        self.root=root
        self.root.title("Drug Store Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#1e81b0")
        self.root.focus_force()


         #window title
        title=Label(self.root,text="Drug Details",font=("goudy old style",20,"bold"),bg="#e28743",fg="#eeeee4").place(x=10,y=15,width=1180,height=35)
        

        #variables for storing field data
        self.var_name1=StringVar()
        self.var_type=StringVar()
        self.var_barcode=StringVar()
        self.var_dose=StringVar()
        self.var_code=StringVar()
        self.var_cp=DoubleVar()
        self.var_sp=DoubleVar()
        self.var_company=StringVar()
        self.var_production=StringVar()
        self.var_expiry=StringVar()
        self.var_place=StringVar()
        self.var_quantity=StringVar()



        #Fields
        lbl_MedicineName=Label(self.root,text="Medicine Name",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=60)
        lbl_Barcode=Label(self.root,text="Barcode",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=100)
        lbl_MedicineType=Label(self.root,text="Medicine Type",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=140)
        lbl_MedicineDose=Label(self.root,text="Medicine Dose",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=180)
        lbl_MedicineCode=Label(self.root,text="Medicine Code",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=220)
        lbl_costprice=Label(self.root,text="Cost Price",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=260)
        lbl_sellingprice=Label(self.root,text="Selling Price",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=350,y=60)
        lbl_companyname=Label(self.root,text="Company Name",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=350,y=100)
        lbl_productiondate=Label(self.root,text="Production Date",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=350,y=140)
        lbl_expirydate=Label(self.root,text="Expiry Date",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=350,y=180)
        lbl_place=Label(self.root,text="Place",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=350,y=220)
        lbl_quantity=Label(self.root,text="Quantity",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=350,y=260)


        #data for fields
        self.txt_MedicineName=Entry(self.root,textvariable=self.var_name1,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_MedicineName.place(x=170,y=60,width=170)

        self.txt_Barcode=Entry(self.root,textvariable=self.var_barcode,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=170,y=100,width=170)

        
        self.txt_MedicineType=Entry(self.root,textvariable=self.var_type,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_MedicineType.place(x=170,y=140,width=170)


        self.txt_MedicineDose=Entry(self.root,textvariable=self.var_dose,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_MedicineDose.place(x=170,y=180,width=170)


        self.txt_MedicineCode=Entry(self.root,textvariable=self.var_code,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_MedicineCode.place(x=170,y=220,width=170)


        self.txt_cp=Entry(self.root,textvariable=self.var_cp,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_cp.place(x=170,y=260,width=170)


        self.txt_sp=Entry(self.root,textvariable=self.var_sp,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_sp.place(x=520,y=60,width=170)


        self.company_list=[]
        self.fetch_cname()
        self.txt_cname=ttk.Combobox(self.root,textvariable=self.var_company,values=self.company_list,font=("goudy old style",15,'bold'))
        self.txt_cname.place(x=520,y=100,width=170)
        self.txt_cname.set("Select")


        self.txt_production=Entry(self.root,textvariable=self.var_production,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_production.place(x=520,y=140,width=170)


        self.txt_expiry=Entry(self.root,textvariable=self.var_expiry,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_expiry.place(x=520,y=180,width=170)


        self.txt_place=Entry(self.root,textvariable=self.var_place,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_place.place(x=520,y=220,width=170)


        self.txt_quantity=Entry(self.root,textvariable=self.var_quantity,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_quantity.place(x=520,y=260,width=170)






        #Button creation
        self.btn_add=Button(self.root,text="Add",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.add)
        self.btn_add.place(x=170,y=400,width=110,height=40)

        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.update)
        self.btn_update.place(x=290,y=400,width=110,height=40)

        self.btn_Delete=Button(self.root,text="Delete",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.delete)
        self.btn_Delete.place(x=410,y=400,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=530,y=400,width=110,height=40)


        #query panel
        self.var_search=StringVar()
        lbl_search_drugname=Label(self.root,text="Search Medicine",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=700,y=60)
        txt_search_drugname=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=870,y=60,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.search).place(x=1085,y=60,width=105,height=30)


        #search results
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=705,y=100,width=485,height=340)


        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.DrugTable=ttk.Treeview(self.C_Frame,columns=("Name","Type","Barcode","Dose","Code","cp","sp","company","prod","exp","place","quant"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.DrugTable.xview)
        scrolly.config(command=self.DrugTable.yview)

        self.DrugTable.heading("Name",text="Drug Name")
        self.DrugTable.heading("Type",text="Drug Type")
        self.DrugTable.heading("Barcode",text="Barcode")
        self.DrugTable.heading("Dose",text="Dosage")
        self.DrugTable.heading("Code",text="Code")
        self.DrugTable.heading("cp",text="Cost Price")
        self.DrugTable.heading("sp",text="Selling Price")
        self.DrugTable.heading("company",text="Company Name")
        self.DrugTable.heading("prod",text="Production Date")
        self.DrugTable.heading("exp",text="Expiry Date")
        self.DrugTable.heading("place",text="Place")
        self.DrugTable.heading("quant",text="Quantity")
        self.DrugTable["show"]='headings'

        self.DrugTable.column("Name",width=100)
        self.DrugTable.column("Type",width=100)
        self.DrugTable.column("Barcode",width=100)
        self.DrugTable.column("Dose",width=100)
        self.DrugTable.column("Code",width=100)
        self.DrugTable.column("cp",width=100)
        self.DrugTable.column("sp",width=100)
        self.DrugTable.column("company",width=100)
        self.DrugTable.column("prod",width=100)
        self.DrugTable.column("exp",width=100)
        self.DrugTable.column("place",width=100)
        self.DrugTable.column("quant",width=100)


        self.DrugTable.pack(fill=BOTH,expand=1)
        self.DrugTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def get_data(self,event):
        self.txt_MedicineName.config(state='readonly')
        self.txt_MedicineName
        r=self.DrugTable.focus()
        content=self.DrugTable.item(r)
        row=content["values"]
        self.var_name1.set(row[0])
        self.var_type.set(row[1])
        self.var_barcode.set(row[2])
        self.var_dose.set(row[3])
        self.var_code.set(row[4])
        self.var_cp.set(row[5])
        self.var_sp.set(row[6])
        self.var_company.set(row[7])
        self.var_production.set(row[8])
        self.var_expiry.set(row[9])
        self.var_place.set(row[10])
        self.var_quantity.set(row[11])    


    def add(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            if self.var_name1.get()=="" or self.var_type.get()=="" or self.var_barcode.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :
                cur.execute("select * from drugs where NAME=%s",(self.var_name1.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Medicine name already present",parent=self.root)
                else :
                    cur.execute("INSERT into drugs values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_name1.get(),
                        self.var_type.get(),
                        self.var_barcode.get(),
                        self.var_dose.get(),
                        self.var_code.get(),
                        self.var_cp.get(),
                        self.var_sp.get(),
                        self.var_company.get(),
                        self.var_production.get(),
                        self.var_expiry.get(),
                        self.var_place.get(),
                        self.var_quantity.get()
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Medicine added successfully")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')


    def show(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute("select * from drugs")
            rows=cur.fetchall()
            self.DrugTable.delete(*self.DrugTable.get_children())
            for i in rows:
                self.DrugTable.insert('',END,values=i)
            con.close()



        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    def fetch_cname(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute("select NAME from company")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.company_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    def update(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            if self.var_name1.get()=="" or self.var_type.get()=="" or self.var_barcode.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :
                cur.execute("select * from drugs where NAME=%s",(self.var_name1.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Medicine From List",parent=self.root)
                else :
                    cur.execute("UPDATE drugs set NAME=%s,TYPE=%s,DOSE=%s,CODE=%s,COST_PRICE=%s,SELLING_PRICE=%s,COMPANY_NAME=%s,PRODUCTION_DATE=%s,EXPIRATION_DATE=%s,PLACE=%s,QUANTITY=%s where BARCODE=%s",
                    (
                        self.var_name1.get(),
                        self.var_type.get(),
                        self.var_dose.get(),
                        self.var_code.get(),
                        self.var_cp.get(),
                        self.var_sp.get(),
                        self.var_company.get(),
                        self.var_production.get(),
                        self.var_expiry.get(),
                        self.var_place.get(),
                        self.var_quantity.get(),
                        self.var_barcode.get(),
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Record updated successfully")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    def clear(self):
        self.show()
        self.var_name1.set("")
        self.var_type.set("")
        self.var_barcode.set("")
        self.var_dose.set("")
        self.var_code.set("")
        self.var_cp.set("")
        self.var_sp.set("")
        self.var_company.set("")
        self.var_production.set("")
        self.var_expiry.set("")
        self.var_place.set("")
        self.var_quantity.set("")  
        self.txt_MedicineName.config(state='normal')
        self.var_search.set("")



    def delete(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        try:
            if self.var_name1.get()=="" or self.var_type.get()=="" or self.var_barcode.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :
                cur.execute("select * from drugs where NAME=%s",(self.var_name1.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Medicine name cannot be empty",parent=self.root)
                else :
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("Delete from drugs where NAME=%s",(self.var_name1.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Medicine data deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute(f"select * from drugs where NAME LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchone()
            self.DrugTable.delete(*self.DrugTable.get_children())
            for i in rows:
                self.DrugTable.insert('',END,values=i)
            con.close()



        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')

if __name__=="__main__":
    root=Tk()
    obj=medicine(root)
    root.mainloop()