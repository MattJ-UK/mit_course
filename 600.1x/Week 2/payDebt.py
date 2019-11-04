balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12

def addInterest(bal,intRate):
    """
    :param bal: current balance
    :param intrate: monthly interest rate
    :return: updated balance
    """
    bal  = bal * (1+intRate)
    return bal

def payAmount(bal, payRate):
    """
    :param bal: current balance
    :param payRate: percent being paid
    :return: updated balance
    """
    bal -= bal * payRate
    return bal

for i in range (1,13):
    balance = addInterest(balance, monthlyInterestRate)
    balance = payAmount(balance,monthlyPaymentRate)
    #print('Month ' + str(i) + ' Remaining balance: ' + str(round(balance,2)))

print('Remaining balance: ' + str(round(balance,2)))