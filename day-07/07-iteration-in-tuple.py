#nIteration in Tuple

my_tuple = ("Osama","Ali","Ahtasham",1,33,5,12)

n = len(my_tuple)
for i in range(0,n):
    print(my_tuple[i],end="  ")

#Output

'''
Osama  Ali  Ahtasham  1  33  5  12  

'''
print(my_tuple)
for ele in my_tuple:
    print(ele,end=" ")

#Output

'''
('Osama', 'Ali', 'Ahtasham', 1, 33, 5, 12)
Osama Ali Ahtasham 1 33 5 12 

'''

for index,value in enumerate (my_tuple):
    print(f"index = {index} and value = {value}")

#Output

'''
index = 0 and value = Osama
index = 1 and value = Ali
index = 2 and value = Ahtasham
index = 3 and value = 1
index = 4 and value = 33
index = 5 and value = 5
index = 6 and value = 12
   
''' 