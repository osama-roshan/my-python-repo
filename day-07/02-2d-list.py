# 2D List 

lst = [[1,2,3],
       [4,5,6],
       [7,8,9],
       ]
# print(lst)     # printing list
# print(lst[0])  # printing indix of list
# print(lst[1])
# print(lst[2])

#Output

'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3]
[4, 5, 6]
[7, 8, 9] 

'''

# now using nested loop

for i in range(0,3):
    for j in range(0, 3):
        print(lst [i][j], end=" ")
    print()

#Output

'''
1 2 3 
4 5 6 
7 8 9 

'''