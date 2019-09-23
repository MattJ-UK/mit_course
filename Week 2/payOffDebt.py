def addInterest(bal,intRate):
    """
    :param bal: current balance
    :param intrate: monthly interest rate
    :return: updated balance
    """
    bal  = bal * (1+intRate)
    return bal

