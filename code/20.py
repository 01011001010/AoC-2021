with open('20.txt', 'r') as file:
    imageEnhancementAlgorithmString, image = file.read().strip().split('\n\n')


def enhance(steps):
    imagePixels = {}
    for y, line in enumerate(image.split()):
        for x, val in enumerate(line):
            imagePixels[(x, y)] = 1 if val == '#' else 0
    minX, maxX, minY, maxY = 0, x, 0, y

    result = 0
    for step in range(steps):
        minX, maxX, minY, maxY = minX - 1, maxX + 1, minY - 1, maxY + 1
        newImagePixels = {}
        getNum = 1 if step % 2 == 1 and imageEnhancementAlgorithmString[0] == '#' else 0
        for pixX in range(minX, maxX+1):
            for pixY in range(minY, maxY + 1):
                index = 0
                for power, pixel in enumerate(((pixX+1, pixY+1), (pixX, pixY+1), (pixX-1, pixY+1),
                                               (pixX+1, pixY), (pixX, pixY), (pixX-1, pixY),
                                               (pixX+1, pixY-1), (pixX, pixY-1), (pixX-1, pixY-1))):
                    index += imagePixels.get(pixel, getNum) * 2**power
                newImagePixels[pixX, pixY] = 1 if imageEnhancementAlgorithmString[index] == '#' else 0
                if step == steps-1 and newImagePixels[pixX, pixY] == 1:
                    result += 1
        imagePixels = newImagePixels
        # uncomment to view each iteration (lit up edges do not show)
        # numToChar = {0: '.', 1: '#'}
        # for y in range(minY, maxY + 1):
        #     for x in range(minX, maxX + 1):
        #         print(numToChar[imagePixels[x, y]], end='')
        #     print()
    return result


if imageEnhancementAlgorithmString[0] != '#' or imageEnhancementAlgorithmString[0] != '#':
    print('This algorithm was implemented with the assumption that 000000000 translates to \'#\' and 111111111',
          'to \'.\'. This does not apply for this input. Sorry.')
else:
    print('Part 1:', enhance(2))
    print('Part 2:', enhance(50))
