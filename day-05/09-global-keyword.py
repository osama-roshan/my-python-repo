# before uisng global keyword

count = 1

def xyz():
    
    count = 0
    print(f"value of count inside the function = {count}")
xyz()

print(f"value of count outside the function = {count}")


#Output before using global keyword

'''
value of count inside the function = 0
value of count outside the function = 1

'''

#after using global keyword

count = 1

def xyz():
    global count
    count = 0
    print(f"value of count inside the function = {count}")
xyz()

print(f"value of count outside the function = {count}")



#Output after using global keyword

'''
value of count inside the function = 0
value of count outside the function = 0

'''