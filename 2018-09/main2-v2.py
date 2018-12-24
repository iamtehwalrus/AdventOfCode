fpath = 'input.txt'

contents = open(fpath, 'r').readline().split()
contents = [int(s) for s in contents if s.isdigit()]
open(fpath).close()

numplayers = contents[0]
nummarbles = (contents[1]*100) + 1

class Marble:
    def __init__(self, value=0, prev=None, next=None):
        self.val = value
        self.prev = prev
        self.next = next

class CircleList:
    def __init__(self):
        self.current = None

    def insert2cw(self, m):
        up = self.current.next.next
        down = self.current.next
        down.next = m
        m.prev = down
        m.next = up
        up.prev = m
        self.current = m

    def popccw(self, m):
        count = m.val
        tmp = self.current
        for i in range(7):
            tmp = tmp.prev
        down = tmp.prev
        up = tmp.next
        count += tmp.val
        down.next = up
        up.prev = down
        self.current = up
        return count

circle = CircleList()
startmarble = Marble(0)
startmarble.prev = startmarble
startmarble.next = startmarble
circle.current = startmarble

players = [0] * numplayers
p = 0

for m in range(1, nummarbles):
    newmarble = Marble(m)
    if m % 23 != 0:
        circle.insert2cw(newmarble)
    else:
        players[p] += circle.popccw(newmarble)
    p = (p + 1) % len(players)

print(max(players))