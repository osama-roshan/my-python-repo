# sum of 1 to 100 number

start = int(input("Enter start the number = "))
end = int(input("Enter the end number = "))

i = start
total = 0

while i<=end:
    total = total + i
    i+=1

print(f"total number = {total}")

#Output

'''
Enter start the number = 2
Enter the end number = 4
total number = 9

'''