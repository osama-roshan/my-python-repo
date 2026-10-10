# if user is greater than 18 print true and if not then false
# only simple without lambda function

def age(num):
    if num >=18:
        return True
    return False 

print(age(18))
print(age(12))

#Output

'''
True
False

'''

# Now Using lmabda Function

age = lambda num: True if num >= 18 else False

print(age(19))
print(age(12))

#Output

'''
True
False

'''