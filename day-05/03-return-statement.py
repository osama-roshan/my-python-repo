# Question 1
# Write a function that print sum of 3 numbers but using return statemnet

def add(n1,n2,n3):
    return n1 + n2 + n3

x= add(10,20,30)
print(x)

print(add(20,40,50))


#output
'''
60
110

'''

# Question 2
# True and Flase return, if usr can vote or not 

def can_vote(age):
    if age>=18:
        return True
    else:
        return False

vote=can_vote(19)
print(vote)

print(can_vote(15))


#Output

'''

True
False

'''