def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    c = 0
    if a < b:
        c = a
        a = b
        b = c

    if a % b == 0:
        return b
    else:
        return gcdRecur(b, a % b)