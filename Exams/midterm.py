def count7(N):
    if N == 0:
        return 0
    elif N%10 == 7:
        return 1 + count7(N//10)
    else:
        return 0 + count7(N//10)

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    output = 0
    for i in range(len(listA)):
        output += listA[i] * listB[i]

    return output

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    out = []
    for key, val in aDict.items():
        if val == target:
            out.append(key)

    return out

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N//10 == 0:
        return N%10
    else:
        return N%10 + sumDigits(N//10)

def sumFunc(a,b):
    return a+b

def score(word, f):
    """
       word, a string of length > 1 of alphabetical
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26)
       times its distance from start of word.
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters.
       The first parameter to f is the highest letter score,
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the
           score for 'adD' is 12
    """
    #YOUR CODE HERE

    def letterScore(y,z):
        return y*z

    lowerWord = word.lower()

    scorenums = {'a':1, 'b':2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g':7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                 'n': 14, 'o':15, 'p':16, 'q':17, 'r': 18, 's': 19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

    scorelist = []
    for i in range(len(lowerWord)):
        scorelist.append(letterScore(i, scorenums[lowerWord[i]]))

    scorelist.sort(reverse=True)
    return f(scorelist[0], scorelist[1])


