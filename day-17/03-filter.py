# filter function


l = [1,2,3,4,6,8]

def filter_function(x):
    return x>4

newl = list(filter(filter_function,l))
print(newl)


# Output

'''

[6, 8]

'''
