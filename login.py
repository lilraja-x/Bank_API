from flask import Blueprint, jsonify, request
from components.check_account_numbers import Account_Num
from flask_jwt_extended import create_refresh_token, create_access_token



login_bp = Blueprint('login', __name__)
check_account_num = Account_Num()

@login_bp.route('/login', methods = ['POST'])
def login():
    '''
    Route to login account

    Body: 
        json format data: Just the account number that was generated when user created their account!

    Headers:
        None

    Returns:
        In particular if account number is correct and is found in database then it is sent as identity and an access token and refresh token is generated for the user

    Exception Raised:
        Following exceptions will be raised::
        --- Exception if the account number does not exists in the database.

    '''
    data = request.json
    if data.get('account_number'):
        account_number = data.get('account_number')
        try:
            check_account_num.check_account_number(account_number)
            access_token = create_access_token(identity= str(account_number))
            refresh_token = create_refresh_token(identity= str(account_number))
            return jsonify({'Message': 'Logged In!','access token': access_token, 'refresh token': refresh_token }), 200
        except Exception as e:
            return jsonify({'Message': 'No such account number exists!', 'Error': str(e)}), 401
    else:
        return jsonify({"Message": "Atleast give an account number!"}), 400
