from model import Account, Customer, db


class Update:
    '''
        This is class named Update which has all the methods that are responsible for updating the data in database as per user needs.
        
        -- Methods involved:
            - To update account_title
            - to update account_type
            - to update age
            - to update gender
            - to update mobile number
            - to update balance on withdrawl
            - to update balance on deposit

        -- On intializing the the class accepts account number decoded from token in whichever route this class is initialized.
    '''

    def __init__(self, account_number):
        '''
            __init__() constructor to define to bind the arguments to attributes and apply query on them to filter out that row from database.
        '''
        self.account = Account.query.filter_by(account_number = account_number).first()
        self.customer = Customer.query.filter_by(account_number = account_number).first()

    def update_account_title(self, data):
        '''
            Updates Account Title.
            
            Args:
                -- instances of this class i.e., 
                    - account
                    - customer
                -- data(dict): The dictionary from which the key 'account_title' will be selected. 
        '''
        try:
            self.account.account_title = data['account_title']
            self.customer.account_title = data['account_title']
            db.session.commit()
        except Exception as e:
            raise e 
        
    def update_account_type(self, data):
        '''
            Updates Account Type.
            
            Args:
                -- instances of this class i.e., 
                    - account
                    - customer
                -- data(dict): The dictionary from which the key 'account_type' will be selected. 
        '''
        try:
            self.account.account_type = data['account_type']
            self.customer.account_type = data['account_type']
            db.session.commit()
        except Exception as e:
            raise e
        
    def update_age(self, data):
        '''
            Updates Age.
            
            Args:
                -- instances of this class i.e., 
                    - account
                    - customer
                -- data(dict): The dictionary from which the key 'age' will be selected. 
        '''
        try:
            self.customer.age = data['age']
            db.session.commit()
        except Exception as e:
            raise e 

    def update_mobile_number(self, data):
        '''
            Updates Mobile Number.
            
            Args:
                -- instances of this class i.e., 
                    - account
                    - customer
                -- data(dict): The dictionary from which the key 'mobile_number' will be selected. 
        '''
        try:
            self.customer.phone = data['mobile_number']
            db.session.commit()
        except Exception as e:
            raise e

    def update_gender(self, data):
        '''
            Updates Gender.
            
            Args:
                -- instances of this class i.e., 
                    - account
                    - customer
                -- data(dict): The dictionary from which the key 'gender' will be selected. 
        '''
        try:
            self.customer.gender = data['gender']
            db.session.commit()
        except Exception as e:
            raise e
        
    def update_balance_on_withdrawl(self, amount):
        '''
            Updates Balance on withdrawl of money.
            
            Args:
                -- instances of this class i.e., 
                    - account
                    - customer
                -- amount(str or int or float): The amount to be withdrawn from account 
        '''
        try:
            self.account.balance = self.account.balance - amount
            db.session.commit()
            new_balance = self.account.balance
            new_balance = round(float(new_balance), 2)
            return new_balance
        except Exception as e:
            raise e
        
    def update_balance_on_deposit(self, amount):
        '''
            Updates Balance on deposit of money.
            
            Args:
                -- instances of this class i.e., 
                    - account
                    - customer
                -- amount(str or int or float): The amount to be deposited to the account 
        '''
        try:
            self.account.balance = self.account.balance + amount
            db.session.commit()
            new_balance = self.account.balance
            new_balance = round(float(new_balance), 2)
            return new_balance
        except Exception as e:
            raise e