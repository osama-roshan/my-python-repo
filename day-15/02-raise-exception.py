# Raise exception 

def check_age(age: int):
    if age < 0:
        raise ValueError("enter your correct age")
    elif age >= 150:
        raise ValueError("Age is not real")
    print("Your age is good")

try:
    check_age(20)
    check_age(1000)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
# Output

'''
Your age is good
raise ValueError("Age is not real")

'''
