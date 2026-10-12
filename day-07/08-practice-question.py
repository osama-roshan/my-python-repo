
# Question 1
# Given a list of marks, use list comprehension to create a new list which
# contain only the marks that are above 75

# marks = [32,89,56,74,79,77,90,86]

# new_list =[ num for num in marks if num >75]
# print(new_list)

#Output

'''

[89, 79, 77, 90, 86]

'''

# Question 2
# Given a 3X3 matrix as input, lower triangle and replace remaining with "*" 

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0,r):
#     for j in range(0,c):
#          if i >= j:
#             print(matrix[i][j],end=" ")
#          else:
#             print("*", end=" ")
#     print()

#Output

'''
1 * * 
4 5 * 
7 8 9 

'''

# Question 3
# Given a 3X3 matrix as input, upper triangle and replace remaining with "*"

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0,r):
#     for j in range(0,c):
#          if i <= j:
#             print(matrix[i][j],end=" ")
#          else:
#             print("*", end=" ")
#     print()

# Output

'''
1 2 3 
* 5 6 
* * 9 

'''

# Question 4
# Given a 3X3 matrix as input, diagional elemnts and remaining replace with "*"

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0,r):
#     for j in range(0,c):
#          if i == j:
#             print(matrix[i][j],end=" ")
#          else:
#             print("*", end=" ")
#     print()

# Output

'''
1 * * 
* 5 * 
* * 9 

'''

# Question 5
# Given a 3X3 matrix as input, diagional "*"  and remaining elements 
# lower and upper triangle 


# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0,r):
#     for j in range(0,c):
#          if i != j:
#             print(matrix[i][j],end=" ")
#          else:
#             print("*", end=" ")
#     print()

#Output

'''
* 2 3 
4 * 6 
7 8 * 

'''

# Question 6
# Given a 3X3 matrix as input, print reverse diagoal elments and remaning with "*"

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# r = len(matrix)
# c = len(matrix[0])

# for i in range(0,r):
#     for j in range(0,c):
#          if i + j == r -1 :
#             print(matrix[i][j],end=" ")
#          else:
#             print("*", end=" ")
#     print()

# Output

'''
* * 3 
* 5 * 
7 * * 

'''
#Question 7
# Given a 4X4 matrix as input, print value only on border and existing with "*"

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

r = len(matrix)
c = len(matrix[0])

for i in range(0,r):
    for j in range(0,c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()

#Output

'''

1 2 3 4 
5 * * 8 
9 * * 12 
13 14 15 16 

'''
