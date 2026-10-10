# Positioal argument

# In positional argument sequesnce does not matter while 
# passing arguments

def subjects(Eng,Math,Bio,Phy,Urdu):
    print(f"Eng marks = {Eng}")
    print(f"Math marks = {Math}")
    print(f"Bio marks = {Bio}")
    print(f"Phy marks = {Phy}")
    print(f"Urdu marks = {Urdu}")

    total_marks = Eng + Math + Bio + Phy + Urdu
    print(F"Total marks of all subjects = {total_marks}")

subjects(Urdu=48,Math=41,Eng=47,Bio=49,Phy=40)

#Output

'''
Eng marks = 47
Math marks = 41
Bio marks = 49
Phy marks = 40
Urdu marks = 48
Total marks of all subjects = 225

'''