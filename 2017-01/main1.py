list1 = []
list2 = []

sum = 0

f = open("input.txt", "r")
for c in str(f.read()):
    list1.append(c)
f.close()

list2 = list1.copy()
list2.pop(0)
list2.append(list1[0])

for i,c in enumerate(list1):
    if int(list1[i]) == int(list2[i]):
        sum += int(list1[i])

print(sum)