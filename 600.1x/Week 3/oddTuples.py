def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    i = 0
    out = ()
    while i < len(aTup):
        out = out + (aTup[i],)
        i += 2

    return out