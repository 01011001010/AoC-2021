with open('12.txt', 'r') as file:
    lines = file.read().strip().split('\n')

bigCaves = set()
smallCaves = set()
connections = {}

for cave1, cave2 in map(lambda x: x.split('-'), lines):
    connections[cave1] = connections.get(cave1, set().copy())
    connections[cave2] = connections.get(cave2, set().copy())
    connections[cave1].add(cave2)
    connections[cave2].add(cave1)
    if cave1.isupper():
        bigCaves.add(cave1)
    else:
        smallCaves.add(cave1)
    if cave2.isupper():
        bigCaves.add(cave2)
    else:
        smallCaves.add(cave2)
result1 = 0
canContinue = {('start', ), }
while canContinue:
    willContinue = set()
    for path in canContinue:
        for connection in connections[path[-1]]:
            if connection == 'end':
                result1 += 1
            elif connection in bigCaves or (connection in smallCaves and connection not in path):
                willContinue.add(tuple([*path, connection]))
    canContinue = willContinue

print('Part 1:', result1)

result2 = 0
canContinue = {(True, 'start'), }
while canContinue:
    willContinue = set()
    for path in canContinue:
        for connection in connections[path[-1]]:
            if connection == 'end':
                result2 += 1
            elif connection in bigCaves:
                willContinue.add(tuple([*path, connection]))
            elif connection in smallCaves:
                if connection not in path:
                    willContinue.add(tuple([*path, connection]))
                elif path[0] and connection not in ('end', 'start'):
                    willContinue.add(tuple([False, *path[1:], connection]))

    canContinue = willContinue

print('Part 2:', result2)
