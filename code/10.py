with open('10.txt', 'r') as file:
    lines = file.read().strip().split('\n')

scores = {')': 3, ']': 57, '}': 1197, '>': 25137, '(': 1, '[': 2, '{': 3, '<': 4}
syntaxErrorScore = 0
completionScores = []

for line in lines:
    stack = []
    corrupted = False
    lineCompletionScore = 0
    for character in line:
        if character in '<{([':
            stack.append(character)
        else:
            fromStack = stack.pop()
            if not((character == '>' and fromStack == '<') or
                   (character == ']' and fromStack == '[') or
                   (character == ')' and fromStack == '(') or
                   (character == '}' and fromStack == '{')):
                syntaxErrorScore += scores[character]
                corrupted = True
                break
    if not corrupted:
        for character in reversed(stack):
            lineCompletionScore *= 5
            lineCompletionScore += scores[character]
    if lineCompletionScore != 0:
        completionScores.append(lineCompletionScore)
print('Part1 :', syntaxErrorScore)
print('Part2 :', sorted(completionScores)[len(completionScores)//2])
