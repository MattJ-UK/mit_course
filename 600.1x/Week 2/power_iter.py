def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    out = 1
    while exp > 0:
        out = out * base
        exp -= 1
    return out



