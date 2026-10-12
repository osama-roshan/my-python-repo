# 4 X 5

lst = [[1,3,4,5,6],
       [4,8,9,3,2],
       [4,6,7,8,3],
       [2,3,4,8,9]
       ]

row = len(lst)
coloum = len(lst[0])

for i in range(0,row):
    for j in range(0,coloum):
        print(lst[i][j],end=" ")
    print()

#Output

'''

1 3 4 5 6 
4 8 9 3 2 
4 6 7 8 3 
2 3 4 8 9 

'''
