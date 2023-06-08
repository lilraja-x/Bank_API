from ..dicts import valid_account_types, valid_genders
from ..fetching import Fetching


class Validation:

    '''
        A class that handles all the methods for validating certain entries sent by user. Either they follow sepecfic format or not.
    '''

    def validate_account_title(self, data):
        '''
            Validate Account Title

            -- To Validate
                - Either a string and combination of characters (a-z)(A-Z) or not
            
            -- Args
                - data(dict): The dictionary from which the key 'account_title' will be selected. 
        '''
        if not data['account_title'].replace(" ", "").isalpha():
            raise ValueError("Account Title must be a string!")

    def validate_age(self, data):
        '''
            Validate Age

            -- To Validate
                - Either an integer or combination  of digits or not.
            
            -- Args
                - data(dict): The dictionary from which the key 'age' will be selected. 
        '''
        if type(data['age']) != int:
            if not data['age'].isdigit():
                raise ValueError("Age must be an integer")

    def validate_mobile_number(self, data):
        '''
            Validate Mobile Number

            -- To Validate
                - Either combination of digits and length less than 11.
            
            -- Args
                - data(dict): The dictionary from which the key 'mobile_number' will be selected. 
        '''
        if not data['mobile_number'].isdigit() or len(data['mobile_number']) != 11:
            raise ValueError("Mobile Number must be given in integers and the length must be 11.")

    def validate_gender(self, data):
        '''
            Validate Gender

            -- To Validate
                - Either male or female or not
            
            -- Args
                - data(dict): The dictionary from which the key 'gender' will be selected. 
        '''
        data['gender'] = valid_genders.get(data['gender'].strip().lower(), None)
        if data['gender'] is None:
            raise ValueError("Gender must be either Male or Female")

    def validate_account_type_edit(self, data, account_number):
        '''
            Validate Account Type

            -- To Validate
                - Either a valid account type or not (Business, Saving, Current, Asaan)
            
            -- Args
                - data(dict): The dictionary from which the key 'account_title' will be selected. 
        '''
        fetch = Fetching(account_number)
        if data['account_type'].lower().replace(" ", "") not in valid_account_types or data['account_type'] == "":
            raise ValueError("Account Type must be either Business, Saving, Current, Asaan!")
        elif data['account_type'].lower().replace(" ", "") in valid_account_types and int(fetch.get_age()) < 18:
            if data['account_type'].lower().replace(" ", "") in ['asaan', 'a', 'asaanaccount']:
                data['account_type'] = valid_account_types[data['account_type']]
            else:
                raise ValueError(f"For {data['account_type'].capitalize()} account! Your age must be 18 or greater than 18!")
        else:
            data['account_type'] = valid_account_types[data['account_type'].lower().replace(" ", "")] 

    def validate_account_type_create(self, data):
        '''
            Validate Account Type

            -- To Validate
                - Either a valid account type or not (Business, Saving, Current, Asaan)
            
            -- Args
                - data(dict): The dictionary from which the key 'account_title' will be selected. 
        '''
        if data['account_type'].lower().replace(" ", "") not in valid_account_types or data['account_type'] == "":
            raise ValueError("Account Type must be either Business, Saving, Current, Asaan!")
        elif data['account_type'].lower().replace(" ", "") in valid_account_types and int(data['age']) < 18:
            if data['account_type'].lower().replace(" ", "") in ['asaan', 'a', 'asaanaccount']:
                data['account_type'] = valid_account_types[data['account_type']]
            else:
                raise ValueError(f"For {data['account_type'].capitalize()} account! Your age must be 18 or greater than 18!")
        else:
            data['account_type'] = valid_account_types[data['account_type'].lower().replace(" ", "")] 

    def validate_balance(self, data):
        '''
            Validate Balance

            -- To Validate
                - Either integer/float or not.
            
            -- Args
                - data(dict): The dictionary from which the key 'balance' will be selected. 
        '''
        try:
            data['balance'] = float(data['balance'])
            if data['balance'] <= 0:
                raise ValueError("Balance must be a positive number")
        except ValueError:
            raise ValueError("Invalid Input: Balance must be a number/integer.")
