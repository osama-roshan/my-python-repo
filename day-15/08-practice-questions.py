# Question 1

# Write a Python program that creates a file named student.txt and writes your name, age, and university into it

f = open("student.txt", "w")

f.write("Name: Osama\n")
f.write("Age: 20\n")
f.write("University: UOL")

f.close()

# Output
'''
Name: Osama
Age: 20
University: UOL

'''


# question 2

# Write a Python program that reads and displays all the data from student.txt

f = open("student.txt", "r")

data = f.read()
print(data)

f.close()

# Output

'''
Name: Osama
Age: 20
University: UOL

'''

# Question 3

# Write a Python program that tries to open and read a file. If the file does not exist, 
# handle the error using except. Use finally to display a closing message

try:
    f = open("hello.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File not found!")

finally:
    print("Program finished.")

# Output

'''
hello world
this is a programming world
you are a good programmer 
always do your best 
be consistent
Program finished.

'''
