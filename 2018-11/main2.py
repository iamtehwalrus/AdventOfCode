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
szsquare = 1

for sz in range(1, min(xmax, ymax)):
    for x, xline in enumerate(grid):
        for y, cell in enumerate(xline):
            if x <= xmax-sz and y <= ymax-sz:
                tmpsum = np.sum(grid[x:x+sz, y:y+sz])
                if tmpsum > squaresum:
                    squaresum = tmpsum
                    xsquare = x
                    ysquare = y
                    szsquare = sz

print(xsquare + 1, ysquare + 1, szsquare, squaresum)