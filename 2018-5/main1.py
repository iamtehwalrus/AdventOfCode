fpath = 'input.txt'
f = open(fpath,'r')
polymer = f.read()
reactions = 0
stopflag = False

def react(polymer):
    reactionindex = []
    enumpolymer = enumerate(polymer)
    for i, c in enumpolymer:
        if c.isupper():
            cswitch = c.lower()
        else:
            cswitch = c.upper()
        if polymer[i:i+2] == c+cswitch:
            reactionindex = [i] + reactionindex     # Append index to list in reverse order
            next(enumpolymer)

    for rindex in reactionindex:
        polymer = polymer[:rindex] + polymer[rindex+2:]
    return (polymer, len(reactionindex))

newreactions = 1
while newreactions:
    (polymer, newreactions) = react(polymer)

print(len(polymer))