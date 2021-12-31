with open('24.txt', 'r') as file:
    lines = list(map(lambda a: a.split(' '), file.read().strip().split('\n')))

# This whole solution rests upon the educated guess that all inputs are the same with only differing values in
# significant three places of each block of the input

first = [int(lines[inp+5][2]) for inp in range(0, len(lines), 18)]
second = [int(lines[inp+15][2]) for inp in range(0, len(lines), 18)]
divideZs = [int(lines[inp+4][2]) for inp in range(0, len(lines), 18)]

conditions = []
stack = [(0, second[0])]
for i in range(1, 14):
    if divideZs[i] == 26:
        eql = stack.pop()
        conditions.append((i, eql[0], eql[1]+first[i]))
    else:
        stack.append((i, second[i]))

res1 = [None] * 14
res2 = [None] * 14
for lhs, rhs, plus in conditions:
    for digit in range(1, 10):
        if (digit == 9 and digit - plus < 9) or digit - plus == 9:
            res1[lhs] = digit
            res1[rhs] = digit - plus
        if (digit == 1 and digit - plus > 0) or digit - plus == 1:
            res2[lhs] = digit
            res2[rhs] = digit - plus

print('Part 1:', ''.join(map(str, res1)))
print('Part 2:', ''.join(map(str, res2)))
