from model import Account, Customer


def test_new_account():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the account_number, account_title, balance and account_type are defined correctly.
    """
    account = Account('PK46213120594897', 'Osama', 'saving', 562656.651)
    costumer = Customer('PK46213120594897', 'Osama', 'saving', '26', 'male', '03216523626')
    assert account.account_number == 'PK46213120594897'
    assert account.account_title == 'Osama'
    assert account.account_type == 'saving'
    assert account.balance == 562656.651
    assert costumer.account_number == 'PK46213120594897'
    assert costumer.account_title == 'Osama'
    assert costumer.account_type == 'saving'
    assert costumer.age == '26'
    assert costumer.gender == 'male'
    assert costumer.phone == '03216523626'



