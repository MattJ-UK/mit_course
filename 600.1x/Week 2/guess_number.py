hi = 100
lo = 0

print('Please think of a number between 0 and 100!')

ans = ''
while ans != 'c':
    g = lo + (hi - lo) //2
    ans = input('Is your secret number ' + str(g) + '?\nEnter \'h\' to indicate the guess is too high. '
                                                    'Enter \'l\' to indicate the guess is too low. '
                                                    'Enter \'c\' to indicate I guessed correctly: ')
    if ans == 'l':
        lo = g
    elif ans == 'h':
        hi = g
    elif ans == 'c':
        break
    else:
        print('That\'s not a valid response, please use either l, h or c')

print('Game over. Your secret number was ' + str(g))


