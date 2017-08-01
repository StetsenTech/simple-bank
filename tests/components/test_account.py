import pytest

from simple_bank.components.account import Account


@pytest.fixture()
def account(scope="function"):
    """Creates an account"""
    return Account()

@pytest.mark.xfail(raises=NotImplementedError)
def test_account_add_fail(account):
    """Tests trying to add an account by another type of object"""
    account + {"test": "fail"}


@pytest.mark.xfail(raises=NotImplementedError)
def test_account_subtract_fail(account):
    """Tests trying to subtract an account by another type of object"""
    account - {"test": "fail"}
