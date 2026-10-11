# usinf enumerate function in looping 
lst = [3,4,5,66,76,32,90]

for index,value in enumerate(lst):
    print(f"index = {index} and value is = {value}")
# Output

'''
index = 0 and value is = 3
index = 1 and value is = 4
index = 2 and value is = 5
index = 3 and value is = 66
index = 4 and value is = 76
index = 5 and value is = 32
index = 6 and value is = 90

'''

# if we want to print index of only even numbes

for index,value in enumerate(lst):
    if value % 2 == 0:
        print(index)

# Output

'''
1
3
4
5
6

'''