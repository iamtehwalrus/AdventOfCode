import numpy as np

fpath = 'input.txt'
contents = open(fpath,'r').read().splitlines()

for i, coord in enumerate(contents):
    contents[i] = list(map(int, coord.split(', ')))

licoords = contents

ymax = max(licoords, key=lambda x: x[1])[1]
xmax = max(licoords, key=lambda x: x[0])[0]

field = np.zeros((xmax, ymax)).astype(int)


for x, xc in enumerate(field):
    for y, yc in enumerate(xc):
        shortestdist = max(xmax, ymax)
        for ic, coords in enumerate(licoords):
            ic += 1
            distance = abs(coords[1]-y) + abs(coords[0]-x)
            if distance < shortestdist:
                field[x,y] = ic
                shortestdist = distance
            elif distance == shortestdist:
                field[x,y] = 0

edge = []
licount = [0] * len(licoords)

for x, xc in enumerate(field):
    for y, yc in enumerate(xc):
        if yc != 0:
            licount[yc-1] += 1
        if x == 0 or y == 0 or x == xmax-1 or y == ymax-1:
            if yc not in edge:
                edge.append(yc)
maxsize = 0
for i, count in enumerate(licount):
    if count > maxsize and i+1 not in edge:
        maxsize = count

print(maxsize)