# Constructor in OOPS

class student:
    def __init__(self, n: str,a:int,g:str,r:int) -> None:
            self.name = n
            self.age = a
            self.gender = g
            self.rollno = r

    def display_detaills(self):
            print(f"name = {self.name}")
            print(f"age = {self.age}")
            print(f"gender = {self.gender}")
            print(f"rollno = {self.rollno}")



student1 = student("Osama",19,"male",21)
student1.display_detaills()

# Output


'''

name = Osama
age = 19
gender = male
rollno = 21

'''