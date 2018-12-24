import numpy as np

fpath = 'input.txt'
contents = open(fpath,'r').read().splitlines()

for i, coord in enumerate(contents):
    contents[i] = list(map(int, coord.split(', ')))

licoords = contents

ymax = max(licoords, key=lambda x: x[1])[1]
xmax = max(licoords, key=lambda x: x[0])[0]

field = np.zeros((xmax, ymax)).astype(int)

maxdist = 10000

def finddistance(x, y, licoords):
    distance = 0
    for i, coords in enumerate(licoords):
        distance += abs(coords[0] - x) + abs(coords[1] - y)
    return distance

for x, xc in enumerate(field):
    for y, yc in enumerate(xc):
        if finddistance(x, y, licoords) < maxdist:
            field[x, y] = 1

print(np.sum(field))