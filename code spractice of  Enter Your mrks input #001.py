S1 =int(input(" Enter Your Marks of S1"))
S2 =int(input(" Enter Your Marks of S2"))
S3 =int(input(" Enter Your Marks of S3"))
S4 =int(input(" Enter Your Marks of S4"))
S5 =int(input(" Enter Your Marks of S5"))
S6 =int(input(" Enter Your Marks of S6"))
a=(((S1+S2+S3+S4+S5+S6)/600)*100)
print(a)
if a>60:
    print("Great Your Passed!")
else:
     ("Sorry, Your Failed!")