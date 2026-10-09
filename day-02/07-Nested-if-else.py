age = int(input("enter the age ="))
certificate = True
if age>=18:
    if certificate == True:
        print("you will be hired")
    else:
       print("Cannot hire due to no certificate")
else:
    print("cannot hire, age is less than 18")

#Output

'''
enter the age =19
you will be hired

'''
