import pytest

from simple_bank.components.account import Account
from simple_bank.utils.transactions import process_transactions


@pytest.fixture()
def account(scope="function"):
    """Creates an account"""
    return Account()
