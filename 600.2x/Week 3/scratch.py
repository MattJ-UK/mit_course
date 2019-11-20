import math

def coVar(L):
    """

    :param L: a list of values (int or float)_
    :return: the coefficient of variation (stdev / mean)
    """

    count = len(L)
    mean = sum(L) / count

    varsum = 0
    for l in L:
        varsum += (l - mean) ** 2

    sd = math.sqrt(varsum / count)

    coVarOut = sd/mean


    return coVarOut

L = [10, 4, 12, 15, 20, 5]

print(coVar(L))