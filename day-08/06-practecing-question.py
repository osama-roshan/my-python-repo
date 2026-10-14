
#Question 1

#Favourite Songs


songs = ("Song1", "Song2", "Song3", "Song4", "Song5")

print("First song:", songs[0])
print("Last song:", songs[-1])
print("Middle song:", songs[2])

#Output

'''
First song: Song1
Last song: Song5
Middle song: Song3

'''

#Question 2

# Tuple Slicing


numbers = (10, 20, 30, 40, 50, 60, 70, 80)

print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])
print("Alternate elements:", numbers[::2])

#Output

'''
First 3: (10, 20, 30)
Last 3: (60, 70, 80)
Alternate elements: (10, 30, 50, 70)

'''

# Question 3

# Take input 5 numbers in input 



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

numbers = (a, b, c, d, e)

print("Tuple:", numbers)
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))


# Output

'''
Enter first number: 67
Enter second number: 45
Enter third number: 78
Enter fourth number: 90
Enter fifth number: 32
Tuple: (67, 45, 78, 90, 32)
Minimum: 32
Maximum: 90

'''

# Question 4

# print value if i it existing in dictionary list and if not then print value
# not found

marks = { "Science" : 98, "Bio" : 95, "Computer" : 90, 55 : 100}

subjects = "Science"

ans = marks.get(subjects)

if ans is None:
    print("SUbject not found")
else:
    print(f"marks = {ans}")


# Output

'''
marks = 98
SUbject not found

'''