import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        sd = float('NaN')
    else:
        lengths = []
        for e in L:
            lengths.append(len(e))

        count = len(lengths)
        mean = sum(lengths) / count

        varsum = 0
        for l in lengths:
            varsum += (l-mean)**2

        sd = math.sqrt(varsum/count)

    return sd


L = ['blah', 'flap', 'banana']

print(stdDevOfLengths(L))



