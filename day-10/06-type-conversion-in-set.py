# Type conversion in set

# Set to list

my_set = {2,3,4,55,5,55,55,90,89,90,89,32,45}
print(list(my_set))


#  remove duplicate in list by using set 
my_list = [2,3,4,55,5,55,55,90,89,90,89,32,45 ]
print(list(set(my_list)))


#Output

'''

[32, 2, 3, 4, 5, 45, 55, 89, 90]
[32, 2, 3, 4, 5, 45, 55, 89, 90]

'''