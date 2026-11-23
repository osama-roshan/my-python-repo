# Reduce funcrion

from functools import reduce


l = [1,2,3,4,5]

def mysum(x,y):
    return x+y

sum = reduce(mysum,l)
print(sum)


#Output

'''

15

'''