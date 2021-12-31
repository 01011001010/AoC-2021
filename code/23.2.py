from collections import deque
from time import time


with open('23.2.txt', 'r') as file:
    lines = file.read().strip().split()

timeToEndAndAssumeOptimum = 2

energyCost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
hallway = [None] * (len(lines[1])-2)
roomA = [lines[2][3], lines[3][1], lines[4][1], lines[5][1]]
roomB = [lines[2][5], lines[3][3], lines[4][3], lines[5][3]]
roomC = [lines[2][7], lines[3][5], lines[4][5], lines[5][5]]
roomD = [lines[2][9], lines[3][7], lines[4][7], lines[5][7]]

benchmark = 900000


def isPathClear(h, fr, to):
    if fr > to:
        fr, to = to, fr
    le = to - fr - 1
    return h[fr+1:to] == [None]*le


def isEverybodyHome(a, b, c, d):
    return (a == ['A', 'A', 'A', 'A'] and b == ['B', 'B', 'B', 'B'] and
            c == ['C', 'C', 'C', 'C'] and d == ['D', 'D', 'D', 'D'])


configurations = deque([[roomA, roomB, roomC, roomD, hallway, 0]])
t = time()
while configurations:
    if time()-t > timeToEndAndAssumeOptimum:
        print('Part 2:', benchmark)
        break
    a, b, c, d, h, cost = configurations.popleft()
    newH = h.copy()
    if a != ['A', 'A', 'A', 'A']:
        newA = a.copy()
        if a[0] is not None:
            newA[0] = None
            if h[1] is None:
                newCost = cost + 2 * energyCost[a[0]]
                if newCost < benchmark:
                    newH[1] = a[0]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[1] = None
                if h[0] is None:
                    newCost = cost + 3 * energyCost[a[0]]
                    if newCost < benchmark:
                        newH[0] = a[0]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[0] = None
            if h[3] is None:
                newCost = cost + 2 * energyCost[a[0]]
                if newCost < benchmark:
                    newH[3] = a[0]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[5] is None:
                    newCost = cost + 4 * energyCost[a[0]]
                    if newCost < benchmark:
                        newH[5] = a[0]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[7] is None:
                        newCost = cost + 6 * energyCost[a[0]]
                        if newCost < benchmark:
                            newH[7] = a[0]
                            configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[7] = None
                        if h[9] is None:
                            newCost = cost + 8 * energyCost[a[0]]
                            if newCost < benchmark:
                                newH[9] = a[0]
                                configurations.appendleft(
                                    [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[9] = None
                            if h[10] is None:
                                newCost = cost + 9 * energyCost[a[0]]
                                if newCost < benchmark:
                                    newH[10] = a[0]
                                    configurations.appendleft(
                                        [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                    newH[10] = None
        elif a[1] is not None and a[1:] != ['A', 'A', 'A']:
            newA[1] = None
            if h[1] is None:
                newCost = cost + 3 * energyCost[a[1]]
                if newCost < benchmark:
                    newH[1] = a[1]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[1] = None
                if h[0] is None:
                    newCost = cost + 4 * energyCost[a[1]]
                    if newCost < benchmark:
                        newH[0] = a[1]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[0] = None
            if h[3] is None:
                newCost = cost + 3 * energyCost[a[1]]
                if newCost < benchmark:
                    newH[3] = a[1]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[5] is None:
                    newCost = cost + 5 * energyCost[a[1]]
                    if newCost < benchmark:
                        newH[5] = a[1]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[7] is None:
                        newCost = cost + 7 * energyCost[a[1]]
                        if newCost < benchmark:
                            newH[7] = a[1]
                            configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[7] = None
                        if h[9] is None:
                            newCost = cost + 9 * energyCost[a[1]]
                            if newCost < benchmark:
                                newH[9] = a[1]
                                configurations.appendleft(
                                    [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[9] = None
                            if h[10] is None:
                                newCost = cost + 10 * energyCost[a[1]]
                                if newCost < benchmark:
                                    newH[10] = a[1]
                                    configurations.appendleft(
                                        [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                    newH[10] = None
        elif a[2] is not None and a[2:] != ['A', 'A']:
            newA[2] = None
            if h[1] is None:
                newCost = cost + 4 * energyCost[a[2]]
                if newCost < benchmark:
                    newH[1] = a[2]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[1] = None
                if h[0] is None:
                    newCost = cost + 5 * energyCost[a[2]]
                    if newCost < benchmark:
                        newH[0] = a[2]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[0] = None
            if h[3] is None:
                newCost = cost + 4 * energyCost[a[2]]
                if newCost < benchmark:
                    newH[3] = a[2]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[5] is None:
                    newCost = cost + 6 * energyCost[a[2]]
                    if newCost < benchmark:
                        newH[5] = a[2]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[7] is None:
                        newCost = cost + 8 * energyCost[a[2]]
                        if newCost < benchmark:
                            newH[7] = a[2]
                            configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[7] = None
                        if h[9] is None:
                            newCost = cost + 10 * energyCost[a[2]]
                            if newCost < benchmark:
                                newH[9] = a[2]
                                configurations.appendleft(
                                    [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[9] = None
                            if h[10] is None:
                                newCost = cost + 11 * energyCost[a[2]]
                                if newCost < benchmark:
                                    newH[10] = a[2]
                                    configurations.appendleft(
                                        [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                    newH[10] = None
        elif a[3] != 'A' and a[3] is not None:
            newA[3] = None
            if h[1] is None:
                newCost = cost + 5 * energyCost[a[3]]
                if newCost < benchmark:
                    newH[1] = a[3]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[1] = None
                if h[0] is None:
                    newCost = cost + 6 * energyCost[a[3]]
                    if newCost < benchmark:
                        newH[0] = a[3]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[0] = None
            if h[3] is None:
                newCost = cost + 5 * energyCost[a[3]]
                if newCost < benchmark:
                    newH[3] = a[3]
                    configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[5] is None:
                    newCost = cost + 7 * energyCost[a[3]]
                    if newCost < benchmark:
                        newH[5] = a[3]
                        configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[7] is None:
                        newCost = cost + 9 * energyCost[a[3]]
                        if newCost < benchmark:
                            newH[7] = a[3]
                            configurations.appendleft([newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[7] = None
                        if h[9] is None:
                            newCost = cost + 11 * energyCost[a[3]]
                            if newCost < benchmark:
                                newH[9] = a[3]
                                configurations.appendleft(
                                    [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[9] = None
                            if h[10] is None:
                                newCost = cost + 12 * energyCost[a[3]]
                                if newCost < benchmark:
                                    newH[10] = a[3]
                                    configurations.appendleft(
                                        [newA.copy(), b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                    newH[10] = None
    if b != ['B', 'B', 'B', 'B']:
        newB = b.copy()
        if b[0] is not None:
            newB[0] = None
            if h[3] is None:
                newCost = cost + 2 * energyCost[b[0]]
                if newCost < benchmark:
                    newH[3] = b[0]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[1] is None:
                    newCost = cost + 4 * energyCost[b[0]]
                    if newCost < benchmark:
                        newH[1] = b[0]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[1] = None
                    if h[0] is None:
                        newCost = cost + 5 * energyCost[b[0]]
                        if newCost < benchmark:
                            newH[0] = b[0]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[0] = None
            if h[5] is None:
                newCost = cost + 2 * energyCost[b[0]]
                if newCost < benchmark:
                    newH[5] = b[0]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[7] is None:
                    newCost = cost + 4 * energyCost[b[0]]
                    if newCost < benchmark:
                        newH[7] = b[0]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[7] = None
                    if h[9] is None:
                        newCost = cost + 6 * energyCost[b[0]]
                        if newCost < benchmark:
                            newH[9] = b[0]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[9] = None
                        if h[10] is None:
                            newCost = cost + 7 * energyCost[b[0]]
                            if newCost < benchmark:
                                newH[10] = b[0]
                                configurations.appendleft(
                                    [a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[10] = None
        elif b[1] is not None and b[1:] != ['B', 'B', 'B']:
            newB[1] = None
            if h[3] is None:
                newCost = cost + 3 * energyCost[b[1]]
                if newCost < benchmark:
                    newH[3] = b[1]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[1] is None:
                    newCost = cost + 5 * energyCost[b[1]]
                    if newCost < benchmark:
                        newH[1] = b[1]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[1] = None
                    if h[0] is None:
                        newCost = cost + 6 * energyCost[b[1]]
                        if newCost < benchmark:
                            newH[0] = b[1]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[0] = None
            if h[5] is None:
                newCost = cost + 3 * energyCost[b[1]]
                if newCost < benchmark:
                    newH[5] = b[1]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[7] is None:
                    newCost = cost + 5 * energyCost[b[1]]
                    if newCost < benchmark:
                        newH[7] = b[1]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[7] = None
                    if h[9] is None:
                        newCost = cost + 7 * energyCost[b[1]]
                        if newCost < benchmark:
                            newH[9] = b[1]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[9] = None
                        if h[10] is None:
                            newCost = cost + 8 * energyCost[b[1]]
                            if newCost < benchmark:
                                newH[10] = b[1]
                                configurations.appendleft(
                                    [a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[10] = None
        elif b[2] is not None and b[2:] != ['B', 'B']:
            newB[2] = None
            if h[3] is None:
                newCost = cost + 4 * energyCost[b[2]]
                if newCost < benchmark:
                    newH[3] = b[2]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[1] is None:
                    newCost = cost + 6 * energyCost[b[2]]
                    if newCost < benchmark:
                        newH[1] = b[2]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[1] = None
                    if h[0] is None:
                        newCost = cost + 7 * energyCost[b[2]]
                        if newCost < benchmark:
                            newH[0] = b[2]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[0] = None
            if h[5] is None:
                newCost = cost + 4 * energyCost[b[2]]
                if newCost < benchmark:
                    newH[5] = b[2]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[7] is None:
                    newCost = cost + 6 * energyCost[b[2]]
                    if newCost < benchmark:
                        newH[7] = b[2]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[7] = None
                    if h[9] is None:
                        newCost = cost + 8 * energyCost[b[2]]
                        if newCost < benchmark:
                            newH[9] = b[2]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[9] = None
                        if h[10] is None:
                            newCost = cost + 9 * energyCost[b[2]]
                            if newCost < benchmark:
                                newH[10] = b[2]
                                configurations.appendleft(
                                    [a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[10] = None
        elif b[3] != 'B' and b[3] is not None:
            newB[3] = None
            if h[3] is None:
                newCost = cost + 5 * energyCost[b[3]]
                if newCost < benchmark:
                    newH[3] = b[3]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[3] = None
                if h[1] is None:
                    newCost = cost + 7 * energyCost[b[3]]
                    if newCost < benchmark:
                        newH[1] = b[3]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[1] = None
                    if h[0] is None:
                        newCost = cost + 8 * energyCost[b[3]]
                        if newCost < benchmark:
                            newH[0] = b[3]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[0] = None
            if h[5] is None:
                newCost = cost + 5 * energyCost[b[3]]
                if newCost < benchmark:
                    newH[5] = b[3]
                    configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[7] is None:
                    newCost = cost + 7 * energyCost[b[3]]
                    if newCost < benchmark:
                        newH[7] = b[3]
                        configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[7] = None
                    if h[9] is None:
                        newCost = cost + 9 * energyCost[b[3]]
                        if newCost < benchmark:
                            newH[9] = b[3]
                            configurations.appendleft([a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                            newH[9] = None
                        if h[10] is None:
                            newCost = cost + 10 * energyCost[b[3]]
                            if newCost < benchmark:
                                newH[10] = b[3]
                                configurations.appendleft(
                                    [a.copy(), newB.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                                newH[10] = None
    if c != ['C', 'C', 'C', 'C']:
        newC = c.copy()
        if c[0] is not None:
            newC[0] = None
            if h[5] is None:
                newCost = cost + 2 * energyCost[c[0]]
                if newCost < benchmark:
                    newH[5] = c[0]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[3] is None:
                    newCost = cost + 4 * energyCost[c[0]]
                    if newCost < benchmark:
                        newH[3] = c[0]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[3] = None
                    if h[1] is None:
                        newCost = cost + 6 * energyCost[c[0]]
                        if newCost < benchmark:
                            newH[1] = c[0]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[1] = None
                        if h[0] is None:
                            newCost = cost + 7 * energyCost[c[0]]
                            if newCost < benchmark:
                                newH[0] = c[0]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                                newH[0] = None
            if h[7] is None:
                newCost = cost + 2 * energyCost[c[0]]
                if newCost < benchmark:
                    newH[7] = c[0]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[9] is None:
                    newCost = cost + 4 * energyCost[c[0]]
                    if newCost < benchmark:
                        newH[9] = c[0]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[9] = None
                    if h[10] is None:
                        newCost = cost + 5 * energyCost[c[0]]
                        if newCost < benchmark:
                            newH[10] = c[0]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[10] = None
        elif c[1] is not None and c[1:] != ['C', 'C', 'C']:
            newC[1] = None
            if h[5] is None:
                newCost = cost + 3 * energyCost[c[1]]
                if newCost < benchmark:
                    newH[5] = c[1]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[3] is None:
                    newCost = cost + 5 * energyCost[c[1]]
                    if newCost < benchmark:
                        newH[3] = c[1]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[3] = None
                    if h[1] is None:
                        newCost = cost + 7 * energyCost[c[1]]
                        if newCost < benchmark:
                            newH[1] = c[1]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[1] = None
                        if h[0] is None:
                            newCost = cost + 8 * energyCost[c[1]]
                            if newCost < benchmark:
                                newH[0] = c[1]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                                newH[0] = None
            if h[7] is None:
                newCost = cost + 3 * energyCost[c[1]]
                if newCost < benchmark:
                    newH[7] = c[1]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[9] is None:
                    newCost = cost + 5 * energyCost[c[1]]
                    if newCost < benchmark:
                        newH[9] = c[1]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[9] = None
                    if h[10] is None:
                        newCost = cost + 6 * energyCost[c[1]]
                        if newCost < benchmark:
                            newH[10] = c[1]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[10] = None
        elif c[2] is not None and c[2:] != ['C', 'C']:
            newC[2] = None
            if h[5] is None:
                newCost = cost + 4 * energyCost[c[2]]
                if newCost < benchmark:
                    newH[5] = c[2]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[3] is None:
                    newCost = cost + 6 * energyCost[c[2]]
                    if newCost < benchmark:
                        newH[3] = c[2]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[3] = None
                    if h[1] is None:
                        newCost = cost + 8 * energyCost[c[2]]
                        if newCost < benchmark:
                            newH[1] = c[2]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[1] = None
                        if h[0] is None:
                            newCost = cost + 9 * energyCost[c[2]]
                            if newCost < benchmark:
                                newH[0] = c[2]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                                newH[0] = None
            if h[7] is None:
                newCost = cost + 4 * energyCost[c[2]]
                if newCost < benchmark:
                    newH[7] = c[2]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[9] is None:
                    newCost = cost + 6 * energyCost[c[2]]
                    if newCost < benchmark:
                        newH[9] = c[2]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[9] = None
                    if h[10] is None:
                        newCost = cost + 7 * energyCost[c[2]]
                        if newCost < benchmark:
                            newH[10] = c[2]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[10] = None
        elif c[3] != 'C' and c[3] is not None:
            newC[3] = None
            if h[5] is None:
                newCost = cost + 5 * energyCost[c[3]]
                if newCost < benchmark:
                    newH[5] = c[3]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[5] = None
                if h[3] is None:
                    newCost = cost + 7 * energyCost[c[3]]
                    if newCost < benchmark:
                        newH[3] = c[3]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[3] = None
                    if h[1] is None:
                        newCost = cost + 9 * energyCost[c[3]]
                        if newCost < benchmark:
                            newH[1] = c[3]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[1] = None
                        if h[0] is None:
                            newCost = cost + 10 * energyCost[c[3]]
                            if newCost < benchmark:
                                newH[0] = c[3]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                                newH[0] = None
            if h[7] is None:
                newCost = cost + 5 * energyCost[c[3]]
                if newCost < benchmark:
                    newH[7] = c[3]
                    configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[9] is None:
                    newCost = cost + 7 * energyCost[c[3]]
                    if newCost < benchmark:
                        newH[9] = c[3]
                        configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                        newH[9] = None
                    if h[10] is None:
                        newCost = cost + 8 * energyCost[c[3]]
                        if newCost < benchmark:
                            newH[10] = c[3]
                            configurations.appendleft([a.copy(), b.copy(), newC.copy(), d.copy(), newH.copy(), newCost])
                            newH[10] = None
    if d != ['D', 'D', 'D', 'D']:
        newD = d.copy()
        if d[0] is not None:
            newD[0] = None
            if h[7] is None:
                newCost = cost + 2 * energyCost[d[0]]
                if newCost < benchmark:
                    newH[7] = d[0]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[5] is None:
                    newCost = cost + 4 * energyCost[d[0]]
                    if newCost < benchmark:
                        newH[5] = d[0]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[3] is None:
                        newCost = cost + 6 * energyCost[d[0]]
                        if newCost < benchmark:
                            newH[3] = d[0]
                            configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                            newH[3] = None
                        if h[1] is None:
                            newCost = cost + 8 * energyCost[d[0]]
                            if newCost < benchmark:
                                newH[1] = d[0]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                newH[1] = None
                            if h[0] is None:
                                newCost = cost + 9 * energyCost[d[0]]
                                if newCost < benchmark:
                                    newH[0] = d[0]
                                    configurations.appendleft(
                                        [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                    newH[0] = None
            if h[9] is None:
                newCost = cost + 2 * energyCost[d[0]]
                if newCost < benchmark:
                    newH[9] = d[0]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[9] = None
                if h[10] is None:
                    newCost = cost + 3 * energyCost[d[0]]
                    if newCost < benchmark:
                        newH[10] = d[0]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[10] = None
        elif d[1] is not None and d[1:] != ['D', 'D', 'D']:
            newD[1] = None
            if h[7] is None:
                newCost = cost + 3 * energyCost[d[1]]
                if newCost < benchmark:
                    newH[7] = d[1]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[5] is None:
                    newCost = cost + 5 * energyCost[d[1]]
                    if newCost < benchmark:
                        newH[5] = d[1]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[3] is None:
                        newCost = cost + 7 * energyCost[d[1]]
                        if newCost < benchmark:
                            newH[3] = d[1]
                            configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                            newH[3] = None
                        if h[1] is None:
                            newCost = cost + 9 * energyCost[d[1]]
                            if newCost < benchmark:
                                newH[1] = d[1]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                newH[1] = None
                            if h[0] is None:
                                newCost = cost + 10 * energyCost[d[1]]
                                if newCost < benchmark:
                                    newH[0] = d[1]
                                    configurations.appendleft(
                                        [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                    newH[0] = None
            if h[9] is None:
                newCost = cost + 3 * energyCost[d[1]]
                if newCost < benchmark:
                    newH[9] = d[1]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[9] = None
                if h[10] is None:
                    newCost = cost + 4 * energyCost[d[1]]
                    if newCost < benchmark:
                        newH[10] = d[1]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[10] = None
        elif d[2] is not None and d[2:] != ['D', 'D']:
            newD[2] = None
            if h[7] is None:
                newCost = cost + 4 * energyCost[d[2]]
                if newCost < benchmark:
                    newH[7] = d[2]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[5] is None:
                    newCost = cost + 6 * energyCost[d[2]]
                    if newCost < benchmark:
                        newH[5] = d[2]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[3] is None:
                        newCost = cost + 8 * energyCost[d[2]]
                        if newCost < benchmark:
                            newH[3] = d[2]
                            configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                            newH[3] = None
                        if h[1] is None:
                            newCost = cost + 10 * energyCost[d[2]]
                            if newCost < benchmark:
                                newH[1] = d[2]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                newH[1] = None
                            if h[0] is None:
                                newCost = cost + 11 * energyCost[d[2]]
                                if newCost < benchmark:
                                    newH[0] = d[2]
                                    configurations.appendleft(
                                        [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                    newH[0] = None
            if h[9] is None:
                newCost = cost + 4 * energyCost[d[2]]
                if newCost < benchmark:
                    newH[9] = d[2]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[9] = None
                if h[10] is None:
                    newCost = cost + 5 * energyCost[d[2]]
                    if newCost < benchmark:
                        newH[10] = d[2]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[10] = None
        elif d[3] != 'D' and d[3] is not None:
            newD[3] = None
            if h[7] is None:
                newCost = cost + 5 * energyCost[d[3]]
                if newCost < benchmark:
                    newH[7] = d[3]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[7] = None
                if h[5] is None:
                    newCost = cost + 7 * energyCost[d[3]]
                    if newCost < benchmark:
                        newH[5] = d[3]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[5] = None
                    if h[3] is None:
                        newCost = cost + 9 * energyCost[d[3]]
                        if newCost < benchmark:
                            newH[3] = d[3]
                            configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                            newH[3] = None
                        if h[1] is None:
                            newCost = cost + 11 * energyCost[d[3]]
                            if newCost < benchmark:
                                newH[1] = d[3]
                                configurations.appendleft(
                                    [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                newH[1] = None
                            if h[0] is None:
                                newCost = cost + 12 * energyCost[d[3]]
                                if newCost < benchmark:
                                    newH[0] = d[3]
                                    configurations.appendleft(
                                        [a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                                    newH[0] = None
            if h[9] is None:
                newCost = cost + 5 * energyCost[d[3]]
                if newCost < benchmark:
                    newH[9] = d[3]
                    configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                    newH[9] = None
                if h[10] is None:
                    newCost = cost + 6 * energyCost[d[3]]
                    if newCost < benchmark:
                        newH[10] = d[3]
                        configurations.appendleft([a.copy(), b.copy(), c.copy(), newD.copy(), newH.copy(), newCost])
                        newH[10] = None

    for i, co in (0, 3), (1, 2), (3, 2), (5, 4), (7, 6), (9, 8), (10, 9):
        if h[i] == 'A' and isPathClear(h, i, 2):
            if a[3] is None:
                newCost = cost + (co + 3) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [[None, None, None, 'A'], b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif a[2] is None and a[3] == 'A':
                newCost = cost + (co + 2) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [[None, None, 'A', 'A'], b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]

            elif a[1] is None and a[3] == 'A' and a[2] == 'A':
                newCost = cost + (co + 1) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [[None, 'A', 'A', 'A'], b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif a[0] is None and a[3] == 'A' and a[2] == 'A' and a[1] == 'A':
                newCost = cost + co * energyCost[h[i]]
                if newCost < benchmark:

                    if isEverybodyHome(['A', 'A', 'A', 'A'], b, c, d):
                        benchmark = newCost
                    else:
                        newH[i] = None
                        configurations.appendleft([['A', 'A', 'A', 'A'], b.copy(), c.copy(), d.copy(), newH.copy(), newCost])
                        newH[i] = h[i]
    for i, co in (0, 5), (1, 4), (3, 2), (5, 2), (7, 4), (9, 6), (10, 7):
        if h[i] == 'B' and isPathClear(h, i, 4):
            if b[3] is None:
                newCost = cost + (co + 3) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), [None, None, None, 'B'], c.copy(), d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif b[2] is None and b[3] == 'B':
                newCost = cost + (co + 2) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), [None, None, 'B', 'B'], c.copy(), d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif b[1] is None and b[3] == 'B' and b[2] == 'B':
                newCost = cost + (co + 1) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), [None, 'B', 'B', 'B'], c.copy(), d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif b[0] is None and b[3] == 'B' and b[2] == 'B' and b[1] == 'B':
                newCost = cost + co * energyCost[h[i]]
                if newCost < benchmark:
                    if isEverybodyHome(a, ['B', 'B', 'B', 'B'], c, d):
                        benchmark = newCost
                    else:
                        newH[i] = None
                        configurations.appendleft(
                            [a.copy(), ['B', 'B', 'B', 'B'], c.copy(), d.copy(), newH.copy(), newCost])
                        newH[i] = h[i]
    for i, co in (0, 7), (1, 6), (3, 4), (5, 2), (7, 2), (9, 4), (10, 5):
        if h[i] == 'C' and isPathClear(h, i, 6):
            if c[3] is None:
                newCost = cost + (co + 3) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), b.copy(), [None, None, None, 'C'], d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif c[2] is None and c[3] == 'C':
                newCost = cost + (co + 2) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), b.copy(), [None, None, 'C', 'C'], d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif c[1] is None and c[3] == 'C' and c[2] == 'C':
                newCost = cost + (co + 1) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), b.copy(), [None, 'C', 'C', 'C'], d.copy(), newH.copy(), newCost])
                    newH[i] = h[i]
            elif c[0] is None and c[3] == 'C' and c[2] == 'C' and c[1] == 'C':
                newCost = cost + co * energyCost[h[i]]
                if newCost < benchmark:
                    if isEverybodyHome(a, b, ['C', 'C', 'C', 'C'], d):
                        benchmark = newCost
                    else:
                        newH[i] = None
                        configurations.appendleft(
                            [a.copy(), b.copy(), ['C', 'C', 'C', 'C'], d.copy(), newH.copy(), newCost])
                        newH[i] = h[i]
    for i, co in (0, 9), (1, 8), (3, 6), (5, 4), (7, 2), (9, 2), (10, 3):
        if h[i] == 'D' and isPathClear(h, i, 8):
            if d[3] is None:
                newCost = cost + (co + 3) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), b.copy(), c.copy(), [None, None, None, 'D'], newH.copy(), newCost])
                    newH[i] = h[i]
            elif d[2] is None and d[3] == 'D':
                newCost = cost + (co + 2) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), b.copy(), c.copy(), [None, None, 'D', 'D'], newH.copy(), newCost])
                    newH[i] = h[i]
            elif d[1] is None and d[3] == 'D' and d[2] == 'D':
                newCost = cost + (co + 1) * energyCost[h[i]]
                if newCost < benchmark:
                    newH[i] = None
                    configurations.appendleft(
                        [a.copy(), b.copy(), c.copy(), [None, 'D', 'D', 'D'], newH.copy(), newCost])
                    newH[i] = h[i]
            elif d[0] is None and d[3] == 'D' and d[2] == 'D' and d[1] == 'D':
                newCost = cost + co * energyCost[h[i]]
                if newCost < benchmark:
                    if isEverybodyHome(a, b, c, ['D', 'D', 'D', 'D']):
                        benchmark = newCost
                    else:
                        newH[i] = None
                        configurations.appendleft(
                            [a.copy(), b.copy(), c.copy(), ['D', 'D', 'D', 'D'], newH.copy(), newCost])
                        newH[i] = h[i]
