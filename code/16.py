from math import prod


with open('16.txt', 'r') as file:
    mainPacket = file.read().strip()


class Packet:
    def __init__(self, data):
        self.versionNumber = int(data[:3], 2)
        self.typeID = int(data[3:6], 2)
        if self.typeID == 4:
            self.literalData = ''
            prefix = 1
            prefixPosition = 6
            while prefix:
                self.literalData += data[prefixPosition+1:prefixPosition+5]
                prefix = int(data[prefixPosition])
                prefixPosition += 5
            self.bitLength = len(self.literalData)//4
            self.totalLength = self.bitLength * 5 + 6
            self.subPackets = None
            self.literalNumber = int(self.literalData, 2)
        else:
            self.lengthTypeID = int(data[6])
            if self.lengthTypeID == 0:
                self.subPacketBitLength = int(data[7:22], 2)
                self.totalLength = self.subPacketBitLength + 22
                self.literalSubPackets = data[22:22+self.subPacketBitLength]
                self.subPackets = []
                subPacketBitLength = self.subPacketBitLength
                dataToParse = self.literalSubPackets
                while subPacketBitLength:
                    self.subPackets.append(Packet(dataToParse))
                    parsedLength = int(self.subPackets[-1].totalLength)
                    subPacketBitLength -= parsedLength
                    dataToParse = dataToParse[parsedLength:]
            else:
                self.numberOfSubPacketsContained = int(data[7:18], 2)
                self.literalSubPackets = data[18:]

                self.subPackets = []
                numberOfSubPacketsLeft = self.numberOfSubPacketsContained
                dataToParse = self.literalSubPackets
                totalParsedLength = 0
                while numberOfSubPacketsLeft:
                    self.subPackets.append(Packet(dataToParse))
                    parsedLength = self.subPackets[-1].totalLength
                    numberOfSubPacketsLeft -= 1
                    dataToParse = dataToParse[parsedLength:]
                    totalParsedLength += parsedLength
                self.totalLength = totalParsedLength + 18

    def version(self):
        return self.versionNumber

    def recursiveVersion(self):
        if self.subPackets is None:
            return [self.version()]
        result = [self.version()]
        for subPacket in self.subPackets:
            result.extend(subPacket.recursiveVersion())
        return result

    def evaluate(self):
        if self.typeID == 4:
            return self.literalNumber
        if self.typeID == 0:
            return sum([subPacket.evaluate() for subPacket in self.subPackets])
        if self.typeID == 1:
            return prod([subPacket.evaluate() for subPacket in self.subPackets])
        if self.typeID == 2:
            return min([subPacket.evaluate() for subPacket in self.subPackets])
        if self.typeID == 3:
            return max([subPacket.evaluate() for subPacket in self.subPackets])
        if self.typeID == 5:
            return self.subPackets[0].evaluate() > self.subPackets[1].evaluate()
        if self.typeID == 6:
            return self.subPackets[0].evaluate() < self.subPackets[1].evaluate()
        if self.typeID == 7:
            return self.subPackets[0].evaluate() == self.subPackets[1].evaluate()


pairs = [('0', '0000'), ('1', '0001'), ('2', '0010'), ('3', '0011'), ('4', '0100'), ('5', '0101'), ('6', '0110'),
         ('7', '0111'), ('8', '1000'), ('9', '1001'), ('A', '1010'), ('B', '1011'), ('C', '1100'), ('D', '1101'),
         ('E', '1110'), ('F', '1111')]

binaryMainPacket = mainPacket
for fr, to in pairs:
    binaryMainPacket = binaryMainPacket.replace(fr, to)

mainP = Packet(binaryMainPacket)
print('Part 1:', sum(mainP.recursiveVersion()))
print('Part 2:', mainP.evaluate())
