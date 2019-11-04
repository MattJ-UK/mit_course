def recurPower(base, exp):
    """
    :param base: int
    :param exp: int >= 0
    :return: base to power of exp using recursion
    """
    if exp >= 1:
        return base * recurPower(base, exp-1)
    else:
        return 1
