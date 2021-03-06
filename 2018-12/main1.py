import re

fpath = 'input.txt'
contents = open(fpath,'r').read().splitlines()

padnum = 30

currentgen = re.search('(#|\.)+', contents[0]).group()
currentgen = '.'*padnum + currentgen + '.'*padnum

patternlist = []
replacelist = []
contentsiter = iter(contents)
next(contentsiter)
next(contentsiter)
for line in contentsiter:
    patternlist.append(re.search('(#|\.){5}', line).group())
    replacelist.append(line[-1])

def getsum(str):
    sum = 0
    for i, c in enumerate(str):
        i -= padnum
        if c == '#':
            sum += i
    return sum

def nextgen(currentgen):
    nextgen = list(currentgen)
    for i in range(len(currentgen)-5):
        for j, pattern in enumerate(patternlist):
            if currentgen[i:i+5] == pattern:
                nextgen[i+2] = replacelist[j]
                break
    nextgen = ''.join(nextgen)
    print(nextgen, getsum(nextgen))
    return nextgen


for _ in range(20):
    currentgen = nextgen(currentgen)

print(getsum(currentgen))