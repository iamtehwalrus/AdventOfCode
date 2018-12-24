sum = 0
digits = []

f = open("input.txt", "r")
for c in str(f.read()):
    digits.append(c)
f.close()

length = len(digits)

for i,c in enumerate(digits):
    index = int((i + length/2) % length)
    if int(digits[i]) == int(digits[index]):
        sum += int(c)

print(sum)