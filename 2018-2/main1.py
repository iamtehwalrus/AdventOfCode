filepath = 'input.txt'

cnt2 = 0
cnt3 = 0
with open(filepath) as f:
    line = f.readline()
    while line:
        flag2 = False
        flag3 = False
        for c in line:
            if not flag2 and line.count(c) == 2:
                cnt2 += 1
                flag2 = True
            if not flag3 and line.count(c) == 3:
                cnt3 += 1
                flag3 = True
        line = f.readline()

print(cnt2 * cnt3)