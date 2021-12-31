from math import ceil


with open('18.txt', 'r') as file:
    numbers = file.read().strip().split()


def extractPair(pair):
    first = ''
    second = ''
    stack = []
    one = True
    for ch in pair[1:-1]:
        if ch == '[':
            stack.append('[')
            if one:
                first += ch
            else:
                second += ch
        elif ch == ']':
            stack.pop()
            if one:
                first += ch
            else:
                second += ch
        elif ch == ',' and len(stack) == 0:
            one = False
        else:
            if one:
                first += ch
            else:
                second += ch
    return [first, second]


class Pair:
    def __init__(self, data, parent, side):
        self.parent = parent
        self.mySide = side
        self.number = None
        self.left = None
        self.right = None
        self.action = None
        if data.isnumeric():
            self.number = int(data)
            if self.number >= 10:
                self.action = 'split'
        else:
            left, right = extractPair(data)
            self.left = Pair(left, self, 'l')
            self.right = Pair(right, self, 'r')
            if self.parent is not None:
                if self.parent.parent is not None:
                    if self.parent.parent.parent is not None:
                        if self.parent.parent.parent.parent is not None:
                            self.action = 'expl'

    def explode(self):
        toSplit = []
        if self.mySide == 'r':
            giveLeft = self.parent.left
            while giveLeft.number is None:
                giveLeft = giveLeft.right
            giveLeft.number += self.left.number
            if giveLeft.number >= 10:
                toSplit.append(giveLeft)
                giveLeft.action = 'split'
            self.parent.right = Pair('0', self.parent, 'r')
            giveRight = self.parent
            while giveRight.parent is not None and giveRight.mySide == 'r':
                giveRight = giveRight.parent
            if giveRight.parent is not None:
                giveRight = giveRight.parent.right
                while giveRight.number is None:
                    giveRight = giveRight.left
                giveRight.number += self.right.number
                if giveRight.number >= 10:
                    toSplit.append(giveRight)
                    giveRight.action = 'split'
            toSplit.reverse()
        else:
            giveRight = self.parent.right
            while giveRight.number is None:
                giveRight = giveRight.left
            giveRight.number += self.right.number
            if giveRight.number >= 10:
                toSplit.append(giveRight)
                giveRight.action = 'split'
            self.parent.left = Pair('0', self.parent, 'l')
            giveLeft = self.parent
            while giveLeft.parent is not None and giveLeft.mySide == 'l':
                giveLeft = giveLeft.parent
            if giveLeft.parent is not None:
                giveLeft = giveLeft.parent.left
                while giveLeft.number is None:
                    giveLeft = giveLeft.right
                giveLeft.number += self.left.number
                if giveLeft.number >= 10:
                    toSplit.append(giveLeft)
                    giveLeft.action = 'split'

        if len(toSplit) != 0:
            return 'split', toSplit
        return None

    def split(self):
        left = self.number//2
        right = ceil(self.number/2)
        if self.mySide == 'r':
            self.parent.right = Pair('['+str(left)+','+str(right)+']', self.parent, 'r')
            toContinue = self.parent.right
        else:
            self.parent.left = Pair('['+str(left)+','+str(right)+']', self.parent, 'l')
            toContinue = self.parent.left
        if self.parent.parent is not None:
            if self.parent.parent.parent is not None:
                if self.parent.parent.parent.parent is not None:
                    return 'expl', toContinue
        return None

    def next(self):
        if self.right is not None:
            toReturn = self.right
            while toReturn.left is not None:
                toReturn = toReturn.left
            return toReturn
        if self.mySide == 'l':
            return self.parent
        toReturn = self.parent
        while toReturn.mySide == 'r':
            toReturn = toReturn.parent
        return toReturn.parent

    def magnitude(self):
        if self.number is not None:
            return self.number
        return self.left.magnitude()*3+self.right.magnitude()*2

    def reduce(self, first=True):
        listToDoExplode = []
        listToDoSplit = []
        do = self
        while do.left is not None:
            do = do.left
        while do is not None:
            if do.action is not None:
                if do.action == 'split':
                    if not listToDoExplode:
                        listToDoSplit.append(do)
                else:
                    listToDoExplode.append(do)
                    if not first:
                        break
            do = do.next()
        listToDoExplode.reverse()
        listToDoSplit.reverse()
        if not listToDoSplit and not listToDoExplode:
            return
        if listToDoExplode:
            while listToDoExplode:
                listToDoExplode.pop().explode()

        else:
            if listToDoSplit:
                listToDoSplit.pop().split()
        self.reduce(False)

    def printOutRecursive(self):
        if self.number is not None:
            return str(self.number)
        return '['+self.left.printOutRecursive()+','+self.right.printOutRecursive()+']'


pair = Pair(numbers[0], None, None)
for num in numbers[1:]:
    pair = Pair('['+pair.printOutRecursive()+','+num+']', None, None)
    pair.reduce()
print('Part 1:', pair.magnitude())

maxMagnitude = 0
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        pair = Pair('[' + numbers[i] + ',' + numbers[j] + ']', None, None)
        pair.reduce()
        newMag = pair.magnitude()
        if maxMagnitude < newMag:
            maxMagnitude = newMag
        pair = Pair('[' + numbers[j] + ',' + numbers[i] + ']', None, None)
        pair.reduce()
        newMag = pair.magnitude()
        if maxMagnitude < newMag:
            maxMagnitude = newMag

print('Part 2:', maxMagnitude)
