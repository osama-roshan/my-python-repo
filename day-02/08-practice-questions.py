# Question 1 
# Write a Python program that asks the user to enter two numbers. Use arithmetic operators to calculate and print their addition, subtraction, multiplication, and division.

num1 = int(input("Enter the number 1 ="))
num2 = int(input("Enter the  number 2 ="))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#Output

'''
Enter the number 1 =20
Enter the  number 2 =10
30
10
200
2.0

'''


# #Question 2 
# #Write a Python program that asks the user to enter their age. Use a comparison operator and an if-else statement to check whether the user is 18 or older. Print an appropriate message.

age = int(input("Enter your Age = "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Output

'''
Enter your Age = 19
You are eligible to vote

'''


# #Question 3
# # Write a Python program that asks the user to enter their marks. Use if-else-if (elif) statements to display the following result:

# # 80 or above → A Grade
# # 70 to 79 → B Grade
# # 60 to 69 → C Grade
# # Below 60 → Fail

marks = int(input("Enter your Marks ="))

if marks >= 80:
    print("Grade is A")
elif marks >= 70:
    print("Grade is B")
elif marks >= 60:
    print("Grade is C")
else:
    print("Fail")

#Output
'''
Enter your Marks =81
Grade is A

'''


# # Question 4 
# # Write a Python program that asks the user to enter their age and whether they have a student ID (yes or no). Use logical operators and an if-else statement to check whether the user is eligible for a student discount.

age = int(input("Enter Your Age = "))
student_id = str(input("Do you have student_id? (Yes / NO)"))

if age <= 25 and student_id == "Yes":
    print("You are eligible for student discount")
else:
    print("You are not eligible for student discount")

#Output

'''
Enter Your Age = 19
Do you have student_id? (Yes / NO) Yes
You are not eligible for student discount
'''


# # Question 5 
# # Write a Python program that asks the user to enter their username, age, and password. Use nested if-else statements to first check the age and then check the password. If both conditions are satisfied, 
# # print that the user is allowed to log in; otherwise, 
# # print an appropriate message. Also use a ternary operator somewhere in the program.


username = str(input("Enter your username = "))
age = int(input("Enter your age = "))
password = str(input("Enter your password = "))

age_status = "Adult" if age >= 18 else "Minor"

if age >= 18:
    if password == "12345":
        print("Username:", username)
        print("Status:", age_status)
        print("You are allowed to log in")
    else:
        print("Incorrect password")

else:
    print("You must be 18 or older to log in")

#Output

'''

Enter your username = Osama
Enter your age = 19
Enter your password = 12345
Username: Osama
Status: Adult
You are allowed to log in

'''