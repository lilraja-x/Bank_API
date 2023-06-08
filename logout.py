from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from components.check_account_numbers import Account_Num
from components.blocklist.blocklist import BLOCKLIST

check = Account_Num()

logout_bp = Blueprint('logout', __name__)
@logout_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    '''
    Route to logout accounts

    Body: 
        None

    Headers:
        Authorization access token geneerated by logging in the account using account number generated when account was created.
        Key(Authorization): Params(Bearer <access token>)

    Returns:
        In particular if the header is correct, then that token is added in blocklist from preventing it to be used again and then a message of logout succesfull with status code 200 is sent as a response

    Exception Raised:
        Following exceptions will be raised::
        --- Exception if no token given.
        --- Exception if token has expired.

    '''
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'Message': 'Missing token'}), 401
    
    if token in BLOCKLIST:
        return jsonify({"Message": "Token Aborted!"}), 500

    try:
        account_number = get_jwt_identity()
        check.check_account_number(account_number)
        try:
            BLOCKLIST.add(token)
            return {"Message": f"Account {account_number} logged out!"}, 200
        except Exception as e:
            return {"Message": "Failed to login", "error": str(e)}, 400
    except Exception as e:
        return jsonify ({"Message": "Invalid token", "error": str(e)}), 401
