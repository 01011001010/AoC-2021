import heapq

with open('15.txt', 'r') as file:
    lines = file.read().strip().split('\n')

maxX = len(lines[0])
maxY = len(lines)
risks = {}
for y, line in enumerate(lines):
    for x, val in enumerate(line):
        for i in 0, 1, 2, 3, 4:
            for j in 0, 1, 2, 3, 4:
                risks[(maxX * i + x, maxY * j + y)] = (int(val) + i + j) if (int(val) + i + j) < 10 else (int(val) + i + j) - 9

riskToGetThere = {(0, 0): 0}

moveFrom = [(0, 0, 0)]
done = set()
while moveFrom:
    value, lastX, lastY = heapq.heappop(moveFrom)
    if (lastX, lastY) not in done:
        for xN, yN in (-1, 0), (1, 0), (0, -1), (0, 1):
            if (0 <= lastX + xN <= x and 0 <= lastY + yN <= y and
                    riskToGetThere.get((lastX + xN, lastY + yN), 999999999) > value + risks[
                        (lastX + xN, lastY + yN)]):
                riskToGetThere[(lastX + xN, lastY + yN)] = value + risks[(lastX + xN, lastY + yN)]
                if (lastX + xN, lastY + yN) not in done:
                    heapq.heappush(moveFrom, (riskToGetThere[(lastX + xN, lastY + yN)], lastX + xN, lastY + yN))
        done.add((lastX, lastY))
    if (x - 1, y) in done and (x, y - 1) in done:
        print('Part 1:', riskToGetThere[x, y])
        break

x2 = maxX * i + x
y2 = maxY * i + y
riskToGetThere = {(0, 0): 0}

moveFrom = [(0, 0, 0)]
done = set()
while moveFrom:
    value, lastX, lastY = heapq.heappop(moveFrom)
    if (lastX, lastY) not in done:
        for xN, yN in (-1, 0), (1, 0), (0, -1), (0, 1):
            if (0 <= lastX + xN <= x2 and 0 <= lastY + yN <= y2 and
                    riskToGetThere.get((lastX + xN, lastY + yN), 999999999) > value + risks[
                        (lastX + xN, lastY + yN)]):
                riskToGetThere[(lastX + xN, lastY + yN)] = value + risks[(lastX + xN, lastY + yN)]
                if (lastX + xN, lastY + yN) not in done:
                    heapq.heappush(moveFrom, (riskToGetThere[(lastX + xN, lastY + yN)], lastX + xN, lastY + yN))
        done.add((lastX, lastY))
    if (x2 - 1, y2) in done and (x2, y2 - 1) in done:
        print('Part 2:', riskToGetThere[x2, y2])
        break
