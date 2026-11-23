import time

def usingwhile():
    i = 0
    while i < 50000:
        i = i + 1

def usingfor():
    for i in range(50000):
        print(i)

init = time.time()

usingfor()
t1 = time.time() - init

usingwhile()
t2 = time.time() - init

print("For loop time:", t1)
print("While loop total time:", t2)

# Ouput

'''
For loop time: 4.02527928352356
While loop total time: 4.026961088180542

'''