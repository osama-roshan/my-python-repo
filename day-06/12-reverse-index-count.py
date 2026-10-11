# reverse the list 

lst = [1,1,43,3,5,77,33,36,29,88,65,90]
print(f"list is = {lst}",id(lst))
lst.reverse()
print(f"list is = {lst}",id(lst))

#Output

'''
list is = [1, 1, 43, 3, 5, 77, 33, 36, 29, 88, 65, 90] 2436048445440
list is = [90, 65, 88, 29, 36, 33, 77, 5, 3, 43, 1, 1] 2436048445440

'''


# index it tells the index of value in the list

lst = [1,1,43,3,5,77,33,36,29,88,65,90]
print(lst.index(3))
print(lst.index(88))
print(lst.index(5))
print(lst.index(77))

#Output

'''

3
9
4
5

'''

# Count  #It would tell us that how many times the same values
#are repeate in our existing list

lst = [1,1,43,3,5,77,33,36,29,77,88,65,90,77,1,3,5,6,33,]

print(lst.count(1))
print(lst.count(3))
print(lst.count(88))
print(lst.count(77))
print(lst.count(65))
print(lst.count(100))

#Output

'''

3
2
1
3
1
0   it would retrun 0 if the number could not exist in the list

'''