s = 'azcbobobegghakl'
count = 0
end = len(s)

for i in range(0, end-2):
    if s[i:(i+3)] == 'bob':
        count += 1

print('Number of times bob occurs is: ' + str(count))


