def add (x,y):
    return (x+y)
def sub (x,y):
    return (x-y)
def multi (x,y):
    return (x*y)
def div (x,y):
    return (x/y)

print ("1.Addition")
print ("2.Substration")
print ("3.Multiplication")
print ("4.Division")

while True:
    choice=int(input("Enter your choice: "))

    if choice in (1,2,3,4):
        try:
            n1=int(input("Enter the 1st number: "))
            n2=int(input("Enter the 2nd number: "))
        except:
            print("You enter a wrong key!,Plz enter a number..!")
            continue
        if choice==1:
            print(n1,"+",n2,"=",add(n1,n2))
        elif choice==2:
            print(n1,"-",n2,"=",sub(n1,n2))
        elif choice==3:
            print(n1,"*",n2,"=",multi(n1,n2))
        elif choice==4:
            print(n1,"/",n2,"=",div(n1,n2))
        nxt_step=input("Ïf you do next calculation(yes/no)")
        if nxt_step=="no":
            break
    else:
        print("Invalid input")
