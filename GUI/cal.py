from tkinter import*
root=Tk()

root.title("Addition calculator")
root.geometry("500x500")
root.resizable(False,False)

l1=Label(root,text="Enter the 1st no. ",font=("times new roman",18),width=20).pack()
e1=Entry(root,font=("times new roman",14),width=30,bd=5)
e1.pack()
l2=Label(root,text="Enter the 2nd no. ",font=("times new roman",18),width=20).pack()
e2=Entry(root,font=("times new roman",14),width=30,bd=5)
e2.pack()
l3=Label(root,text="Result ",font=("times new roman",18),width=5).pack()

def cal():
    sum1=int(e1.get())+int(e2.get())
    res.set(sum1)

res=StringVar()
e3=Entry(root,font=("times new roman",18),width=30,bd=5,textvariable=res)
e3.pack()

b1=Button(root,text=("Find Sum"),font=("times new roman",14),padx=10,activebackground='red',activeforeground='blue',command=cal).pack()

root.mainloop()
