# Walrus Operator in Python

# without walrus opertatorr
         
food = list()
while True:

    item = input("What do you like?: ")
    if item == "quit":
        break
    food.append(item)
print(food)

# with Walrus Operator

foods= list()
while (food:= input("what do you like?> ")) != "quit":
    foods.append(food) 

# Output

'''

what do you like?> apple
what do you like?> banana
what do you like?> cheery
what do you like?> mango
what do you like?> quit


'''