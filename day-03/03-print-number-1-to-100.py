# 1 to 100 diplay only divided by 3 and 5 only

start = int(input("Enter the start number = "))
end = int(input("Enter the end number ="))

i = start

while i <= end:
    if i % 3 == 0 and i % 5 == 0:
        print( i )

    i+=1


#Output

'''
Enter the start number = 2
Enter the end number = 24
15

'''