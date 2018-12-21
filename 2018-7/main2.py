fpath = 'input.txt'

contents = open(fpath,'r').read().splitlines()

instructions = []

for line in contents:
    instructions.append([line[5], line[-12]])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

