# Indexing

lst = ["Osama", "Ahtasham", "Saim","Khanghar",210,20,-33]
print(lst)
print(lst[0])
print(lst[-1])
print(lst[3])
print(lst[2])

#Output

'''
['Osama', 'Ahtasham', 'Saim', 'Khanghar', 210, 20, -33]
Osama
-33
Khanghar
Saim

'''


# Update indexing

lst = ["Osama", "Ahtasham", "Saim","Khanghar",210,20,-33]
print(f"list = {lst}")

lst[3] = "Moeed"
print(f"list = {lst}")

#Output

'''
list = ['Osama', 'Ahtasham', 'Saim', 'Khanghar', 210, 20, -33]
list = ['Osama', 'Ahtasham', 'Saim', 'Moeed', 210, 20, -33]

'''