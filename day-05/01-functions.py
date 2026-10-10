#Queston 1
# Write a function  that ask a number from user and print if that number is odd o even


def even_odd():

    num = int(input("Enter the number ="))

    if num % 2 == 0:
        print("even")
    else:
        print("odd")


even_odd()
even_odd()

#Output

'''
Enter the number =5
odd
Enter the number =10
even

'''

# Question 2
# Write a funtion that ask a number from user that print all the factors of that number

def factor():
    num = int(input("Enter the number ="))
    for i in range (1, num+1):
        if num % i == 0:
            print (i, end=" ")
factor()


#Output

'''
Enter the number =5
1 5 

'''