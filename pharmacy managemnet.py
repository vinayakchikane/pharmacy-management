from tkinter import *
from tkinter import Tk, Label, StringVar, IntVar, GROOVE, Entry, Frame, LabelFrame, Text, Scrollbar, Button, messagebox
import tkinter
import sqlite3
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random


#bg image
window = Tk()
window.title("pharmacy management")
window.geometry('600x900')
#image_path=PhotoImage(file=r"C:\Users\rohit\OneDrive\Pictures\Screenshot 2023-12-01 214728 955.png")
#bg_image=tkinter.Label(window,image=image_path)
#bg_image.place(relheight=1,relwidth=1)
text_label=tkinter.Label(window,text="Welcome to the store",fg="darkgreen",font=('Georgia',24,'bold'))
text_label.pack()


def insert():
    a = a1.get();
    b = b1.get();
    c = c1.get();
    d = d1.get();
    e = e1.get();
    f = f1.get();
    g = g1.get();
    h = h1.get();
    


    if(a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h==""):
        messagebox.showinfo("Insert status","All Fields are required")
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="pharma")
        mycursor = mydb.cursor()
        mycursor.execute("insert into pharmaco values('"+ a +"','"+ b +"','"+ c +"','"+ d +"','"+ e +"','"+ f +"','"+ g +"','"+ h +"')")
        mycursor.execute("commit");
       
        
        
        messagebox.showinfo("Insert status","Inserted Succesfully");
        mydb.close();


def delete():
    if(a1.get() == "" ):
        messagebox.showinfo("Delete status","company is compulsory for remove")
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="pharma")
        mycursor = mydb.cursor()
        mycursor.execute("delete from pharmaco where company='"+a1.get() +"'")
        mycursor.execute("commit");        
        
        
        messagebox.showinfo("Delete status","removed Succesfully");
        mydb.close();
def search_company():
    if(a1.get() == "" ):
        messagebox.showinfo("search status","company is compulsory for search")
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="pharma")
        mycursor = mydb.cursor()
        a = a1.get()
        mycursor.execute("SELECT * FROM pharmaco WHERE company = %s", (a,))
        #mycursor.execute("SELECT * FROM pharmaco WHERE company = ?")
        rows = mycursor.fetchall()
        if len(rows) != 0:
                # Clear existing data in the table
                for item in medname_table.get_children():
                    medname_table.delete(item)
                
                for i in rows:
                    # Insert retrieved data into the treeview
                    medname_table.insert("", END, values=i)
                    
                messagebox.showinfo("Search status", "Search successful")
        else:
                messagebox.showinfo("Search status", "No data found for the given company")
            
        mydb.commit()
        mydb.close()
def search_uses():
    search_text = i1.get()

    if search_text == "":
        messagebox.showinfo("Search status", "Please enter a disease for search")
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="loop", database="pharma")
        mycursor = mydb.cursor()
        search_query = "SELECT medicine, price FROM pharmaco WHERE uses LIKE %s"
        mycursor.execute(search_query, ('%' + search_text + '%',))
        rows = mycursor.fetchall()

        # Clear existing data in the table
        for item in medicine_table.get_children():
            medicine_table.delete(item)

        if len(rows) != 0:
            for row in rows:
                # Insert retrieved data into the treeview
                medicine_table.insert("", END, values=row)
            messagebox.showinfo("Search status", "Search successful")
        else:
            messagebox.showinfo("Search status", "No medicine found for the given disease")

        mydb.close()

    
   


    
    
#variable






    

c_name=StringVar()
c_phone=StringVar()
Item=StringVar()
Rate=IntVar()
Quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))


def open_reciept():
    root=Tk()
    root.title("bill slip")
    root.geometry('1280x720')
    bg_color='#4D0039'
    #global Item, Rate, Quantity, l 

    title=Label(root,pady=2,text="Bill Generation",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
    title.pack(fill=X)
    c_name=StringVar()
    c_phone=StringVar()
    Item=StringVar()
    #Rate=Intvar()
    Quantity=IntVar()
    bill_no=StringVar()
    x=random.randint(1000,9999)
    bill_no.set(str(x))
    #global textarea, item, Rate, quantity, l 
    global l
    l=[]
    global textarea
    result_var = StringVar()
    def additm():
        #rate =  int(rate_txt.get())
        m = rate_txt.get()
        try:
        # Convert the quantity value to an integer
            quantity = int(quantity_txt.get())
            n = quantity * int(m)
            l.append(n)
            result_var.set(f"Result: {n}")

            if itm_txt.get() != '':
                textarea.insert((10.0 + float(len(l) - 1)), f"{itm_txt.get()}\t\t{quantity}\t\t{n}\n")
                #print(f"Quantity: {quantity}, Rate: {m}")
            else:
                messagebox.showerror('Error', 'Please enter item')

        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid quantity (numeric value)')

    
               


    def gbill():
            cname_lbl=Label(F1,text='Customer Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
            cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

            cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
            cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

            #cname_lbl =cname_txt()
            #cphone_lbl = cphone_txt()
            
            global textarea
            if cname_txt == "" or cphone_txt == "":
                messagebox.showerror("Error", "Customer detail are must")
            else:
                textAreaText = textarea.get(10.0,(10.0+float(len(l))))
                welcome()
                textarea.insert(END, textAreaText)
                textarea.insert(END, f"\n=========================================")
                textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(l)}")
                textarea.insert(END, f"\n\n=========================================")
                save_bill(root)

    def clear():
        global textarea

        c_name.set('')
        c_phone.set('')
        Item.set('')
        Rate.set(0)
        Quantity.set(0)

        # Clear the content of the Entry widgets
        itm_txt.delete(0, END)
        quantity_txt.delete(0, END)
        rate_txt.delete(0, END)

        # Clear the content of the textarea
        textarea.delete(10.0, END)

        welcome()


            
    def save_bill(root):
            global textarea
            
            op=messagebox.askyesno("Save bill","Do you want t o save the Bill?",parent=root)
    
            if op>0:
                bill_details=textarea.get('1.0',END)
                f1=open("bills/"+str(bill_no.get())+".txt","w")
                f1.write(bill_details)
                f1.close()
                messagebox.showinfo("Saved",f"Bill no, :{bill_no.get()} Saved Successfully",parent=root)
            else:
                return

    def welcome():
        global textarea
        cname_lbl = Label(F1, text='Customer Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)

        cname_txt = Entry(F1, width=15, textvariable=c_name, font='arial 15 bold', relief=SUNKEN, bd=7)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone No. ', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        cphone_lbl.grid(row=0, column=2, padx=20, pady=5)

        cphone_txt = Entry(F1, width=15, font='arial 15 bold', textvariable=c_phone, relief=SUNKEN, bd=7)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        textarea.delete(1.0, END)
        textarea.insert(END, "\t  INVOICE")
        textarea.insert(END, f"\n\nBill Number:\t\t{bill_no.get()}")
        
        # Use c_name.get() and c_phone.get() instead of cname_txt.get() and cphone_txt.get()
        textarea.insert(END, f"\nCustomer Name:\t\t{cname_txt.get()}")
        textarea.insert(END, f"\nPhone Number:\t\t{cphone_txt.get()}")
        
        textarea.insert(END, f"\n\n=========================================")
        textarea.insert(END, "\nProduct\t\tQTY\t\tPrice")
        textarea.insert(END, f"\n=========================================\n")
        textarea.configure(font='Georgia 12 bold')

    #=================Product Frames=================
    F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
    F1.place(x=0,y=80,relwidth=1)

    cname_lbl=Label(F1,text='Customer Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
    cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

    cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
    cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

    F2 = LabelFrame(root, text='Product Details', font=('times new roman', 18, 'bold'), fg='gold', bg=bg_color)
    F2.place(x=20, y=180, width=630, height=500)

    itm = Label(F2, text='Product Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
        row=0, column=0, padx=30, pady=20)
    itm_txt = Entry(F2, width=20, textvariable=Item, font='arial 15 bold', relief='sunken', bd=7)
    itm_txt.grid(row=0, column=1, padx=10, pady=20)

    quantity = Label(F2, text='Product quantity', font=('times new roman', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
        row=1, column=0, padx=30, pady=20)
    quantity_txt = Entry(F2, width=20, textvariable=Quantity, font='arial 15 bold', relief='sunken', bd=7)
    quantity_txt.grid(row=1, column=1, padx=10, pady=20)

    rate = Label(F2, text='Product price', font=('times new roman', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(
        row=2, column=0, padx=30, pady=20)
    rate_txt = Entry(F2, width=20, textvariable=Rate, font='arial 15 bold', relief='sunken', bd=7)
    rate_txt.grid(row=2, column=1, padx=10, pady=20)
    itm_txt.configure(state='normal')
    rate_txt.configure(state='normal')
    quantity_txt.configure(state='normal')
    itm_txt.focus_set()
    rate_txt.focus_set()
    quantity_txt.focus_set()



    #========================Bill area================
    F3=Frame(root,relief=GROOVE,bd=10)
    F3.place(x=700,y=180,width=500,height=500)
    

    bill_title=Label(F3,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
    scrol_y=Scrollbar(F3,orient=VERTICAL)
    textarea=Text(F3,yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    welcome()
    #=========================Buttons======================
    
    
    btn1=Button(F2,text='Add item',font='arial 15 bold',command=additm,padx=5,pady=10,bg='lime',width=15)
    btn1.grid(row=3,column=0,padx=10,pady=30)
    btn2=Button(F2,text='Generate Bill',font='arial 15 bold',command=gbill,padx=5,pady=10,bg='lime',width=15)
    btn2.grid(row=3,column=1,padx=10,pady=30)
    btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='lime',width=15)
    btn3.grid(row=4,column=0,padx=10,pady=30)
    


    root.mainloop()
    


    
    



#frame code
Framedeatils=Frame(window,bd=15,relief=RIDGE)
Framedeatils.place(x=2,y=60,width=700,height=400)
label = tkinter.Label(window, text="Medicine Record:", fg="darkgreen", font=('Georgia', 18, 'bold'))
label.place(x=50,y=90)
Framesecond=Frame(window,bd=15,relief=RIDGE)
Framesecond.place(x=670,y=60,width=700,height=400)
side_frame=Frame(Framesecond,bd=4,relief=RIDGE,bg="white")
side_frame.place(x=30,y=180,width=500,height=180)
sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
sc_y.pack(side=RIGHT,fill=Y)
Framelast=Frame(window,bd=15,relief=RIDGE)
Framelast.place(x=2,y=450,width=1360,height=250)
sc_x=ttk.Scrollbar(Framelast,orient=HORIZONTAL)
sc_x.pack(side=BOTTOM,fill=X)

medname_table=ttk.Treeview(Framelast,column=("company","medicine name","manufacture date","expiry date","price","type of medicine","uses","product quantity"),xscrollcommand=sc_x.set)
sc_x.config(command=medname_table.xview)
#medname table
medname_table.heading("company",text="company")
medname_table.heading("medicine name",text="medicine name")
medname_table.heading("manufacture date",text="manufacture date")
medname_table.heading("expiry date",text="expiry date")
medname_table.heading("price",text="price")
medname_table.heading("type of medicine",text="type of medicine")
medname_table.heading("uses",text="uses")
medname_table.heading("product quantity",text="product quantity")
medname_table["show"]="headings"
medname_table.pack(fill=BOTH,expand=1)
medname_table.column("company",width=100)
medname_table.column("medicine name",width=100)
medname_table.column("manufacture date",width=100)
medname_table.column("expiry date",width=100)
medname_table.column("price",width=100)
medname_table.column("type of medicine",width=100)
medname_table.column("uses",width=100)
medname_table.column("product quantity",width=100)
#medicine table
medicine_table=ttk.Treeview(side_frame,column=("medicine name","price"),yscrollcommand=sc_y.set)
sc_y.config(command=medicine_table.yview)
medicine_table.heading("medicine name",text="medicine name")
medicine_table.heading("price",text="price")
medicine_table["show"]="headings"
medicine_table.pack(fill=BOTH,expand=1)
medicine_table.column("medicine name",width=100)
medicine_table.column("price",width=100)
label = tkinter.Label(window, text="Search The Medicine Accoding to Disease", fg="darkgreen", font=('Georgia', 18, 'bold'))
label.place(x=700,y=90)
i = Label(window ,text = "Disease:",font=('Georgia',12))
i.place(x=700,y=150)
i1 = Entry(window)
i1.place(x=800,y=150)
search = Button(window, text="Get The Medicine", font=("Georgia", 12), bg="red", command=search_uses)
search.place(x=700,y=200)
reciept = Button(Framelast, text="Reciept", font=("Georgia", 12), bg="red", command=open_reciept)
reciept.place(x=1200,y=150)


#code for label
a = Label(window ,text = "Company:",font=('Georgia',12))
a.place(x=50,y=150)
a1 = Entry(window)
a1.place(x=230,y=150)
b = Label(window ,text = "Medicine Name:",font=('Georgia',12))
b.place(x=50,y=180)
b1 = Entry(window)
b1.place(x=230,y=180)
c = Label(window ,text = "Manufacture date:",font=('Georgia',12))
c.place(x=50,y=210)
c1 = Entry(window)
c1.place(x=230,y=210)
d = Label(window ,text = "Expiry date:",font=('Georgia',12))
d.place(x=50,y=240)
d1 = Entry(window)
d1.place(x=230,y=240)
e = Label(window ,text = "Price:",font=('Georgia',12))
e.place(x=50,y=270)
e1 = Entry(window)
e1.place(x=230,y=270)
f = Label(window ,text = "Type Of Medicine:",font=('Georgia',12))
f.place(x=50,y=300)
f1 = Entry(window)
f1.place(x=230,y=300)
options = ['Liquid', 'Tablet','Drop','Capsule','Injection','Cream']
f1 = ttk.Combobox(window, values=options, font=('Georgia',8))
f1.place(x=230,y=300)
f1.set(options[0])# Set the default value
#combobox.bind("<<ComboboxSelected>>", on_combobox_selected)
g = Label(window ,text = "Uses:",font=('Georgia',12))
g.place(x=50,y=330)
g1 = Entry(window)
g1.place(x=230,y=330)
h = Label(window ,text = "Product Quantity:",font=('Georgia',12))
h.place(x=50,y=360)
h1 = Entry(window)
h1.place(x=230,y=360)





#code for button
insert = Button(window, text="Insert", font=("Georgia", 12), bg="red", command=insert)
insert.place(x=50,y=400)
delete = Button(window, text="Remove", font=("Georgia", 12), bg="red", command=delete)
delete.place(x=150,y=400)
search = Button(window, text="Search By Company Name", font=("Georgia", 12), bg="red", command=search_company)
search.place(x=270,y=400)


window.mainloop()

