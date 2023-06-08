from app import create_app
import json
from pytest_check import check
from checking_response import checking_response


def test_transaction_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/transaction' page is requested (PATCH)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app({"TESTING": True})
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjE0Mzk1OSwianRpIjoiYWQ2ZjI2ZWItNzRkNi00MWY0LWFhMDAtNzQxYzU1MDZjMGUyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlBLODQ0NDI0MTE0NDY0NDEiLCJuYmYiOjE2ODYxNDM5NTksImV4cCI6MTY4NjE0NDg1OX0.YZfrnGqp-CM8vX-jFA54wHlxQpGSzOOMHr75nVfDHoQ'
        }
    # Create a test client using the Flask application configured for testing

    # Case 1 ==> for deposit
    with flask_app.test_client() as test_client:
        response = test_client.patch('/transaction', headers= headers, data=json.dumps(dict(transaction_code="d", amount="525.26")))

        data = json.loads(response.data)
        checking_response(response, data)

    # Case 2 ==> for withdraw
    with flask_app.test_client() as test_client:
        response = test_client.patch('/transaction', headers= headers, data=json.dumps(dict(transaction_code="w", amount="525.26")))

        data = json.loads(response.data)
        checking_response(response, data)

    # Case 3 ==>  for error handling
    with flask_app.test_client() as test_client:
        response = test_client.patch('/transaction', headers= headers, data=json.dumps(dict(transaction_code="s", amount="525.26")))

        data = json.loads(response.data)
        checking_response(response, data)
        
        
    # Case 4 ==> for error handling
    with flask_app.test_client() as test_client:
        response = test_client.patch('/transaction', headers= headers, data=json.dumps(dict(transaction_code="w", amount="asasd541.2351a")))

        data = json.loads(response.data)
        checking_response(response, data)

    # Case 5 ==> for error handling
    with flask_app.test_client() as test_client:
        response = test_client.patch('/transaction', headers= headers, data=json.dumps(dict(transaction_code="-", amount="asasd541.2351a")))

        data = json.loads(response.data)
        checking_response(response, data)

    # Case 6 ==> for withdrawing more than what is in bank
    with flask_app.test_client() as test_client:
        response = test_client.patch('/transaction', headers= headers, data=json.dumps(dict(transaction_code="w", amount="99999999999999999999")))

        data = json.loads(response.data)
        checking_response(response, data)