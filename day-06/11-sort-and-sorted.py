# Sorted which only returns a new list and this is a built-in function
# not a method of list

lst = [1,1,43,3,5,77,33,36,29,88,65,90]
print(lst,id(lst))
new_list = sorted(lst)
print(f"new_list is = {new_list}",id(new_list))

#Output

'''
[1, 1, 43, 3, 5, 77, 33, 36, 29, 88, 65, 90] 2941848084480
new_list is = [1, 1, 3, 5, 29, 33, 36, 43, 65, 77, 88, 90] 2941853269248

'''

# sort is a method of list not a built-in funtion
# This is sorting the list but in the same address without
# returning new list

print(f"list is = {lst}",id(lst))

lst.sort()      #in pleace

print(f"list is = {lst}",id(lst))

#Output

'''
list is = [1, 1, 43, 3, 5, 77, 33, 36, 29, 88, 65, 90] 2880769449984
list is = [1, 1, 3, 5, 29, 33, 36, 43, 65, 77, 88, 90] 2880769449984

'''


