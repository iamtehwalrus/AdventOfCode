fpath = 'input.txt'

contents = open(fpath,'r').read().splitlines()

instructions = []

for line in contents:
    instructions.append([line[5], line[-12]])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

completed = []
ready = set()

# Initialize ready set
for c in alphabet:
    addflag = True
    for line in instructions:
        if line[1] == c:
            addflag = False
            break
    if addflag:
        ready.add(c)

def sortpop(ready):
    for c in alphabet:
        if c in ready:
            ready.remove(c)
            return c

while len(ready) > 0:
    cnew = sortpop(ready)
    completed.append(cnew)

    # Add potential new ready letters and modify instructions
    liremove = []
    for i, line in enumerate(instructions):
        if line[0] in completed:
            ready.add(line[1])
            liremove.append(i)
    liremove.reverse()
    for i in liremove:
        instructions.pop(i)

    # Remove the restricted letters again
    for line in instructions:
        if line[1] in ready:
            ready.remove(line[1])

str = ''.join(completed)
print(str)