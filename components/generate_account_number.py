import random

'''
    To generate a random account number for every new account
'''
account_number = str(random.randint(10000000000000, 99999999999999))
account_number = "PK" + account_number