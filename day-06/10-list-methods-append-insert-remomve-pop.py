# List methods which is also known as functions but these functions 
# are bound and only applicalbe for List

#first one is  append

lst = [2,5,32,"Osama",20,2,"Ali",32,"khanghar"]

print(lst)
lst.append("Ahtasham")
lst.append(100)
print(lst)

#Output

'''
[2, 5, 32, 'Osama', 20, 2, 'Ali', 32, 'khanghar']
[2, 5, 32, 'Osama', 20, 2, 'Ali', 32, 'khanghar', 'Ahtasham', 100]

'''

# Insert require index and value both 

lst.insert(3,11)
lst.insert(5,"Ali")
print(lst)

#Output

'''
[2, 5, 32, 'Osama', 20, 2, 'Ali', 32, 'khanghar']
[2, 5, 32, 'Osama', 20, 2, 'Ali', 32, 'khanghar', 'Ahtasham', 100]
[2, 5, 32, 11, 'Osama', 'Ali', 20, 2, 'Ali', 32, 'khanghar', 'Ahtasham', 100]

'''

# POP by index and also remove last value by itself
lst.pop(3)
lst.pop(5)
lst.pop(6)
lst.pop(2)
print(lst)

#Output
"""
[2, 5, 'Osama', 'Ali', 2, 32, 'khanghar', 'Ahtasham', 100]

"""

# remove    # only by value

lst.remove("Osama")
lst.remove("Ali")
lst.remove(20)
lst.remove(2)
print(lst)

#Output

'''
[2, 5, 32, 'Osama', 20, 2, 'Ali', 32, 'khanghar']
[5, 32, 2, 32, 'khanghar']

'''