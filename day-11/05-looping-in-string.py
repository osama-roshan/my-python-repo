# Looping in string

text = "programming"

n = len(text)
for i in range(0,n):
    print(text[i])

# Output

'''
p
r
o
g
r
a
m
m
i
n
g


'''

# Count how many o in this string

text = "programming"

n = len(text)
total = 0
for i in range(0,n):
    if text[i]== "o" or text[i] == "0":
        total += 1
print(total)

# Output

'''

1

'''

# enumerate in string

for ind,ch in enumerate(text):
    print(f"ind = {ind}  and ch = {ch}")