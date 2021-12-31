with open('13.txt', 'r') as file:
    dots, folds = map(lambda x: x.split('\n'), file.read().strip().split('\n\n'))

currentDots = set(map(lambda x: tuple(map(int,x.split(','))), dots))
size = [0, 0]
for fold in folds:

    axis, value = fold.split('=')
    value = int(value)
    if axis[-1] == 'x':
        for x, y in currentDots.copy():
            if x > value:
                currentDots.add((2*value-x, y))
                currentDots.remove((x, y))
    if axis[-1] == 'y':
        for x, y in currentDots.copy():
            if y > value:
                currentDots.add((x, 2*value-y))
                currentDots.remove((x, y))
    if fold == folds[0]:
        print('Part 1:',len(currentDots))

print('Part 2:')
for y in range(6):
    for x in range(39):
        print('#' if (x, y) in currentDots else '.', end=' ')
    print()
