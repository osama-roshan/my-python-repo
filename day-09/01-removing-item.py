# Removing item using three methods

student = { "name": "Osama", "age" : 21}
print(student, id(student))


# First Method Pop

student.pop("name")
print(student)

#Second Method Clear
student = { "name": "Osama", "age" : 21}
student.clear()
print(student)

# Third Method Del
student = { "name": "Osama", "age" : 21}
del student["name"]
print(student)

#Output

'''
{'name': 'Osama', 'age': 21} 2466890898112
{'age': 21}
{}
{'age': 21}

'''