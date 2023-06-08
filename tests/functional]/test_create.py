from app import create_app
import json
from pytest_check import check
from checking_response import checking_response

def test_create_route():
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/create' page is requested (POST)
    THEN check that the response is valid
    '''
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app({"TESTING": True})

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        
        #case 1 ==> with correct inputs
        with check:
            response = test_client.post('/create', 
                                        data=json.dumps(dict(account_title='Raja Uzair', account_type='saving', age = '22', gender = 'male', mobile_number = '03216522362', balance = '52152.632')),
                                        content_type='application/json')
            data = json.loads(response.data)
            checking_response(response, data)

        #case 2 ==> with incorrect inputs
        with check:
            response = test_client.post('/create', 
                                        data=json.dumps(dict(account_title='Raj53456a Uzair', account_type='sav23ing', age = '22', gender = 'male', mobile_number = '03216522362', balance = '52152.632')),
                                        content_type='application/json')
            data = json.loads(response.data)
            checking_response(response, data)





# def test_delete_route():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/delete' page is requested (DELETE)
#     THEN check that the response is valid
#     """
#     # Set the Testing configuration prior to creating the Flask application
#     flask_app = create_app({"TESTING": True})
#     headers = {
#             'Access-Control-Allow-Origin': '*',
#             'Content-Type': 'application/json',
#             'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjA0OTIxNCwianRpIjoiMjlkZWFlMWItMjQ4MC00NTBkLTgwZmEtZTMwNzZkMjBiM2Q4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlBLODE1ODM5ODY3MzAzMzQiLCJuYmYiOjE2ODYwNDkyMTQsImV4cCI6MTY4NjA1MDExNH0.K3nCYmWLk6CLHY9ilb7Kn45MgE9mYuXFC5a-TTMYr7k'
#         }
#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as test_client:
#         response = test_client.delete('/delete', headers= headers)

#         data = json.loads(response.data)

#         assert response.status_code in (200, 201)
#         assert "Deleted!" in data['message']


