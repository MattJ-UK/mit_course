def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    if char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[0:len(aStr)//2])
    elif char > aStr[len(aStr)//2]:
        return isIn(char,aStr[len(aStr)//2:-1])