from model import Account

class Account_Num:

    def check_account_number(self, account_number):
            '''
               To check if the account number exists in database or not.

               Args:
                    --account_number(int): The account number to be validated.
               
               Return:
                    -- if it exists:
                         return account_number
                    -- if not, then
                         raise Exception to trigger the exception in the parent file.
            '''
            Acc = Account.query.filter_by(account_number=account_number).first()
            if Acc.account_number:
                 return Acc.account_number
            else:
                 raise Exception