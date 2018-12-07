import re
import numpy as np

fpath = 'input.txt'
fabric = np.zeros((1000,1000))

def parse(str):
    strlist = list(filter(None,re.split('[ #@,:x]', str)))
    intlist = list(map(int, strlist))
    return intlist

f = open(fpath,'r')
contents = f.read().splitlines()
f.close()

for index, line in enumerate(contents):
    contents[index] = parse(line)

for index in range(len(contents)):
    a = contents[index][1]
    b = contents[index][2]
    c = contents[index][3]
    d = contents[index][4]
    fabric[b:b+d, a:a+c] += 1

for index in range(len(contents)):
    a = contents[index][1]
    b = contents[index][2]
    c = contents[index][3]
    d = contents[index][4]
    if np.array_equal(fabric[b:b+d, a:a+c], np.ones((d, c))):
        print(contents[index][0])
        break