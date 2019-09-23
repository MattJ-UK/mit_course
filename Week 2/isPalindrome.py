def isPalindrome(str):
    if len(str) <=1:
        return True
    else:
        return isPalindrome(str[1:-1]) and str[0] == str[-1]

