# by using rebind

# rebind mean by using "=" operator we create new list or mutable value or object 
# thats why both values are differnet in output


def rebind_value(x):
    x = [10,20,30]
    print(f"inside the function = {x}")

num = [1,2,3]
rebind_value(num)
print(f"outside function = {num}")


# Output

'''

inside the function = [10, 20, 30]
outside function = [1, 2, 3]

'''