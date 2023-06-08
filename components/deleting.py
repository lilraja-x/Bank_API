from model import db, Account, Customer

class Deleting:

    def delete_account(self, account_number):
        '''
            Deletes the account from database and all of its info.

            Args:
                account_number (int): The acoount number decoded from the token which was sent as heder in the '/delete' route.
        '''
        try:
            costumer_ids = Customer.query.filter_by(account_number = account_number)
            for costumer_id in costumer_ids:
                costumer = Customer.query.filter_by(id = costumer_id.id).first()
                db.session.delete(costumer)
                user = Account.query.filter_by(account_number = account_number).first()
                db.session.delete(user)
                db.session.commit()
        except Exception as e:
            raise e