from tkinter import*
from tkinter import messagebox
import sqlite3

window=Tk()
window.geometry("600x650")
window.title("Registration Form")
window.config(bg="grey")
window.resizable(False,False)
window.iconbitmap("C:/Users/USER/Desktop/PGM/python/GUI/IMAGE/registr icon.ico")


#CREATE DATABASE
name=StringVar()
phone_number=IntVar()
gmail_id=StringVar()
gender=StringVar()
language=StringVar()
state=StringVar()

def details():
    nam=name.get()
    phno=phone_number.get()
    gmid=gmail_id.get()
    gndr=v.get()
    lang=var1.get()+var2.get()+var3.get()+var4.get()
    cnty="INDIA"
    sat=c.get()
    conn=sqlite3.connect('personal _details.db')
    cursorobj=conn.cursor()
    cursorobj.execute("create table if not exists personaldetails(NAME text,CONDACT text,GMAIL_ID text,GENDER text,LANGUAGE text,COUNTARY text,STATE text)")
    cursorobj.execute("insert into personaldetails(NAME,CONDACT,GMAIL_ID,GENDER,LANGUAGE,COUNTARY,STATE)values(?,?,?,?,?,?,?)",(nam,phno,gmid,gndr,lang,cnty,sat))
    conn.commit()
    conn.close()

#CREATE MENU BAR
menu_bar=Menu(window)
window.config(menu=menu_bar)

file=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="New File")
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Save As")
file.add_command(label="Save")

edit=Menu(menu_bar,tearoff=1)
menu_bar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Undo")
edit.add_command(label="Redo")
edit.add_separator()
edit.add_command(label="Copy")
edit.add_command(label="Cut")
edit.add_command(label="Paste")


#CREATING LABELS AND ENTRY
l0=Label(window,text="REGISTRATION FORM",font=("times new roman",18,"bold","underline"),bg="grey").place(x=150,y=10)
l1=Label(window,text="Name: ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=50)
l3=Label(window,text="Phone no.: ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=100)
l4=Label(window,text="Gmail ID:  ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=150)
l5=Label(window,text="Gender ",font=("Times New Roman",16,"bold","underline"),bg="grey").place(x=50,y=200)
l6=Label(window,text="Language ",font=("Times New Roman",16,"bold","underline"),bg="grey").place(x=50,y=300)
l7=Label(window,text="Countary: ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=400)
l8=Label(window,text="INDIA ",font=("Times New Roman",14,"bold"),bg="grey").place(x=180,y=400)
l9=Label(window,text="State:  ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=450)

el=Entry(window,font=("Times New Roman",14,"bold"),bd=5,textvar=name).place(x=180,y=50)
e3=Entry(window,font=("Times New Roman",14,"bold"),bd=5,textvar=phone_number).place(x=180,y=100)
e4=Entry(window,font=("Times New Roman",14,"bold"),bd=5,textvar=gmail_id).place(x=180,y=150)


#CREATING RADIOBUTTONS
v=StringVar()
Radiobutton(window,text="Female",font=("Times New Roman",16,"bold"),bg="grey",variable=v,value="Female").place(x=50,y=250)
Radiobutton(window,text="Male",font=("Times New Roman",16,"bold"),bg="grey",variable=v,value="Male").place(x=200,y=250)



#CREATING CHEAKBUTTON
var1=StringVar()
Checkbutton(window,text="Malayalam",font=("Times New Roman",16,"bold"),bg="grey",variable=var1,onvalue="Malayalam  ",offvalue="").place(x=50,y=350)
var2=StringVar()
Checkbutton(window,text="English",font=("Times New Roman",16,"bold"),bg="grey",variable=var2,onvalue="English  ",offvalue="").place(x=190,y=350)
var3=StringVar()
Checkbutton(window,text="Hindi",font=("Times New Roman",16,"bold"),bg="grey",variable=var3,onvalue="Hindi  ",offvalue="").place(x=290,y=350)
var4=StringVar()
Checkbutton(window,text="Tamil",font=("Times New Roman",16,"bold"),bg="grey",variable=var4,onvalue="Tamil  ",offvalue="").place(x=390,y=350)


#CREATING DROPLIST
c=StringVar()
list1=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Madhya Pradesh','Manipur',
       'Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
droplist=OptionMenu(window,c,*list1)
droplist.config(font=("Times New Roman",16,"bold"),bd=5,width=20)
c.set("Select Your State")
droplist.place(x=175,y=450)


#CREATING BUTTON
b1=Button(window,text="Sumit",font=("times new roman",16,"bold"),bd=5,padx=20,activebackground="blue",activeforeground="red",command=details).place(x=250,y=520)



window.mainloop()
