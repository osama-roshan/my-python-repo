# This piece of code make a folder name data and in data it will create 100 folders name of date 

import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/day{i+1}")


# this rename all the folder name 

for i in range(0,100):
    os.rename(f"data/day{i+1}", f"data/tutorial {i+1}")

