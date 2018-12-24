fpath = 'input.txt'

contents = open(fpath,'r').read().splitlines()

instructions = []
completed = []
workers = []
ready = []
t = 0

for line in contents:
    instructions.append([line[5], line[-12]])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Initialize ready set
for c in alphabet:
    addflag = True
    for line in instructions:
        if line[1] == c:
            addflag = False
            break
    if addflag:
        ready.append(c)

def steptime(c):
    return 60 + ord(c) - 64

# Main loop
while len(completed) < len(alphabet):
    # Start work using ready steps
    while len(workers) < 5 and len(ready) > 0:   #While there are idle workers and ready steps
        readytime = list(map(steptime,ready))
        i = readytime.index(min(readytime))
        workers.append([ready.pop(i), readytime.pop(i)])

    # Advance Time
    t += 1
    for worker in list(workers):
        worker[1] -= 1          # Reduce worker time left
        if worker[1] == 0:      # If worker finishes work
            newc = worker[0]
            completed.append(newc)
            workers.remove(worker)
            # Update ready and instructions lists
            for line in list(instructions):
                if line[0] == newc:
                    ready.append(line[1])
                    instructions.remove(line)
            for line in instructions:
                if line[1] in ready:
                    ready.remove(line[1])

print(t)