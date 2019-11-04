s = 'dahhurfvkiaatugb'

vowels = 'aeiou'
count = 0
for i in s:
    for v in vowels:
        if i == v:
            count = count + 1

print('Number of vowels: ' + str(count))
