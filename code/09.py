from functools import lru_cache


with open('9.txt', 'r') as file:
    lines = file.read().strip().split('\n')

heightMap = {}
result1 = 0
for y, line in enumerate(lines):
    for x, val in enumerate(line):
        heightMap[(x, y)] = int(val)
basinSizeOfALowPoint = {}
higherThanCaduceus = 10
for x, y in heightMap:
    height = heightMap[(x, y)]
    if (heightMap.get((x+1, y), higherThanCaduceus) > height and
            heightMap.get((x-1, y), higherThanCaduceus) > height and
            heightMap.get((x, y+1), higherThanCaduceus) > height and
            heightMap.get((x, y-1), higherThanCaduceus) > height):
        basinSizeOfALowPoint[(x, y)] = 0
        result1 += height + 1

print('Part 1:', result1)


@lru_cache
def myLowPoint(x, y):
    if (x, y) in basinSizeOfALowPoint:
        return (x, y)
    if heightMap[(x, y)] == 9:
        return None
    height = heightMap[(x, y)]
    for neigh in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        if heightMap.get(neigh, higherThanCaduceus) < height:
            return myLowPoint(*neigh)


for point in heightMap:
    pointsLowPoint = myLowPoint(*point)
    if pointsLowPoint is not None:
        basinSizeOfALowPoint[pointsLowPoint] += 1
treeBiggestBasins = sorted(basinSizeOfALowPoint.values(), reverse=True)[:3]
print('Part 2:', treeBiggestBasins[0]*treeBiggestBasins[1]*treeBiggestBasins[2])
