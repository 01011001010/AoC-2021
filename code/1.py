with open('1.txt', 'r') as file:
    lines = list(map(int, file.read().strip().split()))

result1 = 0
for i, n in enumerate(lines[1:]):
    if n > lines[i]:
        result1 += 1
print('Part 1:', result1)

result2 = 0
window = sum(lines[:3])
for i, n in enumerate(lines[3:]):
    nextWindow = window + n - lines[i]
    if nextWindow > window:
        result2 += 1
    window = nextWindow
print('Part 2:', result2)
