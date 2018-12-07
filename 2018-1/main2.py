frequency = 0
history = set()
history.add(frequency)
answer = 0
iter = 0
found = False

def processfile(freq, hist, found):
    with open("frequencyinput.txt", "r") as f:
        for line in f:
            freq += int(line)
            if freq in hist:
                found = True
                return freq, hist, found
                break
            else:
                hist.add(freq)
    return freq, hist, found

for iter in range(150):
    frequency, history, found = processfile(frequency,history, found)
    if found == True:
        print(frequency)
        break