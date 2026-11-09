# Membership in string

text = "programming"

print("P" in text)
print("p" in text)
print("p" not in text)
print("ming" in text)

# Output

'''

False
True
False
True

'''

# count all vowels in this string by easy way 

total = 0
for i in text:
    if i in "aeiouAEIOU":
        total +=1
print(total)

# Output

'''
3 

'''