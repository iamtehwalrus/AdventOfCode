fpath = 'input.txt'

contents = open(fpath, 'r').read().split(' ')
contents = list(map(int, contents))

global mdsum
mdsum = 0

def dig(chlist):
	global mdsum
	while chlist[0] > 0:
		chlist[:] = chlist[0:2] + dig(chlist[2:])
		chlist[0] -= 1

	while chlist[1] > 0:
		mdsum += chlist.pop(2)
		chlist[1] -= 1

	chlist[:] = chlist[2:]
	return chlist

dig(contents)
print(mdsum)