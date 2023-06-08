from app import create_app
import json
from pytest_check import check
from checking_response import checking_response


def test_edit_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/edit' page is requested (PUT/PATCH)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app({"TESTING": True})
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjEzODgwMCwianRpIjoiOWQzMWYzNzQtYjJjNS00NzgwLWIyNzAtYTIzN2Y5Y2E1NmVjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlBLODQ0NDI0MTE0NDY0NDEiLCJuYmYiOjE2ODYxMzg4MDAsImV4cCI6MTY4NjEzOTcwMH0.v8WVeLsJOetMYwaDSCSipES4iwSuhd0zPlNGA4Rdf3o'
        }
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        #Case 1 ==> To Edit with correct inputs
        with check:
            response = test_client.patch('/edit', headers= headers, data=json.dumps(dict(account_title="Asifa Shaheen")))

            data = json.loads(response.data)
            checking_response(response, data)
        #Case 2 ==> To Edit with all correct inputs
        with check:
            response = test_client.patch('/edit', headers= headers, data=json.dumps(dict(account_title="Asifa Shaheen", age="24", mobile_number="03215648654", gender="female")))

            data = json.loads(response.data)
            checking_response(response, data)


        #Case 3 ==> To Edit with incorrect inputs
        with check:
            response = test_client.patch('/edit', headers= headers, data=json.dumps(dict(account_title="Asifa 123Shaheen")))

            data = json.loads(response.data)
            checking_response(response, data)

        #Case 4 ==> To Edit with wrong headers
        with check:
            headers = {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NuEzNzU1MCwianRpIjoiZjcyZWE0OGMtMDUyNi00ZGViLTg4MTQtNjdiYWRjYTEzN2EwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlBLODQ0NDI0MTE0NDY0NDEiLCJuYmYiOjE2ODYxMzc1NTAsImV4cCI6MTY4NjEzODQ1MH0.5NE3R2EmZLMWYlVVG1Vlp9G_9SFTN4YfFVuS-EFocAs'
            }
            response = test_client.patch('/edit', headers= headers, data=json.dumps(dict(account_title="Asifa 123Shaheen")))

            data = json.loads(response.data)
            checking_response(response, data)