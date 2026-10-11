# sorted new list 
# This sorted funcrion is also a built-in funtion is list

marks = [ 40,39,58,72,84,90]
#print(marks) 

#sorted funtion

new_list = sorted(marks)
print(f"New sorted list = {new_list}")
print(f"Old list of marks = {marks}")

#Output

'''

New sorted list = [39, 40, 58, 72, 84, 90]
Old list of marks = [40, 39, 58, 72, 84, 90]

'''

# If you want to print list in desending order in sorted way 

new_list = sorted(marks, reverse = True)
print(f"New sorted list in desending order = {new_list}")

#Output

'''
New sorted list = [39, 40, 58, 72, 84, 90]
Old list of marks = [40, 39, 58, 72, 84, 90]
New sorted list in desending order = [90, 84, 72, 58, 40, 39]

'''