# Module Tables.py

import math

class Table:
    def __init__(self, position):
        self.position = position
        self.capacity = 0

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, capacity):
        self.capacity = capacity

    def clear(self):
        self.capacity = 0



# Table arrangement

def areInReach(pos1, pos2, minDist):
    return (pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2 < minDist**2

def positionTaken(tables, position, minDist):
    for table in tables:
        if areInReach(table.position, position, minDist):
            return True

    return False

def inBound(boundary, x, y):
    x0, y0, width, height = boundary
    return (x0 <= x <= width) and (y0 <= y <= height)

def getTableArrangement(boundary, minDist, tableRadius):
    tables = []
    length = minDist + tableRadius

    def addTable(x, y):
        if not inBound(boundary, x, y):
            return
        elif positionTaken(tables, (x,y), minDist):
            return
        else:
            tables.append(Table((x,y)))

            for i in range(6):
                newX = 2*length*math.cos(math.pi*i/3)
                newY = 2*length*math.sin(math.pi*i/3)
                addTable(x + newX, y + newY)

    addTable(0,0)

    return tables

if __name__ == "__main__":
    tables = getTableArrangement((0,0,7.5,5), 1.5, 1)

    for table in tables:
        print(f"{table.position[0]}\t{table.position[1]}\t{table.capacity}")
