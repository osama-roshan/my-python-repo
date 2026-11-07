# Question 1 
# Print only top 3 subjects with the highest marks

subject = {
    "English": 87,
    "Urdu": 86,
    "Math": 80,
    "Bio": 78,
    "Computer": 75,
}

ans = sorted(subject.items(),key = lambda x:x [1], reverse = True)
result = ans [0:3]

for sub, marks in  result:
    print(f"sub = {sub} mark = {marks}")


# Output

'''
sub = English mark = 87
sub = Urdu mark = 86
sub = Math mark = 80

'''


# Question 2
# Print highest marks and then print average marks 

students = {

    "Osama": [85,84,83,78,76,80],
    "Saim": [83,78,76,89,80,87],
    "Ali": [78,88,87,76,79,80],
}
for name, mark in students.items():
    total = sum(mark)
    avg = total/ len(mark)
    print(f"{name} has scored total marks {total} and average marks {avg:.2f}")