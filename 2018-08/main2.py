fpath = 'input.txt'

contents = open(fpath, 'r').read().split(' ')
contents = list(map(int, contents))

class Node:
	def __init__(self, mylist):
		self.list = list(mylist)

		self.cnodes = []
		self.numchildren = self.list[0]
		self.nummd = self.list[1]

		self.md = self.list[-self.nummd:]
		self.length = len(self.list)

	def value(self):
		value = 0
		if self.numchildren == 0:
			value = sum(self.md)
		else:
			for i in self.md:
				try:
					value += self.cnodes[i-1].value()
				except:
					pass
		return value

def dig(mylist):				# Returns Node class with identified children nodes
	numchildren = mylist[0]
	cnodes = []
	for n in range(numchildren):
		i = 2 + sum([cnode.length for cnode in cnodes])
		templist = mylist[i:]
		newnode = dig(templist)
		cnodes.append(newnode)
	j = 2 + sum([cnode.length for cnode in cnodes]) + mylist[1]
	currentnode = Node(mylist[:j])
	currentnode.cnodes = cnodes

	return currentnode

mainnode = dig(contents)
print(mainnode.value())