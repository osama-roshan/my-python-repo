# "remove"  it removes a specific number form list and also by user input
# "clear" it will just make all your existing list empthy 

lst = [1,1,43,3,5,77,33,36,29,88,65,90]

lst.clear()
print(lst)

#Output

'''
[]

'''

# ask the number from user now 

lst = [1,1,43,3,5,77,33,36,29,88,65,90]

target = int(input("Enter the num = "))

if target in lst:
    lst.remove(target)
    print(f"lst = {lst}")
else:
    print("Target  dees not exist in list, cannot remove it")

#Output

'''
Enter the num = 29
lst = [1, 1, 43, 3, 5, 77, 33, 36, 88, 65, 90]

Enter the num = 100
Target  dees not exist in list, cannot remove it

'''

# in and not in

#Write a Python program to check whether "Apple" exists in a list 
# using in and not in. Print the results.


fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Apple" in fruits)
print("Apple" not in fruits)


#Output

'''
True
False

'''