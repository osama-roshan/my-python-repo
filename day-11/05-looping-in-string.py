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

# Output

'''

ind = 0  and ch = p
ind = 1  and ch = r
ind = 2  and ch = o
ind = 3  and ch = g
ind = 4  and ch = r
ind = 5  and ch = a
ind = 6  and ch = m
ind = 7  and ch = m
ind = 8  and ch = i
ind = 9  and ch = n
ind = 10  and ch = g

'''