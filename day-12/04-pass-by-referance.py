# pass by reference
import copy

def add_item(x):
    x= copy.deepcopy(x)
    x.append(10)
    print(f"inside the function = {x}")


nums = [1,2,3,4]
add_item(nums)
print(f"outside the funcction = {nums}")

#Output

'''

inside the function = [1, 2, 3, 4, 10]
outside the funcction = [1, 2, 3, 4]

''' 