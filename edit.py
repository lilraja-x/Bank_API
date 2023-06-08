from flask import Blueprint, request, jsonify
from components.blocklist.blocklist import BLOCKLIST
from components.updating import Update
from components.check_account_numbers import Account_Num
from components.validation.validate import Validation
from flask_jwt_extended import jwt_required, get_jwt_identity
import jwt



check = Account_Num()
validate = Validation()
sample = {"account_number": "PK**************", "age": "22"}


edit_bp = Blueprint('edit', __name__)

# API for editing the account info
@edit_bp.route('/edit', methods=['PUT', 'PATCH'])
@jwt_required()
def edit_account():
    '''
    Route to edit account details

    Body: 
        json format data: The new data user wants to update in their account!
        It is not necessary user will have to send all the data
        User may just edit as per user's need.

    Headers:
        Authorization access token geneerated by logging in the account using account number generated when account was created.
        Key(Authorization): Params(Bearer <access token>)

    Returns:
        In particular if all the data is entered correctly, then just a message is returned saying Data updated is returned and an http response 200

    Exception Raised:
        Following exceptions will be raised::
        --- ValueError: For every incorrect values given by user:
            - Account Title: Must be a string
            - Account Type: Must be of 4 types (Business, Saving, Asaan, Current)
            - Age: Must be an integer (can be string of numbers)
            - Mobile Number: Must be integer and of 11 digits (can be string of numbers)
            - Balance: Must be string of numbers, integers, or float.
        --- Throws an exception if age < 18 for Account Types: Business, Saving and Asaan
        --- Normal Exception Error if occurs in database querys.
        --- Exception if data format is not correct i.e., json.
        --- Exception if token has expired.

    '''
    data = request.json
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'Message': 'Missing token'}), 401

    if token in BLOCKLIST:
        return jsonify({"Message": "Token Aborted!"}), 500
    try:
        account_number = get_jwt_identity()
        update = Update(account_number)
        check.check_account_number(account_number)

        if any(key in data for key in ['account_title', 'age', 'mobile_number', 'gender', 'account_type', 'balance']):
            # Update account title
            if data.get('account_title') is not None:
                try:
                    validate.validate_account_title(data)
                    update.update_account_title(data)
                except Exception as e:
                    return jsonify({"Message": "Incorrect entered data!", "Account Title Error": str(e)}), 400

            # Update account type
            if data.get('account_type') is not None:
                try:
                    validate.validate_account_type_edit(data, account_number)
                    update.update_account_type(data)
                except Exception as e:
                    return jsonify({"Message": "Incorrect entered data!", "Account Type Error": str(e)}), 400

            # Update age
            if data.get('age') is not None:
                try:
                    validate.validate_age(data)
                    update.update_age(data)
                except Exception as e:
                    return jsonify({"Message": "Incorrect entered data!", "Age Error": str(e)}), 400

            # Update gender
            if data.get('gender') is not None:
                try:
                    validate.validate_gender(data)
                    update.update_gender(data)
                except Exception as e:
                    return jsonify({"Message": "Incorrect entered data!", "Gender Error": str(e)}), 400

            # Update mobile number
            if data.get('mobile_number') is not None:
                try:
                    validate.validate_mobile_number(data)
                    update.update_mobile_number(data)
                except Exception as e:
                    return jsonify({"Message": "Incorrect entered data!", "Mobile Number Error": str(e)}), 400

            return jsonify({"Message": "Data updated!"}), 200
        else:
            return jsonify({"Message": "Incorrect entered data!", "example": "If you want to change age", "sample": sample}), 400
    except jwt.ExpiredSignatureError:
        return jsonify({'Message': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'Message': 'Invalid token'}), 401
