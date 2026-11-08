# by using normal way 
square = {}
for i in range(1,6):
    square[i] = i*i
print(square)


# By suing Comprehension method

squares = {i: i*i for i in range (1,6)}
print(squares)


#Output

'''

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''