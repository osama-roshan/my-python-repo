# Shallow Copy

''' this is a concept of without deep and shallow copy two varaibles but same address '''

# origional = [1,2,3]
# copy = origional
# copy.append(10)

# print(origional)
# print(copy)

# Output

'''

[1, 2, 3, 10]
[1, 2, 3, 10]

'''

''' now using of shallow copy '''

origional = [1,2,3]
copy = origional.copy()
print(id(origional))
print(id(copy))

copy.append(20)

print(origional)
print(copy)

# Output

'''

3037993411456
[1, 2, 3]
[1, 2, 3, 20]

'''