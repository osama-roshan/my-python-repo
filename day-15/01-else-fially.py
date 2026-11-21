# Else and finally in exception handling

try:
    num = int(input("Enter the number = "))
    result = 100/num

except ValueError:
    print("This is not a valid number")

except ZeroDivisionError:
    print("You cant divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Calcuulation attempt complete")

# Output

'''
Enter the number = 0
You cant divide by zero
Calcuulation attempt complete

'''

