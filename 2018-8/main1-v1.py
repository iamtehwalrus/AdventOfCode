fpath = 'input.txt'

contents = open(fpath, 'r').read().split(' ')

class Node:
	def __splitchildnodes(self, childrenlist, numchildren):
		childnodes = []

		if numchildren == 1:
			childnodes.append(Node(childrenlist))
			return childnodes
		else:




	def __init__(self, inputlist):
		self.mylist = list(inputlist)
		self.length = len(mylist)

		numchildren = listcopy[0]
		nummetadata = listcopy[1]

		# Metadata
		if nummetadata == 0:
			self.metadata = []
		else:
			self.metadata = self.mylist[-nummetadata:]

		# Children Node
		if numchildren == 0:
			self.childnodes = []
		else:
			self.childnodes = self.__splitchildnodes(self.mylist[2:-len(self.metadata)], numchildren)


def getmetadata(node):
	nummetadata = node[1]
	if nummetadata == 0:
		return []
	else:
		return node[-nummetadata:]

