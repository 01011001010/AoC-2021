with open('2.txt', 'r') as file:
    lines = list(map(lambda x: list(x.split()), file.read().strip().split('\n')))

depth1 = 0
position1 = 0
depth2 = 0
position2 = 0
aim2 = 0

for direction, number in lines:
    if direction == 'forward':
        position1 += int(number)
        position2 += int(number)
        depth2 += int(number)*aim2
    elif direction == 'up':
        if depth1 == 0:
            print('This wants to fly!')
        else:
            depth1 -= int(number)
            aim2 -= int(number)
    else:
        depth1 += int(number)
        aim2 += int(number)

print('Part 1:', depth1 * position1)
print(f'(for depth: {depth1} and position: {position1})')

print('Part 2:', depth2 * position2)
print(f'(for depth: {depth2} and position: {position2})')