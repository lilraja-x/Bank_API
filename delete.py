from flask import Blueprint, jsonify, request
from components.check_account_numbers import Account_Num
from components.deleting import Deleting
from components.blocklist.blocklist import BLOCKLIST
from flask_jwt_extended import jwt_required, get_jwt_identity

delete_bp = Blueprint('delete', __name__)
deletion = Deleting()
check = Account_Num()

@delete_bp.route('/delete', methods = ['DELETE'])
@jwt_required()
def delete():
    '''
    Route to delete accounts

    Body: 
        None

    Headers:
        Authorization access token geneerated by logging in the account using account number generated when account was created.
        Key(Authorization): Params(Bearer <access token>)

    Returns:
        If valid token is sent in headers ith the rewuest to delete at route '/delete' than a response with status code 200 and a message confirming the deletion is sent.

    Exception Raised:
        Following exceptions will be raised::
        --- Exception if token has expired and no new loginn is performed 
        --- Exception if no token is sent as Authorization in request header.
        --- Normal Exception Error if occurs in database querys.

    '''
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Missing token"}), 400
    if token in BLOCKLIST:
        return jsonify({"message": "Token Aborted!"}), 500
    try:
        account_number = get_jwt_identity()
        check.check_account_number(account_number)
        try:
            deletion.delete_account(account_number)
            return jsonify({"message": f"Account {str(account_number)} Deleted!"}), 200
        except Exception as e:
            return jsonify({"message": "Failed to delete", "error": str(e)}), 400
    except:
        return jsonify({"message": "No token found... please login"}), 400

