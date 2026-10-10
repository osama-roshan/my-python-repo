#Question 1
# 3 int as parameter, print parameter

def parameter_argument(a,b,c):
    num = a+b+c
    print(f"sum of {num}")

parameter_argument(10,20,30)

#Output

''''
sum of 60

'''

#Question 2
# Ask name, age gender and print

def greet(name,age,gender):
    print(f"Hi {name} your age is {age} and your gender is {gender}")

greet("osama",19,"Male")

#Output

'''
Hi osama your age is 19 and your gender is Male

'''

# If you want input from user 

def greet(name,age,gender):
    print(f"Hi {name} your age is {age} and your gender is {gender}")

a = input("Enter the Name = ")
b = int(input("Enter the age = "))
c = input("Enter your gender = ")

greet(a,b,c)

#Output

'''
Enter the Name = osama
Enter the age = 19
Enter your gender = Male
Hi osama your age is 19 and your gender is Male


'''
