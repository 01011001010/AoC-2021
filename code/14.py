with open('14.txt', 'r') as file:
    polymer, insertions = file.read().strip().split('\n\n')

pairs = {}
for i in range(len(polymer)-1):
    pairs[polymer[i:i+2]] = pairs.get(polymer[i:i+2], 0)
    pairs[polymer[i:i + 2]] += 1
insertions = dict(map(lambda x: x.split(' -> '), insertions.split('\n')))


steps = 10
for step in range(steps):
    newPairs = {}
    for pair, number in pairs.items():
        newPairs[pair[0] + insertions[pair]] = newPairs.get(pair[0] + insertions[pair], 0)
        newPairs[insertions[pair] + pair[1]] = newPairs.get(insertions[pair] + pair[1], 0)
        newPairs[pair[0]+insertions[pair]] += number
        newPairs[insertions[pair] + pair[1]] += number
    pairs = newPairs

elementCounts = {}
for pair, number in pairs.items():
    elementCounts[pair[0]] = elementCounts.get(pair[0], 0)
    elementCounts[pair[1]] = elementCounts.get(pair[1], 0)
    elementCounts[pair[0]] += number
    elementCounts[pair[1]] += number
elementCounts[polymer[0]] += 1
elementCounts[polymer[-1]] += 1
for element in elementCounts:
    elementCounts[element] //= 2

print('Part 1:', max(elementCounts.values())-min(elementCounts.values()))
steps = 30
for step in range(steps):
    newPairs = {}
    for pair, number in pairs.items():
        newPairs[pair[0] + insertions[pair]] = newPairs.get(pair[0] + insertions[pair], 0)
        newPairs[insertions[pair] + pair[1]] = newPairs.get(insertions[pair] + pair[1], 0)
        newPairs[pair[0]+insertions[pair]] += number
        newPairs[insertions[pair] + pair[1]] += number
    pairs = newPairs

elementCounts = {}
for pair, number in pairs.items():
    elementCounts[pair[0]] = elementCounts.get(pair[0], 0)
    elementCounts[pair[1]] = elementCounts.get(pair[1], 0)
    elementCounts[pair[0]] += number
    elementCounts[pair[1]] += number
elementCounts[polymer[0]] += 1
elementCounts[polymer[-1]] += 1
for element in elementCounts:
    elementCounts[element] //= 2

print('Part 2:', max(elementCounts.values())-min(elementCounts.values()))
