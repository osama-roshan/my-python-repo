# Slicing list

lst = [10,20,30,40,50,60,70,80]
print(lst)

lst1 = lst [1:4]
print(lst1)
lst1 = lst [:4]
print(lst1)
lst1 = lst [4:]
print(lst1)
lst1 = lst [5:8]
print(lst1)
lst1 = lst [1:10]
print(lst1)
lst1 = lst [1:4]
print(lst1)
lst1 = lst [0:9:2]
print(lst1)
lst1 = lst [::4]
print(lst1)

#Output

'''

[10, 20, 30, 40, 50, 60, 70, 80]
[20, 30, 40]
[10, 20, 30, 40]
[50, 60, 70, 80]
[60, 70, 80]
[20, 30, 40, 50, 60, 70, 80]
[20, 30, 40]
[10, 30, 50, 70]
[10, 50]

'''

#for negative nubers

lst1 = lst [10:1:-2]
print(lst1)
lst1 = lst [5:1:-1]
print(lst1)
lst1 = lst [0:9:-2]
print(lst1)
lst1 = lst [::-4]
print(lst1)

#Output

'''
[10, 20, 30, 40, 50, 60, 70, 80]
[80, 60, 40]
[60, 50, 40, 30]
[]
[80, 40]

'''