name=input("Enter the name of student: ")
tol_at=int(input("Enter the total days of class: "))
tol_std_attd=int(input("Enter the day {} atttented the class: ".format(name)))
x=tol_std_attd/tol_at
y=x*100
if y>=75:
    print("{} is eligible for attend the exam".format(name))
    print("{} has {} percentage of attance".format(name,y))
else:
     print("{} is not eligible for attend the exam".format(name))
     print("{} have only {} percentage of attance".format(name,y))
