import numpy as np
def create_powerset(choices):
    num_choices = len(choices)

    all = ''
    for i in range(num_choices):
        all += '1'

    maxnum = int(all,2)
    maxnum_len = len(bin(maxnum)[2:])

    powerset = []
    for i in range(maxnum,-1,-1):
        current = bin(i)[2:].zfill(maxnum_len)
        new_array = np.array([])
        for i in current:
            new_array = np.append(new_array, int(i))
        powerset.append(new_array.astype(int))

    return powerset

def find_options(choices,total):
    powerset = create_powerset(choices)

    choice_array = np.array(choices)

    options = {}
    target = total
    found = False
    while target != -1 and found is False:
        for p in powerset:
            product = p*choice_array

            if int(sum(product)) == int(target):
                options[str(p)] = sum(p)
                found = True

        target -= 1


    return options



def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    options = find_options(choices,total)

    lowest_count = len(choices) + 1

    for key in options.keys():
        if options[key] < lowest_count:
            current_leader = key
            lowest_count = options[key]
    l = current_leader[1:-1].split(' ')
    l_int = []
    for s in l:
        l_int.append(int(s))
    output = np.array(l_int)
    return output








test = find_combination([4, 10, 3, 5, 8],1)

print(test)
print(type(test))