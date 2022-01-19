from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Company:
    def __init__(self,root):
        self.root=root
        self.root.title("Drug Store Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#1e81b0")
        self.root.focus_force()


         #window title
        title=Label(self.root,text="Company Details",font=("goudy old style",20,"bold"),bg="#e28743",fg="#eeeee4").place(x=10,y=15,width=1180,height=35)
        

        #variables for storing field data
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()


        #Fields
        lbl_companyName=Label(self.root,text="Company Name",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=60)
        lbl_company_Phone=Label(self.root,text="Company Phone",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=100)
        lbl_companyAddress=Label(self.root,text="Company Address",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=10,y=140)


        #data for fields
        self.txt_companyName=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_companyName.place(x=170,y=60,width=200)

        self.txt_company_Phone=Entry(self.root,textvariable=self.var_address,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=170,y=100,width=200)
        self.txt_company_Address=Entry(self.root,textvariable=self.var_phone,font=("goudy old style",15,'bold'),bg="#FEFFCE")
        self.txt_company_Address.place(x=170,y=140,width=470,height=130)


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
        lbl_search_companyName=Label(self.root,text="Search Company",font=("goudy old style",15,'bold'),bg="#1e81b0").place(x=700,y=60)
        txt_search_companyName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=870,y=60,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.search).place(x=1085,y=60,width=105,height=30)


        #search results
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=705,y=100,width=485,height=340)


        self.CompanyTable=ttk.Treeview(self.C_Frame,columns=("Name","Address","Phone"))
        self.CompanyTable.heading("Name",text="Company Name")
        self.CompanyTable.heading("Address",text="Company Address")
        self.CompanyTable.heading("Phone",text="Company Phone")
        self.CompanyTable["show"]='headings'

        self.CompanyTable.column("Name",width=50)
        self.CompanyTable.column("Address",width=150)
        self.CompanyTable.column("Phone",width=50)


        self.CompanyTable.pack(fill=BOTH,expand=1)
        self.CompanyTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def get_data(self,event):
        self.txt_companyName.config(state='readonly')
        self.txt_companyName
        r=self.CompanyTable.focus()
        content=self.CompanyTable.item(r)
        row=content["values"]
        self.var_name.set(row[0])
        self.var_phone.set(row[1])
        self.var_address.set(row[2])    


    def add(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            if self.var_name.get()=="" or self.var_address.get()=="" or self.var_phone.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :
                cur.execute("select * from company where NAME=%s",(self.var_name.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Company name already present",parent=self.root)
                else :
                    cur.execute("INSERT into company values(%s,%s,%s)",
                    (
                        self.var_name.get(),
                        self.var_address.get(),
                        self.var_phone.get()
                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Record added successfully")
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')


    def show(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute("select * from company")
            rows=cur.fetchall()
            self.CompanyTable.delete(*self.CompanyTable.get_children())
            for i in rows:
                self.CompanyTable.insert('',END,values=i)
            con.close()



        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    def update(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            if self.var_name.get()=="" or self.var_address.get()=="" or self.var_phone.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :
                cur.execute("select * from company where NAME=%s",(self.var_name.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course From List",parent=self.root)
                else :
                    cur.execute("UPDATE company set ADDRESS=%s,PHONE=%s where NAME=%s",
                    (
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_name.get()
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
        self.var_name.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_search.set("")
        self.txt_companyName.config(state='normal')



    def delete(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        try:
            if self.var_name.get()=="" or self.var_address.get()=="" or self.var_phone.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else :
                cur.execute("select * from company where NAME=%s",(self.var_name.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Company name cannot be empty",parent=self.root)
                else :
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("Delete from company where NAME=%s",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "company deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')



    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            cur.execute(f"select * from company where NAME LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CompanyTable.delete(*self.CompanyTable.get_children())
            for i in rows:
                self.CompanyTable.insert('',END,values=i)
            con.close()



        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')

if __name__=="__main__":
    root=Tk()
    obj=Company(root)
    root.mainloop()