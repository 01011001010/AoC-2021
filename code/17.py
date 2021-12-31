with open('17.txt', 'r') as file:
    line = file.read().strip()[15:]

x, y = line.split(', y=')
x = list(map(int, x.split('..')))
y = list(map(int, y.split('..')))
if y[0] >= 0 or y[1] >= 0 or x[0] <= 0 or x[1] <= 0:
    print('This algorithm was implemented for only negative ys and positive xs. This does not apply for this input.',
          'Sorry.')
else:
    xR = range(*x)
    yR = range(*y)
    ySpeed = y[0] * (-1)
    print('Part 1:', sum(range(0, ySpeed)))
    yTimes = y[1] - y[0]
    xTimes = x[1] - x[0]

    xSteps = {}
    for i in range(1, x[1]+1):
        position = i
        steps = 1
        initialSpeed = i
        while position <= x[1]:
            if position >= x[0]:
                xSteps[steps] = xSteps.get(steps, set().copy())
                xSteps[steps].add(initialSpeed)
                if steps > 1000:
                    break
            else:
                if i <= 0:
                    break
            i -= 1 if i != 0 else 0
            position += i
            steps += 1
    ySteps = {}
    for i in range(y[0], 0):
        position = i
        steps = 1
        initialSpeed1 = i
        initialSpeed2 = i * (-1) - 1

        upwardsSteps = initialSpeed2 * 2 + 1
        while position >= y[0]:
            if position <= y[1]:
                ySteps[steps] = ySteps.get(steps, set().copy())
                ySteps[steps].add(initialSpeed1)
                ySteps[steps+upwardsSteps] = ySteps.get(steps+upwardsSteps, set().copy())
                ySteps[steps+upwardsSteps].add(initialSpeed2)

            i -= 1
            position += i
            steps += 1
result2 = 0
result2Conditions = set()
for steps, xWays in xSteps.items():
    if steps in ySteps:
        for x in xWays:
            for y in ySteps[steps]:
                result2Conditions.add((x, y))

print('Part 2:', len(result2Conditions))
