# required argument

def subjects(Eng,Math,Bio,Phy=0,Urdu=0):
    print(f"Eng marks = {Eng}")
    print(f"Math marks = {Math}")
    print(f"Bio marks = {Bio}")
    print(f"Phy marks = {Phy}")
    print(f"Urdu marks = {Urdu}")

    total_marks = Eng + Math + Bio + Phy + Urdu
    print(F"Total marks of all subjects = {total_marks}")

subjects(40,45,42,)

#output

'''

Eng marks = 40
Math marks = 45
Bio marks = 42
Phy marks = 0
Urdu marks = 0
Total marks of all subjects = 127


'''