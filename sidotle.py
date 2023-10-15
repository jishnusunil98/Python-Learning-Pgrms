s1=int(input("Enter the 1st side of triangle: "))
s2=int(input("Enter the 2nd side of triangle: "))
s3=int(input("Enter the 3rd side of triangle: "))
if s1==s2 and s2==s3:       # CONDITION FOR EQUILATERAL TRIANGLE
    print("Its an EQUILATERAL TRIANGLE")
elif (s1==s2 and s2!=s3) or (s2==s3 and s3!=s1) or (s1==s3 and s3!=s2):     # CONDITION FOR ISOSELACE TRIANGLE
    print("Its an ISOSELACE TRIANGLE")
else:
    print("Its an SCALENE TRIANGLE")        # CONDITION FOR SCALENE TRIANGLE
