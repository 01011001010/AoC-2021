with open('3.txt', 'r') as file:
    rawLines = file.read().strip().split()

lines = list(map(lambda x: int(x, 2), rawLines))
nOfLines = len(lines)
nOfOnes = [0]*len(rawLines[0])
for line in lines:
    for i in range(len(nOfOnes)-1, -1, -1):
        if 2**i & line:
            nOfOnes[i] += 1

gammaRate = 0
epsilonRate = 0
for i, count in enumerate(nOfOnes):
    if count >= nOfLines/2:
        gammaRate += 2 ** i
    if count <= nOfLines/2:
        epsilonRate += 2 ** i
print('Part 1:', gammaRate*epsilonRate)


def filterTheMostOrLeastCommonAtPositionOutOf(numbers, power, most=True):
    count = 0
    all = len(numbers)
    ones = []
    zeros = []
    for number in numbers:
        if 2 ** power & number:
            count += 1
            ones.append(number)
        else:
            zeros.append(number)
    if most:
        if count >= all/2:
            return ones
        return zeros
    else:
        if count >= all/2:
            return zeros
        return ones


nOfBits = len(nOfOnes)
now = lines
for i in range(len(nOfOnes)):
    now = filterTheMostOrLeastCommonAtPositionOutOf(now, nOfBits - 1 - i)
    if len(now) == 1:
        oxygenGeneratorRating = now[0]
        break
now = lines

for i in range(len(nOfOnes)):
    now = filterTheMostOrLeastCommonAtPositionOutOf(now, nOfBits - 1 - i, False)
    if len(now) == 1:
        CO2ScrubberRating = now[0]
        break

print('Part 2:', oxygenGeneratorRating*CO2ScrubberRating)
