# default argument

def subjects(Eng,Math,Bio,Phy,Urdu):
    print(f"Eng marks = {Eng}")
    print(f"Math marks = {Math}")
    print(f"Bio marks = {Bio}")
    print(f"Phy marks = {Phy}")
    print(f"Urdu marks = {Urdu}")

    total_marks = Eng + Math + Bio + Phy + Urdu
    print(F"Total marks of all subjects = {total_marks}")

subjects(40,45,42,38,48)

#Output

'''

Eng marks = 40
Math marks = 45
Bio marks = 42
Phy marks = 38
Urdu marks = 48
Total marks of all subjects = 213


'''
    

