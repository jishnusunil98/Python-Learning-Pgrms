amount = int(input("Enter the amount: "))

if(amount > 0):
    intrest = int(input("Enter the interst rate(in %): "))
    if(intrest > 0 and intrest < 100):
        x = amount/100
        AnnualIntrest = x*intrest

        print(amount)
        print(intrest)
        print(AnnualIntrest)
    else:
        print("You are entered a wrong intrest rate.")
else:
    print("You are enter a wrong amount.")
