# Exception Handling 

try:
    age = int(input("Enter your age = " ))

    if age >=18:
        print("Adult")
    else:
        print("Not Adult")
except:
    print("some error occure")


print("Done")
print("Good")

# Output

'''

Enter your age = abc
some error occure
Done
Good

'''


