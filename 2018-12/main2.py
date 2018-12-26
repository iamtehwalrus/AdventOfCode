import re

fpath = 'input.txt'
contents = open(fpath,'r').read().splitlines()

numpad = 200
numgens = 150

currentgen = re.search('(#|\.)+', contents[0]).group()
currentgen = '.' * numpad + currentgen + '.' * numpad

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
    numplants = 0
    for i, c in enumerate(str):
        i -= numpad
        if c == '#':
            sum += i
            numplants += 1
    return sum, numplants

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


for gen in range(numgens):
    lastvalue = getsum(currentgen)
    currentgen = nextgen(currentgen)
    thisvalue = getsum(currentgen)

    if lastvalue[1] == thisvalue[1] and thisvalue[0] == lastvalue[0] + lastvalue[1]:
        break

finalvalue = (50000000000 - (gen + 1)) * thisvalue[1] + thisvalue[0]

print(finalvalue)