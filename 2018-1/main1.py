frequency = 0

with open("frequencyinput.txt","r") as f:
    for line in f:
        frequency += float(line)

print(frequency)