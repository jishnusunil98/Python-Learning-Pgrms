name=input("Enter the name of student: ")
sub=input("Enter the name of subject: ")
mark=int(input("Enter the mark of %s: "%(sub)))
if 0<=mark<=100:
    if mark>=90<=100:
        print("Grade is A+")
    elif mark>=80<90:
        print("Grade is A")
    elif mark>=70<80:
        print("Grade is B")
    elif mark>=60<70:
        print("Grade is C")
    elif mark>=50<60:
        print("Grade is D")
    else:
        print("Grade is F")
else:
    print("Please enter a value between 0 and 100")
