from tkinter import*
from tkinter import font
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import datetime
import pymysql
class Generate:
    def __init__(self,root):
        self.root=root
        self.root.title("Drug Store Management System")
        self.root.geometry("1200x600+80+170")
        self.root.config(bg="#1e81b0")
        self.root.focus_force()


         #window title
        title=Label(self.root,text="Print Bill",font=("goudy old style",25,"bold"),bg="#e28743",fg="#eeeee4").place(x=10,y=15,width=1180,height=50)

        self.rct=StringVar()
        self.name=StringVar()
        self.quantity=StringVar()
        self.price=StringVar()
        self.total=StringVar()
        self.date=StringVar()
        self.time=StringVar()
        self.net=DoubleVar()



        self.var_search=StringVar()
        lbl_search=Label(self.root,text="Reciept number",font=("goudy old style",19,'bold'),bg="#1e81b0").place(x=230,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg="#FEFFCE").place(x=430,y=105,width=150)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg="#FF5733",cursor="hand2",command=self.search).place(x=600,y=105,width=105,height=30)


        lbl_final=Label(self.root,text="Net Payable",font=("goudy old style",19,'bold'),bg="#1e81b0").place(x=730,y=100)
        txt_final=Entry(self.root,textvariable=self.net,font=("goudy old style",15,'bold'),bg="#FEFFCE",state='readonly').place(x=880,y=105,width=150)


        self.B_Frame=Frame(self.root,bd=15,relief=GROOVE)
        self.B_Frame.place(x=230,y=150,width=800,height=420)


        self.BillTable=ttk.Treeview(self.B_Frame,columns=("Reciept_Number","Name","Quantity","Unit_Price","Gross_Total","Date","Time"))
        self.BillTable.heading("Reciept_Number",text="Reciept Number")
        self.BillTable.heading("Name",text="Name")
        self.BillTable.heading("Quantity",text="Quantity")
        self.BillTable.heading("Unit_Price",text="Unit Price")
        self.BillTable.heading("Gross_Total",text="Gross Total")
        self.BillTable.heading("Date",text="Date")
        self.BillTable.heading("Time",text="Time")
        self.BillTable["show"]='headings'

        self.BillTable.column("Reciept_Number",width=100)
        self.BillTable.column("Name",width=100)
        self.BillTable.column("Quantity",width=100)
        self.BillTable.column("Unit_Price",width=100)
        self.BillTable.column("Gross_Total",width=100)
        self.BillTable.column("Date",width=100)
        self.BillTable.column("Time",width=100)


        self.BillTable.pack(fill=BOTH,expand=1)
        self.BillTable.bind("<ButtonRelease-1>",self.get_data)



    def get_data(self):
        r=self.BillTable.focus()
        content=self.BillTable.item(r)
        row=content["values"]
        self.rct.set(row[0])
        self.name.set(row[1])
        self.quantity.set(row[2])
        self.price.set(row[3])
        self.total.set(row[4])
        self.date.set(row[5])
        self.time.set(row[6]) 




    def search(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()
        
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Please give a valid reciept number",parent=self.root)
            else:
                cur.execute(f"select RECIEPT_NO,NAME,QUANTITY,PRICE,AMOUNT,DATE,TIME from history_sales where RECIEPT_NO LIKE '%{self.var_search.get()}%'")
                rows=cur.fetchall()
                if rows!=None:
                    self.BillTable.delete(*self.BillTable.get_children())
                    for i in rows:
                        self.BillTable.insert('',END,values=i)
                else :
                    messagebox.showerror("Error","No such record found",parent=self.root)

            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')




    def netpayable(self):
        con=pymysql.connect(host='localhost',user='root',password='root123',db='pharmacy')
        cur=con.cursor()

        try:
            cur.execute(f"select AMOUNT from history_sales where RECIEPT_No=%s",(self.var_search.get(),))
            rows=cur.fetchall()
            for i in rows:
                a=a+rows
            
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')






if __name__=="__main__":
    root=Tk()
    obj=Generate(root)
    root.mainloop()