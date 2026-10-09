# Question 1 
# Write a Python program that uses a while loop to print the numbers from 1 to 10.

i = 1
while i<=10:
    print(i)
    i += 1

#Output
'''
1
2
3
4
5
6
7
8
9
10

'''

# Question 2 
# Write a Python program that uses a for loop to print the numbers from 1 to 10.

for  i in range(1,11):
    print(i)

#Output

'''
1
2
3
4
5
6
7
8
9
10

'''

# Question 3
# Write a Python program that uses a while loop to repeatedly ask the user to enter a number. Stop the loop when the user enters 0. Use the break statement to stop the loop.

i = 1
while True:
    num = int(input("Enter the Number = "))
    if num == 0:
        break
    i += 1 

#Output
'''
Enter the Number = 2
Enter the Number = 4
Enter the Number = 6
Enter the Number = 0

'''

# Question 4
# Write a Python program that uses a for loop to print the numbers from 1 to 20. Use the continue statement to skip the number 10.

for i in range (1,21):
    if i == 10:
        continue
    print(i)

#Output
'''
1
2
3
4
5
6
7
8
9
11
12
13
14
15
16
17
18
19
20

'''

# Question 5
# Write a Python program that uses a while loop to ask the user to enter numbers repeatedly. If the user enters 0, stop the loop using break. If the user enters a negative number, skip it using continue. Print all positive numbers entered by the user.

total = 0
while True:
    num = int(input("Enter the number = "))
    if num == 0:
        break
    if num < 0:
        continue
    total = total + 1
print(total)

#Output

'''
Enter the number = 4
Enter the number = 2
Enter the number = 1
Enter the number = 9
Enter the number = -223
Enter the number = -54
Enter the number = 0

'''