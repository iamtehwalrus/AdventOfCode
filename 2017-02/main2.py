import csv

sum = 0

f = open("input.txt", "r")
data = list(csv.reader(f, delimiter='\t'))

for linestr in data:
    line = list(map(int, linestr))
    breakflag = False
    for i, value in enumerate(line):
        for j in range(i+1,len(line)):
            if value % line[j] == 0:
                sum += value / line[j]
                breakflag = True
                break
            if line[j] % value == 0:
                sum += line[j] / value
                breakflag = True
                break
        if breakflag:
            break


print(sum)