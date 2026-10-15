# Membership Operator

marks = { "Science" : 98, "Bio" : 95, "Computer" : 90, 55 : 100}

k = input("Enter Key = ")
if k in marks:
    print(marks[k])
else:
    print("Key Desnot Exist")

# Output

'''
Enter Key = osama 
Key Desnot Exist

Enter Key Science
98

'''