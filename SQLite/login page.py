from tkinter import *
import sqlite3
root=Tk()

root.geometry("400x400")
root.title("LOGIN PAGE")
root.config(bg="light blue")

username=StringVar()
passward=StringVar()

def login():
    user=username.get()
    pwsd=passward.get()
    conn=sqlite3.connect('logoo.bd')
    cursorobj=conn.cursor()
    cursorobj.execute("create table if not exists loginpage(USERNAME test,PASSWARD test)")
    cursorobj.execute("insert into loginpage (USERNAME,PASSWARD)values(?,?)",(user,pwsd))
    conn.commit()



l1=Label(root,text="LOGIN PAGE",font=("times new roman",16,"bold","underline"),fg="blue",bg="light blue").place(x=150,y=10)
l2=Label(root,text="User Name:",font=("times new roman",14,"bold"),fg="blue",bg="light blue").place(x=50,y=50)
l3=Label(root,text="Passward:",font=("times new roman",14,"bold"),fg="blue",bg="light blue").place(x=50,y=100)

e1=Entry(root,font=("times new roman",14,"bold"),bd=5,textvar=username).place(x=155,y=50)
e2=Entry(root,font=("times new roman",14,"bold"),bd=5,show="*",textvar=passward).place(x=155,y=100)

b1=Button(root,text="Sumit",font=("times new roman",14,"bold"),padx=10,pady=0,command=login).place(x=150,y=150)

root.mainloop()
