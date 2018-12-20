fpath = 'input.txt'
f = open(fpath,'r')
originalpolymer = f.read()
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

bestc = ''
fewestreacts = len(originalpolymer)

for removec in 'abcdefghijklmnopqrstuvwxyz':
    polymer = originalpolymer
    polymer = polymer.replace(removec,'').replace(removec.upper(),'')

    newreactions = 1
    while newreactions:
        (polymer, newreactions) = react(polymer)
    print(removec, len(polymer))
    if len(polymer) < fewestreacts:
        bestc = removec
        fewestreacts = len(polymer)

print(bestc, fewestreacts)