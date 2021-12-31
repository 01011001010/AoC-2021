with open('8.txt', 'r') as file:
    lines = file.read().strip().split('\n')

result1 = 0
result2 = 0
for line in lines:
    signalPattern, output = line.split(' | ')
    timesLit = {}
    whatIsWhat = {}
    with5Lit = []
    for number in signalPattern.split(' '):
        if len(number) == 2:
            one = set(number)
        elif len(number) == 3:
            seven = set(number)
        elif len(number) == 4:
            four = set(number)
        elif len(number) == 5:
            with5Lit.append(set(number))
    whatIsWhat['a'] = list(seven - one)[0]
    for character in 'abcdefg':
        n = signalPattern.count(character)
        if n == 4:
            whatIsWhat['e'] = character
        elif n == 9:
            whatIsWhat['f'] = character
        elif n == 6:
            whatIsWhat['b'] = character
        elif n == 7 and character not in four:
            whatIsWhat['g'] = character
        elif n == 7 and character in four:
            whatIsWhat['d'] = character
        elif n == 8 and character != list(seven - one)[0]:
            whatIsWhat['c'] = character
    outputStr = ''
    for number in output.split(' '):
        if len(number) == 2:
            outputStr += '1'
            result1 += 1
        elif len(number) == 3:
            outputStr += '7'
            result1 += 1
        elif len(number) == 4:
            outputStr += '4'
            result1 += 1
        elif len(number) == 7:
            outputStr += '8'
            result1 += 1
        else:
            if whatIsWhat['d'] not in number:
                outputStr += '0'
            elif whatIsWhat['e'] not in number and len(number) == 6:
                outputStr += '9'
            elif len(number) == 6:
                outputStr += '6'
            elif whatIsWhat['e'] in number:
                outputStr += '2'
            elif whatIsWhat['c'] in number:
                outputStr += '3'
            else:
                outputStr += '5'

    result2 += int(outputStr)

print('Part 1:', result1)
print('Part 2:', result2)
