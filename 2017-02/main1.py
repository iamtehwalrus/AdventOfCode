import csv

checksum = 0

f = open("input.txt", "r")
data = list(csv.reader(f, delimiter='\t'))

for line in data:
    lineint = list(map(int, line))
    checksum += max(lineint) - min(lineint)


print(checksum)