# Common file operations in file handling and also using pathlib

# Create

import os
from pathlib import Path

os.mkdir("new_folder")
Path("new_folder1").mkdir()

#Remove

os.remove("new.txt")
Path("new_txt").unlink()

#Rename

os.rename("new.txt", "hello.txt")
Path("hello.txt").rename("abcd.txt")


# Pirnt all files and folder 

for f in os.listdir("."):
    print(f)

# Output

'''

01-append-mode.py
02-exclusive-mode.py
03-os-path-module.py
04-common-files-operations.py
new.txt
new_folder
new_folder1
new_txt

'''