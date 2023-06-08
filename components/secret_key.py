from flask import current_app


def get_secret_key():
    '''
        Get Secret Key from app.py for further use
    '''
    secret_key = current_app.config['SECRET_KEY']
    return secret_key