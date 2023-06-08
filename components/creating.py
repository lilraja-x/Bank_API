from model import db, Account, Customer

class Create:

    def create_account(self, data, account_number):
        '''
            To Create Account

            Args:
                -- data(dict): Contains all the information of the user.
                -- account_number(int): Random account number generated which will be assigned to this specific user
        '''
        try:
            account = Account(
                account_number = account_number,
                account_title = data['account_title'],
                account_type = data['account_type'],
                balance = data['balance'])
            customer = Customer(
                account_number = account_number, 
                account_title = data['account_title'], 
                account_type = data['account_type'], 
                age = data['age'], 
                gender = data['gender'], 
                phone = data['mobile_number'])
            db.session.add(account)
            db.session.add(customer)
            db.session.commit()
        except Exception as e:
            raise e