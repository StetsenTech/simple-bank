# This module responsible for handling information about an account


class Account(object):
    """Module to handle functional of accounts"""

    def __init__(self):
        self.cash = 0
        self.dividend_rate = 0
        self.transactions = []

    def __add__(self, o_acct):
        """Find the differences between accounts"""

        if isinstance(o_acct, Account):
            raise NotImplementedError("Merge accounts is under development")
        else:
            raise NotImplementedError("Both operands must be of type Account")

    def __sub__(self, o_acct):
        """Find the differences between accounts"""

        if isinstance(o_acct, Account):
            raise NotImplementedError("Finding differences between accounts is under development")
        else:
            raise NotImplementedError("Both operands must be of type Account")

    def deposit_cash(self, amount):
        """Deposits cash into account

        Args:
            amount(float): Amount of cash to deposit
        """
        self.cash += amount

    def withdraw_cash(self, amount):
        """Withdraws cash from account

        Args:
            amount(float): Amount of cash to withdraw
        """
        self.cash += amount

    def apply_dividend(self, dividend):
        """Pays dividend

        Args:
            symbol(string): Name of shares
            dividend(float): Dividend issued
        """
        self.cash += dividend

    def apply_fee(self, fee):
        """Fees owed

        Args:
            amount(float): Amount of fee
        """
        self.cash -= fee
