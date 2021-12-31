with open('11.txt', 'r') as file:
    lines = file.read().strip().split('\n')

octopi = {}
for y, line in enumerate(lines):
    for x, val in enumerate(line):
        octopi[(x, y)] = int(val)

result1 = 0
count = True
steps = 100
for step in range(500):
    checkIfFlash = set(octopi.keys())
    toFlash = set()
    while checkIfFlash:
        flashWave = set()
        for x, y in checkIfFlash:
            octopi[(x, y)] += 1
            if octopi[(x, y)] > 9:
                flashWave.add((x, y))

        toFlash.update(flashWave)
        checkIfFlash.clear()
        for x, y in flashWave:
            for neighbour in (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1):
                if neighbour not in toFlash and neighbour in octopi:
                    octopi[neighbour] += 1
                    if octopi[neighbour] > 9:
                        checkIfFlash.add(neighbour)

        for octopus in toFlash:
            result1 += 1
            octopi[octopus] = 0
    if count:
        if step == steps-1:
            count = False
            print('Part 1:', result1)

    if len(toFlash) == len(octopi):
        print('Part 2:', step+1)
        break
