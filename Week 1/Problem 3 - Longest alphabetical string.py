s = 'azcbobobegghakl'

longest_s = s[0]
current_s = ''

count = 0
end = len(s)

for i in range(0,end):
    current_s = s[i]
    for l in s[(i+1):end]:
        if l >= current_s[-1]:
            current_s = current_s + l
        else:
            break
        if len(current_s) > len(longest_s):
            longest_s = current_s


print('Longest substring in alphabetical order is: ' + str(longest_s))
