import re
import datetime
import operator

fpath = 'input.txt'
f = open(fpath,'r')

contents = f.read().splitlines()

def parseline(linestr):
    line = []
    year = int(linestr[1:5])
    month = int(linestr[6:8])
    day = int(linestr[9:11])
    hour = int(linestr[12:14])
    min = int(linestr[15:17])
    timevalue = datetime.datetime(year, month, day, hour, min)
    d = datetime.datetime(1518,1,1)                         # Jan 1, 1518
    line.append(int((timevalue - d).total_seconds()/60))    # Date Time Value in minutes: Index 0

    match = re.search('#(\d+)', linestr)
    if match:
        line.append(int(match.group(1)))    # Guard #: Index 1
        line.append(0)                      # Wake/Asleep: Index 2
    else:
        line.append(False)
        if re.search('falls asleep', linestr):
            line.append(1)
        elif re.search('wakes up', linestr):
            line.append(-1)
        else:
            print('Error')
            sys.exit(0)
    return line

def sortcontents(loglist):
    sortedlist = sorted(loglist, key=lambda a:a[0])
    return sortedlist

for index, line in enumerate(contents):
    contents[index] = parseline(line)

#Sort
contents = sortcontents(contents)

guardlog = {}

#Fill in guard # for all log lines
for index, line in enumerate(contents):
    if line[1]:                         # If line states Guard #
        guardnum = line[1]
    else:                               # Else line states wake or asleep
        line[1] = guardnum              # Add guard # to the line
        if line[2] == 1:                # If guard fell asleep
            timeasleep = contents[index+1][0] - contents[index][0]
            if guardnum in guardlog:     # If guard # is already in guard log dictionary
                guardlog[guardnum] += timeasleep
            else:
                guardlog[guardnum] = timeasleep

# Find guard with most sleep
(maxguard, maxasleep) = max(guardlog.items(), key=operator.itemgetter(1))

minutes = [0] * 60
for index, line in enumerate(contents):
    if line[1] == maxguard and line[2] == 1:
        sleepminute = contents[index][0] % 60
        wakeminute = contents[index+1][0] % 60
        minutes[sleepminute:wakeminute] = [x+1 for x in minutes[sleepminute:wakeminute]]

maxtimes = max(minutes)
for index, numtimes in enumerate(minutes):
    if numtimes == maxtimes:
        m = index
        break

print(maxguard * m)