
def checking_response(response, data):
    '''
        Function that checks: 
            -correctness of message on response status code.

        args:
            - response
            - data
        
        used in:
            - test_create.py
            - test_edit.py
            - test_login.py
            - test_logout.py
            - test_transaction.py
            - test_view.py
    '''
    if response.status_code in (200, 201):
        assert "Account Created Successfully!" or "Account Info Fetched!" or "Balance deposited!" or "Balance withdrawn!" or  "logged out!" or "Logged In!" or "Data updated"or "Balance Fetched" in data['Message']
    elif response.status_code == 500:
        assert "Failed to create account" or "Token Aborted!" or "Invalid!" in data['Message']
    elif response.status_code == 400:
        assert "Incorrect data sent!" or "Incorrect entered data!" or "Atleast give an account number!" or "Failed to login" or "Please enter transaction code." or "transaction choice must be either (deposit/d) or (withdraw/w)" or "Also insert the amount you want to deposit!" or "Not Enough Balance to withdraw money!" or "Balance must be an integer or decimal." or "Also insert the amount you want to withdraw!" or "Invalid!" in data['Message']
    elif response.status_code == 401:
        assert "Missing token" or "Token expired" or "Invalid token" or "No such account number exists!" in data['Message']