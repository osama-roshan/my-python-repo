# break and continue usinf loops


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
Enter the number = 1
Enter the number = 2
Enter the number = 3
Enter the number = 0

'''
