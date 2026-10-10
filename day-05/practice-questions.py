#Question 1
# Write the fucntion of 3 numbers and print which number is greater

def greater_no(a,b,c):
    if a>b and a>c:
        print(f"a {a}")
    elif b>a and b>c:
         print(f"b {b}")
    else:
        print(f"c {c}")

greater_no(10,100,50)

#Output
'''
b 100

'''

# Question 2

# Write a function called dicount_price that takes 
# origional_price and dicount_price as paarameter and print
# the final price after discount

def discount_price(origional_price, discount_percent):
    discount_amount = (discount_percent / 100) * origional_price
    final_price = origional_price - discount_amount
    print(f"Your final amount is Rs{final_price}")

discount_price(100,30)
discount_price(1100,30)

#Output
'''
Your final amount is Rs70.0
Your final amount is Rs770.0

'''

# Question 3
# Write a functionm called absolute_value that takes a number and return
# its absolute value without using built-in abs() function

def absolute_value(num):
    if num>=0:
        return num
    return num * -1

print(absolute_value(10))
print(absolute_value(-100))
print(absolute_value(-220))

# Output

'''
10
100
220

'''

# Question 4
# Write a lambda function which takes a number and return its cube
#store it in a variable and call it

cube =lambda num: num * num * num

print (f"The value of cube = {cube(10)}")                   
print (f"The value of cube = {cube(5)}")   
#Output

'''
The value of cube = 1000
The value of cube = 125

'''

# Question 5
# Write a lambda function that takes a number thats return "Positive" 
#or "Negative"

xyz = lambda num: "Positive" if num > 0 else "Negative"

print(xyz(-5))
print(xyz(5))

#Output

'''
Negative
Positive

'''

# Question 6

# Write a function fizzbuzz(n) that takes a simple number and print
# "frizz" if it is divisible by 3, print "Buzz" if it is divisible 
# by 5, print "Frizzbuzz" if it is divisible by both
# otherwise print the number itself

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif  num % 5 == 0:                    
        return "buzz"
    return num

print(fizzbuzz(3))
print(fizzbuzz(10))
print(fizzbuzz(7))
print(fizzbuzz(15))

#Output
'''
fizz
buzz
7
fizzbuzz

'''