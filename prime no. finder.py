x=int(input("Enter your lowest number: "))
y=int(input("Enter your highest number: "))

print("Prime number between {} and {} are: ".format(x,y))

for num in range(x,y+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
