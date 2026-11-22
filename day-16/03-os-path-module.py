# OS path module in python


import os

print(os.path.exists("my folder"))
print(os.path.isfile("new.txt"))
print(os.path.isdir("document"))
print(os.path.getsize("new_txt"))

path = (os.path.join("data","logs","apps.log"))
print(path)


# Output

'''
False
True
False
18
data \\ logs \\ apps.log

'''

# there is one slach in data \ log\ apps.log output