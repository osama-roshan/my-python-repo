# Sorting in dictionary via keys and values

# marks = {"Math": 85, "English": 90, "Bio":95, "Computer": 70}

# # by value
# ans = dict(sorted(marks.items(), key=lambda x: x[1]))
# print(ans)

# # by key
# ans = dict(sorted(marks.items(), key=lambda x: x[0]))
# print(ans)

# Output
'''

{'Computer': 70, 'Math': 85, 'English': 90, 'Bio': 95}
{'Bio': 95, 'Computer': 70, 'English': 90, 'Math': 85}


'''    


marks2 ={

    "Osama": [89,78,86,85,84 ],
    "Saim": [85,76,69,90,43],
    "Ali" : [89,78,67,84,33]
}


ans = dict(sorted(marks2.items(),key = lambda x :sum(x[1])))
print(ans)

ans = dict(sorted(marks2.items(),key = lambda x :sum(x[1]), reverse = True))
print(ans)