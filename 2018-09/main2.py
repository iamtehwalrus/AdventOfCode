fpath = 'input.txt'

contents = open(fpath, 'r').readline().split()
contents = [int(s) for s in contents if s.isdigit()]
open(fpath).close()

numplayers = contents[0]
nummarbles = (contents[1]*100) + 1

players = [0] * numplayers
circle = [0]                # Clockwise is positive direction
p = 0
i = 0

for m in range(1, nummarbles):
    if m % 23 != 0:
        i = (i + 2) % len(circle)
        circle.insert(i, m)
    else:
        players[p] += m
        i = (i - 7) % len(circle)
        players[p] += circle.pop(i)
        i = i % len(circle)
    p = (p + 1) % len(players)
    print('%s of %s' % ('{:,}'.format(m), '{:,}'.format(nummarbles-1)))

open('output.txt', 'a').write('\n'+str(max(players)))
open('output.txt').close()