# Multithreding code

import threading
import time

def task():
    print("this task is running\n")
    time.sleep(2)
    print("task finished\n")


print("main program start\n")
t = threading.Thread(target = task)
t.start()
print("main program end\n")

# Output

'''

main program start

main program end

this task is running

task finished

'''
