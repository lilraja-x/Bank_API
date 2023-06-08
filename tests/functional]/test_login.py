from app import create_app
from pytest_check import check
import json
from checking_response import checking_response

def test_login_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (POST)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app({"TESTING": True})
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:

        #Case 1 ==> to login with correct creditienals
        with check:
            response = test_client.post('/login', data= json.dumps(dict(account_number= 'PK84442411446441')), content_type='application/json')
            data = json.loads(response.data)
            checking_response(response, data)

        #Case 2 ==> to login with incorrect creditienals
        with check:
            response = test_client.post('/login', data= json.dumps(dict(account_number= 'PK84442411446442')), content_type='application/json')
            data = json.loads(response.data)
            checking_response(response, data)

        #Case 3 ==> to login with incorrect creditienals(2)
        with check:
            response = test_client.post('/login', data= json.dumps(dict(account_number= 'PK8444241144644')), content_type='application/json')
            data = json.loads(response.data)
            checking_response(response, data)

        #Case 4 ==> to login with empty creditienals
        with check:
            response = test_client.post('/login', data= json.dumps(dict(account_number= '')), content_type='application/json')
            data = json.loads(response.data)
            checking_response(response, data)
