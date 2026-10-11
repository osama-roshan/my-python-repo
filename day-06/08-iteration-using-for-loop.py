# itertaion using for loop in list

num = [1,4,5,67,89,5,3,9]
print(num)

n = len(num)
for i in range(0,n):
    print(num[i], end=" ")

#Output

'''
[1, 4, 5, 67, 89, 5, 3, 9]
1 4 5 67 89 5 3 9 

'''

# find the sum in this existing list whith out using built in function of sum

num = [1,4,5,67,89,5,3,9]
print(num)

n = len(num)
total = 0
for i in range(0,n):
    total = total + num[i]
    print(num[i], end=" ")
print(total)

#Output

'''
[1, 4, 5, 67, 89, 5, 3, 9]
1 4 5 67 89 5 3 9 
183

'''