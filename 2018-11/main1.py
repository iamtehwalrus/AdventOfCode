import numpy as np

serial = 6392
xmax = 300
ymax = 300

def powerlevel(coords):
    rackid = coords[0] + 10
    powerlevel =rackid * coords[1]
    powerlevel += serial
    powerlevel *= rackid
    powerlevel = int(str(powerlevel).zfill(3)[-3])
    powerlevel -= 5
    return int(powerlevel)

grid = np.zeros((xmax, ymax))

for x, xline in enumerate(grid):
    for y, cell in enumerate(xline):
        grid[x, y] = powerlevel([x+1, y+1])

squaresum = 0
xsquare = 0
ysquare = 0
for x, xline in enumerate(grid):
    for y, cell in enumerate(xline):
        if x <= 297 and y <= 297:
            tmpsum = np.sum(grid[x:x+3, y:y+3])
            if tmpsum > squaresum:
                squaresum = tmpsum
                xsquare = x
                ysquare = y

print(xsquare + 1, ysquare + 1, squaresum)