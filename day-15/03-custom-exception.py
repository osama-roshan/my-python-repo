# Custom exception

class insufficientfundsError(Exception):
    pass


def withdraw_money(balance,withdraw_amount):
    if withdraw_amount > balance:
        raise insufficientfundsError("Not enough Balance")
    print(f"Remaing balance = {balance - withdraw_amount}")

try:
    withdraw_money(1000,5000)
except insufficientfundsError as e:
    print(f"error = {e}")
except Exception as e:
    print(f"error = {e}")

# Output

'''

error = Not enough Balance

'''