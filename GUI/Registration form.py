from tkinter import*
from tkinter import messagebox

window=Tk()
window.geometry("600x700")
window.config(bg="grey")
window.resizable(False,False)
window.iconbitmap("C:/Users/USER/Desktop/PGM/python/GUI/IMAGE/registr icon.ico")


#CREAT MENU BAR
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


#CREATING LABELS
l0=Label(window,text="REGISTRATION FORM",font=("times new roman",18,"bold","underline"),bg="grey").place(x=150,y=10)
l1=Label(window,text=" First Name: ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=50)
el=Entry(window,font=("Times New Roman",14,"bold"),bd=5).place(x=180,y=50)
l2=Label(window,text="Last Name: ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=100)
e2=Entry(window,font=("Times New Roman",14,"bold"),bd=5).place(x=180,y=100)
l3=Label(window,text="Phone no.: ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=150)
e3=Entry(window,font=("Times New Roman",14,"bold"),bd=5).place(x=180,y=150)
l4=Label(window,text="Gmail ID:  ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=200)
e4=Entry(window,font=("Times New Roman",14,"bold"),bd=5).place(x=180,y=200)
l5=Label(window,text="Gender ",font=("Times New Roman",16,"bold","underline"),bg="grey").place(x=50,y=250)
l6=Label(window,text="Language ",font=("Times New Roman",16,"bold","underline"),bg="grey").place(x=50,y=350)
l7=Label(window,text="Countary: ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=450)
l8=Label(window,text="INDIA ",font=("Times New Roman",14,"bold"),bg="grey").place(x=180,y=450)
l9=Label(window,text="State:  ",font=("Times New Roman",16,"bold"),bg="grey").place(x=50,y=500)


#CREATING RADIOBUTTONS
v=IntVar()
Radiobutton(window,text="Female",font=("Times New Roman",16,"bold"),bg="grey",variable=v,value=1).place(x=50,y=300)
Radiobutton(window,text="Male",font=("Times New Roman",16,"bold"),bg="grey",variable=v,value=2).place(x=200,y=300)


#CREATING CHEAKBUTTON
var1=IntVar()
Checkbutton(window,text="Malayalam",font=("Times New Roman",16,"bold"),bg="grey",variable=var1).place(x=50,y=400)
var2=IntVar()
Checkbutton(window,text="English",font=("Times New Roman",16,"bold"),bg="grey",variable=var2).place(x=190,y=400)
var3=IntVar()
Checkbutton(window,text="Hindi",font=("Times New Roman",16,"bold"),bg="grey",variable=var3).place(x=290,y=400)
var4=IntVar()
Checkbutton(window,text="Tamil",font=("Times New Roman",16,"bold"),bg="grey",variable=var4).place(x=390,y=400)


#CREATING DROPLIST
c=StringVar()
list1=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Madhya Pradesh','Manipur',
       'Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
droplist=OptionMenu(window,c,*list1)
droplist.config(font=("Times New Roman",16,"bold"),bd=5,width=20)
c.set("Select Your State")
droplist.place(x=175,y=500)


#CREATING BUTTON
b1=Button(window,text="Sumit",font=("times new roman",16,"bold"),bd=5,padx=20,activebackground="blue",activeforeground="red").place(x=250,y=570)



window.mainloop()
