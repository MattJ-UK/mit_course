def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test = 0
    if a > b:
        test = b
    else:
        test = a

    out = 0
    for i in range(test, 0, -1):
        if a % i == 0 and b % i == 0:
            out = i
            break

    return out

