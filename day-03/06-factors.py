# ask a number forma a user and print all factors

num = int(input("Enter the number = "))
i = 1
while i<=num:
    if num % i == 0:
        print(i)

    i += 1

#Output
'''
Enter the number = 10
1
2
5
10

'''