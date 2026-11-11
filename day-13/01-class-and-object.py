# Class and object in Python oops concept

class student:
    name = ""
    age = 0
    gender = ""
    rollno = 0

    def set_details(self, n: str,a:int,g:str,r:int):

        self.name = n
        self.age = a
        self.gender = g
        self.rollno = r

    def display_detaills(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")
        print(f"rollno = {self.rollno}")


student1 = student()
student1.set_details("Osama",19,"male",21)
student1.display_detaills()


# Output

'''

name = Osama
age = 19 
gender = male
rollno = 21

'''
