fpath = 'input.txt'
contents = open(fpath,'r').read().splitlines()

for i, coords in enumerate(contents):
    contents[i] = coords.split(', ')
    print(contents[i])

