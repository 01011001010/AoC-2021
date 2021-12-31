with open('5.txt', 'r') as file:
    lines = list(map(lambda a: sorted(map(lambda b: list(map(int, b.split(','))), a.split(' -> '))), file.read().strip().split('\n')))

freq = {}

for line in lines:
    if line[0][0] == line[1][0]:
        for y in range(line[0][1], line[1][1]+1):
            if (line[0][0], y) not in freq:
                freq[(line[0][0], y)] = [1, 1]
            else:
                freq[(line[0][0], y)][0] += 1
                freq[(line[0][0], y)][1] += 1
    else:
        currY = line[0][1]
        yDif = 0
        if line[0][1] != line[1][1]:
            yDif = -1 if line[0][1] > line[1][1] else 1
        for x in range(line[0][0], line[1][0]+1):
            if (x, currY) not in freq:
                freq[(x, currY)] = [1, 1] if yDif == 0 else [0, 1]
            else:
                if yDif == 0:
                    freq[(x, currY)][0] += 1
                freq[(x, currY)][1] += 1
            currY += yDif

result1 = 0
result2 = 0

for count1, count2 in freq.values():
    if count1 > 1:
        result1 += 1
        result2 += 1
    elif count2 > 1:
        result2 += 1

print('Part 1:', result1)
print('Part 2:', result2)
