# Exclusive mode in file handling

f = open("new_txt","x") 
f.write("first_time_content")
f.close()

# that will create a new file and store value like this 

# Output

'''
first_time_content

'''