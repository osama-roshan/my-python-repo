# Pass by Value

def add_number(x):
    x = x+1
    print(f"inside value of function = {x}")


num = 10
add_number(num)
print(f"Outside vlaue of function = {num}")


# Output

'''

inside value of function = 11
Outside vlaue of function = 10

'''