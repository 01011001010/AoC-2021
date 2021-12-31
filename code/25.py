with open('25.txt', 'r') as file:
    lines = file.read().strip().split('\n')

maxX = len(lines[0])
maxY = len(lines)

eastFacingSeaCucumbers = set()
southFacingSeaCucumbers = set()
for y, line in enumerate(lines):
    for x, whatIsThere in enumerate(line):
        if whatIsThere == '>':
            eastFacingSeaCucumbers.add((x, y))
        elif whatIsThere == 'v':
            southFacingSeaCucumbers.add((x, y))


numberMovedInLastStep = True
step = 0
while numberMovedInLastStep:
    numberMovedInLastStep = 0
    newEastFacingSeaCucumbers = set()
    for eastFacingSeaCucumber in eastFacingSeaCucumbers:
        moveToX, moveToY = eastFacingSeaCucumber
        moveToX += 1
        if moveToX == maxX:
            moveToX = 0
        if ((moveToX, moveToY) not in eastFacingSeaCucumbers
                and (moveToX, moveToY) not in southFacingSeaCucumbers):
            newEastFacingSeaCucumbers.add((moveToX, moveToY))
            numberMovedInLastStep += 1
        else:
            newEastFacingSeaCucumbers.add(eastFacingSeaCucumber)
    newSouthFacingSeaCucumbers = set()
    for southFacingSeaCucumber in southFacingSeaCucumbers:
        moveToX, moveToY = southFacingSeaCucumber
        moveToY += 1
        if moveToY == maxY:
            moveToY = 0
        if ((moveToX, moveToY) not in newEastFacingSeaCucumbers
                and (moveToX, moveToY) not in southFacingSeaCucumbers):
            newSouthFacingSeaCucumbers.add((moveToX, moveToY))
            numberMovedInLastStep += 1
        else:
            newSouthFacingSeaCucumbers.add(southFacingSeaCucumber)

    eastFacingSeaCucumbers = newEastFacingSeaCucumbers
    southFacingSeaCucumbers = newSouthFacingSeaCucumbers
    step += 1

print('Part 1:', step)
