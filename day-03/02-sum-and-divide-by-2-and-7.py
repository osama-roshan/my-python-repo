#sum of number from 1 to 100 and divided by 2 and 7

start = int(input("Enter the start number = "))
end = int(input("Enter the end numberv = "))

i = start
total = 0
while i<=end:
    if i % 2 == 0 and i % 7 == 0:
        print(i)
        total = total + i
    i += 1
print(f"total = {total}")

#Output
'''
Enter the start number = 12
Enter the end numberv = 34
14
28
total = 42

'''