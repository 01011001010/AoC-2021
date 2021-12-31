with open('22.txt', 'r') as file:
    initiation = file.read().strip().split('\n')


class Cuboid:
    def __init__(self, x1, x2, y1, y2, z1, z2, on=True):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.on = on

    def doWeIntersect(self, otherCuboid):
        xOverlap = False if ((otherCuboid.x1 < self.x1 and otherCuboid.x2 < self.x1) or
                             (otherCuboid.x1 > self.x2 and otherCuboid.x2 > self.x2)) else True
        yOverlap = False if ((otherCuboid.y1 < self.y1 and otherCuboid.y2 < self.y1) or
                             (otherCuboid.y1 > self.y2 and otherCuboid.y2 > self.y2)) else True
        zOverlap = False if ((otherCuboid.z1 < self.z1 and otherCuboid.z2 < self.z1) or
                             (otherCuboid.z1 > self.z2 and otherCuboid.z2 > self.z2)) else True
        return xOverlap and yOverlap and zOverlap

    def numberOfCubesContained(self):
        return (self.x2 - self.x1 + 1)*(self.y2 - self.y1 + 1)*(self.z2 - self.z1 + 1)

    def intersectAndReturnResultOnCuboids(self, otherCuboid, giveIntersection=False):
        resultCuboids = []
        if self.x1 < otherCuboid.x1 and self.y1 < otherCuboid.y1:
            resultCuboids.append(Cuboid(self.x1, otherCuboid.x1-1, self.y1, otherCuboid.y1-1, self.z1, self.z2))
        if self.x2 > otherCuboid.x2 and self.y1 < otherCuboid.y1:
            resultCuboids.append(Cuboid(otherCuboid.x2+1, self.x2, self.y1, otherCuboid.y1-1, self.z1, self.z2))
        if self.x1 < otherCuboid.x1 and self.y2 > otherCuboid.y2:
            resultCuboids.append(Cuboid(self.x1, otherCuboid.x1-1, otherCuboid.y2+1, self.y2, self.z1, self.z2))
        if self.x2 > otherCuboid.x2 and self.y2 > otherCuboid.y2:
            resultCuboids.append(Cuboid(otherCuboid.x2+1, self.x2, otherCuboid.y2+1, self.y2, self.z1, self.z2))
        x1 = self.x1 if self.x1 > otherCuboid.x1 else otherCuboid.x1
        x2 = self.x2 if self.x2 < otherCuboid.x2 else otherCuboid.x2
        y1 = self.y1 if self.y1 > otherCuboid.y1 else otherCuboid.y1
        y2 = self.y2 if self.y2 < otherCuboid.y2 else otherCuboid.y2
        if self.y1 < otherCuboid.y1:
            resultCuboids.append(Cuboid(x1, x2, self.y1, otherCuboid.y1-1, self.z1, self.z2))
        if self.y2 > otherCuboid.y2:
            resultCuboids.append(Cuboid(x1, x2, otherCuboid.y2+1, self.y2, self.z1, self.z2))
        if self.x1 < otherCuboid.x1:
            resultCuboids.append(Cuboid(self.x1, otherCuboid.x1-1, y1, y2, self.z1, self.z2))
        if self.x2 > otherCuboid.x2:
            resultCuboids.append(Cuboid(otherCuboid.x2+1, self.x2, y1, y2, self.z1, self.z2))
        if self.z1 < otherCuboid.z1:
            resultCuboids.append(Cuboid(x1, x2, y1, y2, self.z1, otherCuboid.z1-1))
        if self.z2 > otherCuboid.z2:
            resultCuboids.append(Cuboid(x1, x2, y1, y2, otherCuboid.z2+1, self.z2))
        if giveIntersection:
            z1 = self.z1 if self.z1 > otherCuboid.z1 else otherCuboid.z1
            z2 = self.z2 if self.z2 < otherCuboid.z2 else otherCuboid.z2
            resultCuboids.append(Cuboid(x1, x2, y1, y2, z1, z2))
        return resultCuboids


printPartOne = True
litCuboids = []
for line in initiation:
    action, coords = line.split(' ')
    x, y, z = coords.split(',')
    x = x[2:].split('..')
    y = y[2:].split('..')
    z = z[2:].split('..')
    if printPartOne and (int(x[0]) < -50 or int(x[0]) > 50):
        res1 = 0
        for finallyLit in litCuboids:
            res1 += finallyLit.numberOfCubesContained()
        print('Part 1:', res1)
        printPartOne = False

    on = True if action == 'on' else False
    if not on:
        newCuboid = Cuboid(int(x[0]), int(x[1]), int(y[0]), int(y[1]), int(z[0]), int(z[1]), on)
        newLitCuboids = []
        for litCube in litCuboids:
            if litCube.doWeIntersect(newCuboid):
                newLitCuboids.extend(litCube.intersectAndReturnResultOnCuboids(newCuboid))
            else:
                newLitCuboids.append(litCube)
    else:
        newLitCuboids = litCuboids.copy()
        newCuboidParts = [Cuboid(int(x[0]), int(x[1]), int(y[0]), int(y[1]), int(z[0]), int(z[1]), on)]
        while newCuboidParts:
            nowIntersecting = newCuboidParts.pop()
            if litCuboids:
                for litCube in litCuboids:
                    if litCube.doWeIntersect(nowIntersecting):
                        break
                if litCube.doWeIntersect(nowIntersecting):
                    newCuboidParts.extend(nowIntersecting.intersectAndReturnResultOnCuboids(litCube))
                else:
                    newLitCuboids.append(nowIntersecting)
            else:
                newLitCuboids.append(nowIntersecting)

    litCuboids = newLitCuboids

res2 = 0
for finallyLit in litCuboids:
    res2 += finallyLit.numberOfCubesContained()

print('Part 2:', res2)
