# Question 1

 #Create a nested list and make its shallow copy. Change the value of the nested list 
 # in the copied list. Print both lists and explain why both lists change.

import copy

original = [10, 20, [30, 40], 50]
shallow = copy.copy(original)

shallow[2][0] = 999
print("Original:", original)
print("Shallow:", shallow)

# Output

'''

Original: [10, 20, [999, 40], 50]
Shallow: [10, 20, [999, 40], 50]

'''

# Question 2

# Create a nested list and make its deep copy. Change a value in the copied list. 
# Print both lists and observe the difference.

import copy

original = [1, 2, [3, 4], 5]
deep = copy.deepcopy(original)

deep[2][0] = 999
print("Original:", original)
print("Deep Copy:", deep)

# Output

'''

Original: [1, 2, [3, 4], 5]
Deep Copy: [1, 2, [999, 4], 5]

'''

# Question 3

# Create a function that takes an integer and a list as arguments.
#  Change the integer value and add a new element to the list. 
# Print the values inside and outside the function.

def update_data(number, items):
    number = 100
    items.append(40)

    print("Inside Function:", number)
    print("Inside Function:", items)


num = 10
my_list = [10, 20, 30]
update_data(num, my_list)
print("Outside Function:", num)
print("Outside Function:", my_list)

# Output

'''

Inside Function: 100
Inside Function: [10, 20, 30, 40]
Outside Function: 10

'''

# Question 4 

# Create a list and pass it to a function. First, mutate the list by adding an element. 
# Then rebind the parameter to a new list. Print the original list.

def change_list(items):

    # Mutate
    items.append(100)
    print("After Mutation:", items)

    # Rebind
    items = [7, 8, 9]
    print("After Rebinding:", items)


numbers = [1, 2, 3]
change_list(numbers)
print("Original List:", numbers)

# Output

'''

After Mutation: [1, 2, 3, 100]
After Rebinding: [7, 8, 9]
Original List: [1, 2, 3, 100]

'''

# Question 5

# Create a function named update_marks that accepts a student's name and marks using type 
# annotations. Add 5 bonus marks to the student's marks and return the updated dictionary.

def update_marks(name: str, marks: int) -> dict:

    student: dict = {
        "name": name,
        "marks": marks
    }

    student["marks"] += 5
    return student


result = update_marks("Osama", 85)
print(result)


# Output

'''

{'name': 'Osama', 'marks': 90}

'''