vow=0
conts=0
dig=0
wt_sp=0
sp_ch=0

st=input("Enter your sentance: ")

for i in st:
    if ((st=='a') or (st=='e') or (st=='i') or (st=='o') or (st=='u') or (st=='A') or (st=='E') or
        (st=='I') or (st=='O') or (st=='U')):
        vow=vow+1
    elif (('a'<st>='z') or ('A'<st>='Z')):
        conts=conts+1
#    elif (0<=st<=9):
#        dig=dig+1
    elif st==" ":
        wt_sp=wt_sp+1
    else:
        sp_ch=sp_ch+1

print("Total number of vowles=",vow)
print("Total number of consonats=",conts)
print("Total number of digites=",dig)
print("Total number of white space=",wt_sp)
print("Total number of special characters=",sp_ch)
