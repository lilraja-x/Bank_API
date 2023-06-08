from model import Account, Customer


class Fetching:

    '''
        A class that handles all the methods used for fetching required information from database.

        -- Methods involved:
            - to get account type
            - to get age
            - to get balance
            of the current account number refrenced to the token sent as Authorization in header of whereever this object is instantiated.

        -- On intializing the the class accepts account number decoded from token in whichever route this class is initialized.
    '''

    def __init__(self, account_number):
        '''
            __init__() constructor to define to bind the arguments to attributes and apply query on them to filter out that row from database.
        '''
        self.account = Account.query.filter_by(account_number = account_number).first()
        self.customer = Customer.query.filter_by(account_number = account_number).first()

    def get_account_type(self):
        '''
            Gets the account type.

            Args:
                instances of this class i.e., 
                    - account
                    - customer
        '''
        return self.account.account_type
        
    def get_age(self):
        '''
            Gets the age.

            Args:
                instances of this class i.e., 
                    - account
                    - customer
        '''
        return self.customer.age
    
    def get_balance(self):
        '''
            Gets the balance.

            Args:
                instances of this class i.e., 
                    - account
                    - customer
        '''
        return round(float(self.account.balance), 2)