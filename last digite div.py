x=int(input("Enter a number: "))
y=x%10
print("The last digite:",y)
if y%3==0:
    print("%d is DIVISIBLE by 3"%(y))
else:
     print("%d is NOT DIVISIBLE by 3"%(y))
