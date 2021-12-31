with open('21.txt', 'r') as file:
    words = file.read().strip().split()


class DeterministicD100:
    def __init__(self):
        self.lastRoll = 0
        self.timesRolled = 0

    def roll(self):
        self.lastRoll += 3
        self.timesRolled += 3
        return (self.lastRoll - 1) * 3

    def numberOfRolls(self):
        return self.timesRolled


positions = {1: int(words[4]), 2: int(words[9])}
score = {1: 0, 2: 0}
die = DeterministicD100()
player = 1
while score[1] < 1000 and score[2] < 1000:
    positions[player] += die.roll()
    positions[player] %= 10
    positions[player] = 10 if positions[player] == 0 else positions[player]
    score[player] += positions[player]
    player = 2 if player == 1 else 1


print('Part 1:', die.numberOfRolls()*min(score.values()))


def nextTurn(player, pos1, pos2, sco1, sco2, nOfUni):
    if sco1 >= 21:
        return nOfUni, 0
    if sco2 >= 21:
        return 0, nOfUni
    if player == 1:
        res = [0, 0]
        for roll, nOfUniverses in (3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1):
            pos = pos1 + roll
            pos %= 10
            pos = 10 if pos == 0 else pos
            sco = sco1 + pos
            re = nextTurn(2, pos, pos2, sco, sco2, nOfUni*nOfUniverses)
            res[0] += re[0]
            res[1] += re[1]
        return res
    res = [0, 0]
    for roll, nOfUniverses in (3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1):
        pos = pos2 + roll
        pos %= 10
        pos = 10 if pos == 0 else pos
        sco = sco2 + pos
        re = nextTurn(1, pos1, pos, sco1, sco, nOfUni * nOfUniverses)
        res[0] += re[0]
        res[1] += re[1]
    return res


print('Part 2:', max(nextTurn(1, int(words[4]), int(words[9]), 0, 0, 1)))
