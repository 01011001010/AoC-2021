with open('6.txt', 'r') as file:
    numbers = list(map(int, file.read().strip().split(',')))

days1 = 80
days2 = 256 - days1
state = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for fish in numbers:
    state[fish] += 1

for day in range(days1):
    state[0], state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8] = state[1], state[2], state[3], state[4], state[5], state[6], state[7]+state[0], state[8], state[0]

print('Part 1:', sum(state.values()))

for day in range(days2):
    state[0], state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8] = state[1], state[2], state[3], state[4], state[5], state[6], state[7]+state[0], state[8], state[0]

print('Part 2:', sum(state.values()))
