with open('4.txt', 'r') as file:
    drawn, *boards = file.read().strip().split('\n\n')
drawn = list(map(int, drawn.split(',')))

locationsOfNumbers = {}
stateOfBoards = {}
for boardI, board in enumerate(boards):
    stateOfBoards[boardI] = []
    stateOfBoards[boardI].append([0] * 5)
    stateOfBoards[boardI].append([0] * 5)
    stateOfBoards[boardI].append(0)
    for lineI, lineNumbers in enumerate(map(lambda x: list(map(int, x.replace('  ', ' ').split(' ') if x[0] != ' ' else
                                                               x[1:].replace('  ', ' ').split(' '))),
                                            board.split('\n'))):
        for colI, number in enumerate(lineNumbers):

            locationsOfNumbers[number] = locationsOfNumbers.get(number, [].copy())
            locationsOfNumbers[number].append((boardI, lineI, colI))
            stateOfBoards[boardI][2] += number


def simulateTheGame():
    won = True
    boardsToWin = set(range(len(boards)))
    for draw in drawn:
        for boardI, lineI, colI in locationsOfNumbers[draw]:
            stateOfBoards[boardI][2] -= draw
            if (stateOfBoards[boardI][0][lineI] == 4 or stateOfBoards[boardI][1][colI] == 4) and boardI in boardsToWin:
                boardsToWin.discard(boardI)
                if won:
                    print('Part 1:', draw * stateOfBoards[boardI][2])
                    won = False
                score = draw * stateOfBoards[boardI][2]
                if len(boardsToWin) == 0:
                    print('Part 2:', score)
                    return

            stateOfBoards[boardI][0][lineI] += 1
            stateOfBoards[boardI][1][colI] += 1


simulateTheGame()
