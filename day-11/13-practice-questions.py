# Question 1

# take a string and print its first, last index and also its length 


# def print_fun(name):
#     first = name[0]
#     last = name[-1]
#     n = len(name)
#     print(f"first = {first}, last = {last}, lenght of string = {n}")

# print_fun("Osama Roshan")


# Output

'''

first = O, last = n, lenght of string = 12

'''

# Question 2 

# accept a string and print it in reverse order by using slicing

# def reverse_a_string(text):
#     return text [::-1]
# ans = reverse_a_string("Osama Roshan")
# print(ans)

# Output

'''

nahsoR amasO

'''
''

# Question 3

# Take an email print valid or invalid if it has only one @ ND ONCE .

# def check_email(email: str):
#     if email.count("@") == 1 and " . " in email:
#         return "Valid"
#     return "Invalid"
# email = "osama@gmail.com"
# print(check_email(email))

#Output

'''
valid

'''

# Question 4

# Take a phone number in formate of +92-443-3433-43 in which clear all dashes and ad also +92 code

# def clean_phonenumber(phone_number:str):
#     phone_number = phone_number.replace("-","")
#     phone_number = phone_number.replace("+92","")
#     print(phone_number)

# phone = "+92-443-3433-43"
# clean_phonenumber(phone)

# Output

'''
443343343

'''

# Question 5

# take a sentence, split it into words and print how many words start with vowels 

# def count_vowels_words(sentence:str):
#     vowels = "aeiouAEIOU"
#     count = 0
#     words = sentence.split()
#     for word in words:
#         if word[0] in vowels:
#             count+=1
#     return count
# sentence = "Osama is a student in Uol"
# print(count_vowels_words(sentence))

# Output

'''
5

'''





