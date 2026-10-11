# iteration using while loop in list

lst = [10,20,30,40,50,60,70,80]
print(lst)


n= len(lst)
i = 0
while i <= n-1:
    print(lst[i])
    i += 1

#Output

'''

[10, 20, 30, 40, 50, 60, 70, 80]
[80, 60, 40]
[60, 50, 40, 30]
[]
[80, 40]

'''

# print only even numbers in this existing list by using while loop

n= len(lst)
i = 0
count = 0
while i <= n-1:
    if lst[i] % 2 == 0:
        print(lst[i])
        count += 1 
    print(lst[i])
    i += 1
print(f"Total even numbers = {count}")

#Output

'''
[10, 20, 30, 40, 50, 60, 70, 80]
10
20
30
40
50
60
70
80
Total even numbers =8

'''

i = n-1
while i>=0:
    print(lst[i])
    i -= 1

#OutPut

'''
80
70
60
50
40
30
20
10

'''