 # adding and updating value

student = { "name": "Osama", "age" : 21}
print(student, id(student))

# 0utput
'''
{'name': 'Osama', 'age': 21} 2122738817664

'''

# adding

student["gender"] = "Male"

# Update

student["age"] = 19
print(student, id(student))

# Output

'''
{'name': 'Osama', 'age': 21} 2024850053760
{'name': 'Osama', 'age': 19, 'gender': 'Male'} 2024850053760

'''