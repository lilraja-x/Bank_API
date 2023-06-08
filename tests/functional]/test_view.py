from app import create_app
import json
from pytest_check import check
from checking_response import checking_response


def test_view_route():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/view' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app({"TESTING": True})
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjA0OTEyNSwianRpIjoiMmI1ZDIyYTQtN2E2Yy00Y2Q0LWJkNTUtMzRiYzRmZjMwMzZhIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJQSzg0NDQyNDExNDQ2NDQxIiwibmJmIjoxNjg2MDQ5MTI1LCJleHAiOjE2ODg2NDExMjV9.KAhTcbk0-S032eZ6fAUlF0KgSEwUHn3s3AxI2qVCJyI'
        }
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        #case 1 ==> with proper header
        with check:
            response = test_client.get('/view', headers= headers)
            data = json.loads(response.data)
            checking_response(response, data)

        #case 2 ==> with no header
        with check:
            response = test_client.get('/view')
            data = json.loads(response.data)
            checking_response(response, data)

        #case 3 ==> with wrong header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjA0OTEyNSwianRpIjoiMmI1ZDIyYTQtN2E2Yy00Y2Q0LWJkNTUtMzRiYzRmZjMwMzZhIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJQSzg0NDQyNDExNDQ2NDQxIiwibmJmIjoxNjg2MDQ5MTI1LCJleHAiOjE2ODg2NDExMjV9.KAhTcbk0-S032eZ6fAUlF0KgSEwUHn3s3AxI2qVCJyT'
        }
        with check:
            response = test_client.get('/view', headers= headers)
            data = json.loads(response.data)
            checking_response(response, data)

