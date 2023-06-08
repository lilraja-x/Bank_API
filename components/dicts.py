'''
    dicts.py

    This file contains dictionaries to be used for validation of data or for dictionaries to guide user of how to enter data.
'''

valid_account_types = {
    'business': 'Business',
    'businessaccount': 'Business',
    'b': 'Business',
    'saving': 'Saving',
    'savingaccount': 'Saving',
    's': 'Saving',
    'current': 'Current',
    'currentaccount': 'Current',
    'c': 'Current',
    'asaan': 'Asaan',
    'asaanaccount': 'Asaan',
    'a': 'Asaan'
}

valid_genders = {
    'male': 'Male',
    'female': 'Female',
    'm': 'Male',
    'f': 'Female'
}

creation_sample = {
    "account_title": "Example",
    "age": "21",
    "mobile_number": "0333*******",
    "gender": "male",
    "account_type": "current",
    "balance": "5512.36"
}