'''
    A bank account management api to allow users to do following operations:
    -------
        - Create Account
        - Login
        - Do Transaction
        - View Data
        - Edit Data
        - Delete
        - Logout
    -------
    
    ----This flask api uses flask_jwt_extended for encoding the account number to allow user login to the bank system to take further actions. This makes the app secure for user.
        -- It uses create_access_token() for an access token and create_refresh_token() for refresh token.
            - Basic usage is to allow user to use refresh token and not needing to login again and again. But user has to use access token for tasks like deleting and editing the data of account.
            - Access token expires after certain time.
            - But refresh tokens may not be generated again and again allowing fluent use of this bank api for user. 
    
    ----It uses an orm sturcutral approach for handling database.
        -- In basic it uses two model classes
            - Accounts (for the account table of database.)
                - account_number
                - account_name
                - account_type
                - balance
            - Customers (for handinlin the customer table of database)
                - account_number
                - account_name
                - account_type
                - age
                - phone
                - gender
        -- The database used is postgresql.
            - Name of Database: Bank
            - Host: Localhost
            - User: pstgresql
            - Password: ****
            - Tables: 
                - Accounts
                - Customers
            - Link to database: postgresql://postgres:****@localhost/Bank
                
    ----It uses blueprint to handle with multiple routes.
        - create_bp ('/create')
        - login_bp('/login')
        - edit_bp ('/edit')
        - transaction_bp ('/transaction')
        - balance_bp ('/balance')
        - view_bp ('/view')
        - delete_bp ('/delete')
        - logout_bp ('/logout')

'''


from flask import Flask
from model import db
from create import create_bp
from edit import edit_bp
from transaction import transaction_bp
from view_balance import balance_bp
from view import view_bp
from delete import delete_bp
from login import login_bp
from logout import logout_bp
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '##jkl*as'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/Bank'

db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


def create_app(config):
    return app


app.register_blueprint(create_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(transaction_bp)
app.register_blueprint(balance_bp)
app.register_blueprint(view_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)