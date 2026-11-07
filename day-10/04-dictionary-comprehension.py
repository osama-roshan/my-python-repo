# by using normal way 
square = {}
for i in range(1,6):
    square[i] = i*i
print(square)


# By suing Comprehension method

squares = {i: i*i for i in range (1,6)}
print(squares)