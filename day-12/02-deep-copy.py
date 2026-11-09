# Deep copy 

''' there is a problem in which it only work on the outer mutable vlaues'''

import copy 
origional =  [1,2,3,[4,5,6],7,8,9]
shallow = copy.copy(origional)

print(id(origional))
print(id(shallow))

shallow[3][1] = 999


print(origional)
print(shallow)

# Output

'''

2470062940352
2470065867136
[1, 2, 3, [4, 999, 6], 7, 8, 9]
[1, 2, 3, [4, 999, 6], 7, 8, 9]

'''



''' By using deepcopy '''


import copy 
origional =  [1,2,3,[4,5,6],7,8,9]
shallow = copy.deepcopy(origional)

print(id(origional))
print(id(shallow))

shallow[3][1] = 999


print(origional)
print(shallow)


# Output

'''

2088548458688
2088551516736
[1, 2, 3, [4, 5, 6], 7, 8, 9]
[1, 2, 3, [4, 999, 6], 7, 8, 9]

''' 