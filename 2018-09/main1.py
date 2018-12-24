fpath = 'input.txt'

contents = open(fpath, 'r').readline().split()
contents = [int(s) for s in contents if s.isdigit()]

numplayers = contents[0]
nummarbles = contents[1] + 1

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
        i = (i - 6) % len(circle)
        if i == 0:
            players[p] += circle.pop(-1)
        else:
            players[p] += circle.pop(i-1)
            i -= 1
    p = (p + 1) % len(players)

print(max(players))