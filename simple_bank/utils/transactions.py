"""Utility responsible for handling transactions"""

def process_transactions(acct, transctions):
    """Processes a given list of transctions

    Args:
        acct(Account): Account to process transctions on
        tranctions(list): List of transctions
    """
    # @TODO: Use Account component methods to handle transactions
    for trans in transctions:
        if trans == 'withdraw':
            pass
        if trans == 'deposit':
            pass
        elif trans == 'fee':
            pass
        elif trans == 'dividend':
            pass

    return acct
