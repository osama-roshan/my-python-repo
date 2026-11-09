# by using mutate

# we change, append or  update values in address 

def mutate_value(x):
    x[0] = 100
    print(f"inside the function = {x}")

num = [1,2,3]
mutate_value(num)
print(f"outside function = {num}")

# Output

'''

inside the function = [100, 2, 3]
outside function = [100, 2, 3]

''' 

