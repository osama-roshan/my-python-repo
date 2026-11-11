# Encapsulation using private attribute and it is also known as name mangling 

class bank:
    def __init__(self,name:str, balance:int) -> None:
        self.name = name
        self.__balance = balance

    def deposit(self,amount:int) -> None:
        if amount < 0:
            print("Invalid Amount")
        else:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


b1 = bank("Osama",1000)
print(b1.get_balance())
b1.deposit(500)
print(b1.get_balance())

# Output

'''

1000
1500

'''