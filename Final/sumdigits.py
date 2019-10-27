def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    ans = 0
    count = 0
    for e in s:
        try:
            ans += int(e)
            count += 1
        except:
            continue

    if count == 0:
        raise ValueError('No digits in string')
    else:
        return ans


print(sum_digits('1adlfk3456jg12h5'))