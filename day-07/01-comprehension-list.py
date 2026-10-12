# Make a new list from 1 to 10 -> [1,2,3,4,5,6,7,8,9,10]

# Solve by common way

new_list = []
for i in range(1,11):
    new_list.append(i)
print(new_list)

#Output

'''

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

# Now by Comprehension list

new_list =  [i for i in range(1,11)]
print(new_list)

# Output

'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

# print 1 - 10 ,but all squares

new_list = [i * i for i in range(1,11)]
print(new_list)

#Output

'''

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''

# From 0 to 100, make a list of  all prime numbers
def is_prime(num):
    factors = 0
    for i in range(1,num + 1):
        if num % i == 0:
            factors +=1 
    if factors == 2:
        return True
    return False 

new_list = [i for i in range(1,101) if  is_prime(i) == True]
print(new_list)


#Output

'''

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

'''