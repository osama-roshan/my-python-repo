# Question 1 
# Create a dictionary containing a student's name, age, and city.
# Remove the "age" key using pop() and print the updated dictionary.


student = {
    "name": "Osama",
    "age": 21,
    "city": "Lahore"
}

student.pop("age")

print(student)


#Output 

'''
{'name': 'Osama', 'city': 'Lahore'}

'''

# Question 2
# Create a dictionary containing three subjects and their marks.
# Ask the user to enter a subject and check whether it exists.


marks = {
    "Science": 98,
    "Bio": 95,
    "Computer": 90
}

subject = input("Enter subject: ")

if subject in marks:
    print("Subject found")
else:
    print("Subject not found")

# Output

'''
Enter subject: Bio
Subject found

Enter subject: sacience
Subject not found

'''


# Question 3

#Create a dictionary containing the names and ages of three students. 
# Print all keys using keys().


students = {
    "Osama": 21,
    "Ali": 20,
    "Ahmed": 22
}

print(students.keys())


#Output

'''
dict_keys(['Osama', 'Ali', 'Ahmed'])

'''

#Question 4

#Create a dictionary containing three subjects and their marks. 
# Print all marks using values().


marks = {
    "Science": 98,
    "Bio": 95,
    "Computer": 90
}

print(marks.values())

#Output

'''
dict_values([98, 95, 90])

'''

# Question 5

# Create a dictionary containing three products and their prices.
#  Print all key-value pairs using items().


products = {
    "Laptop": 100000,
    "Mouse": 1500,
    "Keyboard": 3000
}

print(products.items())

#Output
'''

dict_items([('Laptop', 100000), ('Mouse', 1500), ('Keyboard', 3000)])

'''