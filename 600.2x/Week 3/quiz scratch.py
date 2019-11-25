import random


def rolldie(max):
    options = range(1, max + 1)
    return random.choice(options)


def checkRolls(numRolls, targetNum, sameCount):
    count = 0
    for i in range(numRolls):
        if rolldie(6) == targetNum:
            count += 1

    if count >= sameCount:
        return True
    else:
        return False


def rollTrials(numTrials):
    count = 0
    for t in range(numTrials):
        # Count how many times two sixes come up
        count += int(checkRolls(3, 6, 2))

    return float(count) / float(numTrials)


#print(rollTrials(1000000))

def F():
    mylist = []
    r = 1

    if random.random() > 0.0:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 1:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)


def G():
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.09:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)


def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    remainder = s
    for i in L:
        multipliers.append(remainder // i)
        remainder = remainder % i

    if remainder == 0:
        return sum(multipliers)
    else:
        return 'no solution'


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    # YOUR CODE HERE
    max = 0
    for i in range(len(L)):
        x = 0
        while x + i <= len(L):
            print('Checking start:' + str(i) + ' and end:' + str(x + i) + ', sum is ' + str(sum(L[i:x + i + 1])))
            if sum(L[i:x + i + 1]) > max:
                max = sum(L[i:x + i + 1])
            x += 1

    return max


# L = [1, -1]

# print(max_contig_sum(L))

def solveit_cheat(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    # IMPLEMENT THIS FUNCTION
    options = range(-1000, 1000)

    for i in options:
        if test(i):
            break

    return i

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    # IMPLEMENT THIS FUNCTION
    x = 0
    y = 0
    while test(x) == False and test(y) == False:
        x += 1
        y -= 1

    if test(x):
        return x
    else:
        return y


#### This test case prints 49 ####
def f(x):
    return (x + 15) ** 0.5 + x ** 0.5 == 15


#print(solveit(f))


#### This test case prints 0 ####
def f(x):
    return x == -20


#print(solveit(f))
