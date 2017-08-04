# This module responsible for handling information about an account


class Account(object):
    """Module to handle functional of accounts"""

    def __init__(self):
        self.cash = 0
        self.dividend_rate = 0
        self.transactions = []
        self.atm_fee = 0
        self.overdraft_protection = False
        self.overdraft_fee = 0

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
        return self._adjust_cash(amount)

    def withdraw_cash(self, amount, atm=False, force=False):
        """Withdraws cash from account

        Args:
            amount(float): Amount of cash to withdraw
        """
        if not force and (self.cash <= 0 or self.cash <= amount):
            # @TODO: Create exception for Withdraw errors
            raise Exception("There isn't enough cash to withdraw specified amount.")

        if self.cash - amount < 0 and self.overdraft_protection:
            self.cash -= self.overdraft_fee
        else:
            # @TODO: Create exception for overdraft errors
            raise Exception("Unable to overdraft account.")


        return self._adjust_cash(-amount)


    def apply_dividend(self):
        """Pays dividend

        Args:
            symbol(string): Name of shares
            dividend(float): Dividend issued
        """
        raise NotImplementedError("Applying dividend to account is not implemented.")

    def apply_fee(self, fee):
        """Fees owed

        Args:
            amount(float): Amount of fee
        """
        return self._adjust_cash(-fee)

    def _add_transaction(self, t_name, t_date, t_amount):
        """Adds transtion to history

        Args:
            t_name(string): Name/Details of transction
            t_date(string): Date of transction
            t_amount(float): Transaction amount
        """
        pass

    def _adjust_cash(self, amount):
        """Handles changing amount of cash in current account

        Args:
            amountamount(float): 
        """
        
        self.cash += amount

        return self.cash