def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here

    counts = {}
    # count occurrences
    for e in L:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1

    #find largest that happens odd times

    maxelement = 0
    item_exists = False
    for key in counts:
        if counts[key]%2 == 1 and int(key) > maxelement:
            maxelement = key
            item_exists = True
    if item_exists == True:
        return maxelement
    else:
        return None


test = [1,1,2,2,7,7]
print(largest_odd_times(test))