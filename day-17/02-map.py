
# Map function

def cube(x):
    return x * x * x

print(cube(2))

l = [1,2,3,4,5,6]

newl = list(map(cube,l))
print(newl)

# Output

'''

8
[1, 8, 27, 64, 125, 216]

'''