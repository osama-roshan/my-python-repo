# Question 1
# Given a list of number, write python using a loop to find and print
# the largest number without using built-in funtion of max

lst = [2,4,6,79,43,-5,-34,90]

maxi = float("-inf")
for num in lst:
    if num > maxi:
        maxi = num

print(f"Maximum no = {maxi}")

#Output

'''
Maximum no = 90

'''
# Question 2
# Write a program that takes a list and a target number, use a loop
# to determine if the target number is exist in this list.
# Donot use the in operator


lst = [2,3,55,64,91,10,-4,88]
target = int(input("Enter the number = "))

found = False
for num in lst:
    if num == target:
        found = True

print(found)

#Output

'''
Enter the number = 10
True
Enter the number = 20
False

'''


# same question by usinf functions

def exist_value(value,target):

    for num in lst:
        if num == target:
            return True
    return False

lst = [2,3,55,64,91,10,-4,88]

print(exist_value(lst,10))
print(exist_value(lst,-32))
print(exist_value(lst,90))
print(exist_value(lst,55))

#Output

'''
True
False
False
True

'''

# Question 3
# Given a list of a number ,use a loop to calculate and print their 
# average, you can use len() to get the length of element, but avoid 
# using sum() to calculate their total

def let(num):
    a = len(lst)
    total = 0
    for value in lst:
        total +=  value
    return total / a

lst = [2,3,55,32,-5,73,88,90]

print(f" Average of all values sum = {let(lst)}")


#Output

'''
 Average of all values sum = 42.25

'''

#Question 4

# Given two list of same lenght, write python code using a loop to 
# create a new list where each element is the sum of corresponding 
# elements from both origional list

def new_list(lst1 ,lst2):

    new_list = []

    a = len(lst1)
    for i in range (0,a):
        total = lst1[i] + lst2[i]
        new_list.append(total)
    return new_list

lst1 = [2,4,6,55,32,19,-76,-22,90]
lst2 = [4,6,-4,30,20,-2,21,66,70]
x = new_list(lst1 , lst2)
print(x)

#Output

'''
[6, 10, 2, 85, 52, 17, -55, 44, 160]

'''

#Question 5
# Write a program that takes a list of numbers and using a loop determine
# whether it is stored in ascending order, Print Trur if is it sorted

def is_sorted(num):
    a = len(num)
    for i in range(0,a - 1):
        if num[i] > num[i + 1]:
             return False
    return True
num = [10,20,30,40,50,60,70,80,90,100]

print(is_sorted(num))

#Output

'''
True

'''

# Question 6
# Seprate a list of integer one containing all even numbers and other
# containing all odd numbers

def odd_even_lst(lst):
    even_list = []
    odd_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    print(f"Even list = {even_list}")
    print(f"Odd list = {odd_list}")

lst = [2,3,4,45,32,65,12,55,7,99]
print(lst)
print(odd_even_lst(lst))

#Output

'''
[2, 3, 4, 45, 32, 65, 12, 55, 7, 99]
Even list = [2, 4, 32, 12]
odd list = [3, 45, 65, 55, 7, 99]

'''