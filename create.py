from flask import jsonify, request, Blueprint
from model import db
from components.creating import Create
from components.generate_account_number import account_number
from components.validation.validate import Validation
from components.dicts import creation_sample


create_bp = Blueprint('create', __name__)
creating = Create()
validate = Validation()

@create_bp.route('/create', methods=['POST'])
def create_account():
    '''
        Route to create accounts

        Body: 
            json format data: The data user want to save in their account!

        Headers:
            None

        Returns:
            In particular if all the data is entered correctly, then just a message is returned saying account is returned with the Account Number assigned to user and an http response 200

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

    '''

    data = request.json    
    required_keys = ['account_title', 'age', 'mobile_number', 'gender', 'account_type', 'balance']
    if all(key in data for key in required_keys):
        try:
            validate.validate_account_title(data)
            validate.validate_age(data)
            validate.validate_mobile_number(data)
            validate.validate_gender(data)
            validate.validate_account_type_create(data)
            validate.validate_balance(data)
            creating.create_account(data, account_number)
            db.session.rollback()
            return jsonify({"Message": "Account Created Successfully!", "Account Number": account_number}), 201
        except ValueError as VE:
            return jsonify({"Message": "Incorrect data sent!", "Error": str(VE)}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({"Message": "Failed to create account", "Error": str(e)}), 500
    else :
        return (jsonify({"Message": "Incorrect data sent!", "sample": creation_sample})), 400
