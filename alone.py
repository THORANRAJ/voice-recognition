# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:53:25 2020

@author: Thoranraj
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:53:25 2020

@author: Thoranraj
"""
from tkinter import *
import random
import sqlite3
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

root=Tk()
root.geometry("500x500")
root.config(bg='aqua')
custmer_id=StringVar()
name=StringVar()
email_id=StringVar()
address=StringVar()
city=StringVar()  
nationality=StringVar()
phone_number=IntVar()
c2=IntVar()
rand=IntVar()
def database():
    custmer_id1=rand.get()
    name1=name.get()
    email_id1=email_id.get()
    address1=address.get()
    city1=city.get()
    nationality1=nationality.get()
    phone_number1=phone_number.get()
    c2.get()
   
    conn = sqlite3.connect('Form99.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute("""create table if not exists `people3`(rand int(10) primary key, name text,phone_number int(10),email_id text,address text,city text,nationality text)""")

        cursor.execute("INSERT INTO `people3`(rand, name, phone_number, email_id, address, city,nationality) values (?,?,?,?,?,?,?)",(custmer_id1,name1,phone_number1,email_id1,address1,city1,nationality1))
        messagebox.showinfo("INFORMATION","added sucessfull!!")

        #conn.commit()
        conn.commit()
def show():
    conn=sqlite3.connect('Form99.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute("select * from `people3`")
        for i in cursor.fetchall():
            print("\t",i)        
        

    
def thor1():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    options=["INDIAN","AMERICAN","UK","AUSTRALIAN","OTHERS"]
    tit1=Label(root,text="USER DETAILS",bd=1,relief="solid",font="arial 20")
    tit1.grid(row=1,column=0,padx=(5,0),pady=10)

    abc=Frame(root,bg="powder blue",bd=10,width=170,height=1000,padx=250,pady=50,relief=RIDGE)
    abc.grid(row=2,column=0,columnspan=4)
    
    q=Label(abc,text="CUSTMER ID:",bd=5,padx=12)
    q.grid(row=2,column=0)

    ew=Entry(abc,textvariable=rand)
    ew.grid(row=2,column=1)

    q1=Label(abc,text="NAME:",bd=5,padx=29)
    q1.grid(row=3,column=0)

    ew1=Entry(abc,textvariable=name)
    ew1.grid(row=3,column=1)

    q2=Label(abc,text="PHONE NUMBER:",bd=5)
    q2.grid(row=4,column=0)

    ew2=Entry(abc,textvariable=phone_number)
    ew2.grid(row=4,column=1)

    q3=Label(abc,text="EMAIL ID:",bd=5,padx=23)
    q3.grid(row=5,column=0)

    ew3=Entry(abc,textvariable=email_id)
    ew3.grid(row=5,column=1)

    q4=Label(abc,text="ADDRESS:",bd=5,padx=23)
    q4.grid(row=6,column=0)

    ew4=Entry(abc,textvariable=address)
    ew4.grid(row=6,column=1)

    q5=Label(abc,text="CITY:",bd=5,padx=35)
    q5.grid(row=7,column=0)

    ew5=Entry(abc,textvariable=city)
    ew5.grid(row=7,column=1)

    q6=Label(abc,text="NATIONALITY",bd=5,padx=11)
    q6.grid(row=8,column=0)
    

    ew6=OptionMenu(abc,nationality,*options)
    ew6.grid(row=8,column=1,padx=(10,0))

    nationality.set('select')
      
   # bu1=Button(abc,text="show",bd=8,command=show)
   # bu1.grid(row=11,column=1)


    bu2=Button(abc,text="Submit",bd=8,command=database)
    bu2.grid(row=11,column=3)

    
    bu2=Button(abc,text="Next",bd=8,command=root.destroy)
    bu2.grid(row=11,column=8)


thor1() 

root.mainloop() 


        
def thor2():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("speak something!")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print('you said:{}'.format(text))
            l=text.split()
            tree1(l)
#           
        except Exception as e:
            print(e)
            
root2 = Tk()
root2.geometry('500x500')
root2.title("voice recognition")

pdt_id=IntVar()
pdtname=StringVar()
quantity=IntVar()
price=IntVar()
#rand=IntVar()
a=IntVar()

def buy(tree):
    roo=Tk()
    roo.title("buy")
    roo.configure(background="navy blue")
    roo.geometry("300x300")
    w=Label(roo,text="quantity",bd=8,padx=2)
    w.grid(row=3,column=0)

    e=Entry(roo,textvariable=a)
    e.grid(row=3,column=1)
    
    pdt_id=tree.focus()
    ty=tree.item(pdt_id)
    pid=ty['values'][0]
    def dd():
        ap=e.get()
        top=Toplevel()
        w=Label(top,text="price",bd=8,padx=2)
        w.grid(row=1,column=0)
        y=Label(top,text="quantity",bd=8,padx=2)
        y.grid(row=2,column=0)
        pr=IntVar()
        
        pr.set(ty['values'][3]*int(ap))
        e2=Entry(top,textvariable=pr,state='disabled')
        e2.grid(row=1,column=1)
        e1=Entry(top)
        e1.insert(END,str(ap))
        e1.config(state='disabled')
        e1.grid(row=2,column=1)
        def confirm():
            try:
                if int(ty['values'][2]) < int(ap):
                    raise Exception("Insufficient quantity")
                connt=sqlite3.connect("Form99.db")
                cursor = connt.cursor()
                str1 = "update `pdttab` set quantity = quantity - " + str(ap) + " where pdt_id = " +str(pid)
                print(ap,pid)
                cursor.execute(str1)
                connt.commit()
                connt.close()
                #cursor.execute("update 'pdttab' set quantity=quantity-? where pdt_id=?",(str(ap),str(pid)))
            except Exception  as e:
                 messagebox.showinfo("INFORMATION",e)

                #print(e)
            top.withdraw()
        bu1=Button(top,text="confirm",bd=8,command=confirm)
        bu1.grid(row=3,column=1)
        roo.withdraw()
        
    b1=Button(roo,text="buy",bd=8,command=dd)
    b1.grid(row=5,column=0)
def tree1(l):
    top=Toplevel()
    #top.configure(bg="blue")
    connt=sqlite3.connect("Form99.db")
    cursor = connt.cursor()
    cursor.execute("select distinct pdt_id, pdtname,quantity,price from `pdttab` where pdtname='%s'"%l[0])
    tree=ttk.Treeview(top, column=("column1", "column2","column3","column4"), show='headings')
    tree.heading("#1", text="PRODUCT ID")
    tree.heading("#2", text="PRODUCT NAME")
    tree.heading("#3", text="QUANTITY")
    tree.heading("#4", text="PRICE")
    tree.grid(row=0,column=1)
    for row1 in cursor.fetchall():
        tree.insert("", tk.END, values=row1)
    cursor.close()  
    def delete():
        buy(tree)
        top.withdraw()
    bu1=Button(top,text="order",bd=8,command=delete)
    bu1.grid(row=2,column=6)
def database1():
    pdt_id1=pdt_id.get()
    pdtname1=pdtname.get()
    quantity1=quantity.get()
    price1=price.get()
    conn = sqlite3.connect('Form99.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute("""create table if not exists `pdttab`(pdt_id int(10), pdtname text,quantity int(10),price int(10))""")
        conn.commit()
        
def show11():
    conn=sqlite3.connect('Form99.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute("select * from `pdttab`")
        for i in cursor.fetchall():
            print("\t",i)
                            
def voice():
   
    #options=["INDIAN","AMERICAN","UK","AUSTRALIAN","OTHERS"]
    tit1=Label(root2,text="PRODUCT SEARCH ENGINE",bd=1,relief="solid",font="arial 20")
    tit1.grid(row=1,column=0,padx=(5,0),pady=10)
    abc=Frame(root2,bg="powder blue",bd=10,width=170,height=1000,padx=250,pady=50,relief=RIDGE)
    abc.grid(row=2,column=0,columnspan=4)
    
    q=Label(abc,text="SPEAK SOMETHING:",bd=5,padx=12)
    q.grid(row=2,column=0)
    ew=Entry(abc)
    ew.grid(row=2,column=1)
   
    bu1=Button(abc,text="search",bd=8,command=thor2)
    bu1.grid(row=11,column=1)
    #show11()

voice()

root2.mainloop()
