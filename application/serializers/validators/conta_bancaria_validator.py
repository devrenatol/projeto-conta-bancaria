import re

def invalid_account_number(account_number):
    model = '[0-9]{5}-[0-9]{2}'
    response = re.findall(model, account_number)
    return not response

def invalid_account_holder(account_holder):
    return not account_holder.replace(' ', '').isalpha()

def invalid_balance(balance):
    return balance < 0