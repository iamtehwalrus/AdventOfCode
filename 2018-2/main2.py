filepath = 'input.txt'
f = open(filepath, 'r')
contents = f.readlines()
numlines = len(contents)


for index, line in enumerate(contents):
    for index2 in range(index+1, numlines):
        charcount = 0
        for cindex in range(len(line)):
            if contents[index][cindex] != contents[index2][cindex]:
                charcount += 1
            if charcount > 1:
                break
        if charcount == 1:
            print(contents[index], contents[index2])
            str = ''
            for i, c in enumerate(contents[index]):
                if c == contents[index2][i]:
                    str += c
            print(str)
