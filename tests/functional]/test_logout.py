import json
from app import create_app
from pytest_check import check
from checking_response import checking_response


def test_logout_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (POST)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app({"TESTING": True})
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjEzOTIxMSwianRpIjoiNmViNjhkNDUtNzJmMS00OTgwLTk3YTgtYjk0ZDk5ZjhlMDIzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlBLODQ0NDI0MTE0NDY0NDEiLCJuYmYiOjE2ODYxMzkyMTEsImV4cCI6MTY4NjE0MDExMX0.y6p3IK0w0NLbFukvW8naUQoNaRfX453wy3UOslOVVBk'
        }
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        with check:
            response = test_client.post('/logout', headers= headers)

            data = json.loads(response.data)
            checking_response(response, data)

        headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsINR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjA1ODYxMSwianRpIjoiZDdmYzJmZGItMThjNy00NTMyLWEyMDgtNTAyNWU3NDY1MmMyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlBLODQ0NDI0MTE0NDY0NDEiLCJuYmYiOjE2ODYwNTg2MTEsImV4cCI6MTY4NjA1OTUxMX0.qPbufJR020R_7bRBxxIGuFNF_8ktw5GRqEov6PBvb3k'
        }
        with check:
            response = test_client.post('/logout', headers = headers)

            data = json.loads(response.data)
            checking_response(response, data)
