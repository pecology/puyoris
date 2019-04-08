from core.direction import Direction
from core.puyo import Puyo
from core.color import Color
from core.puyoGroup import PuyoGroup

class Field:
    def __init__(self, numberOfRow, numberOfColumn):
        self.numberOfRow = numberOfRow
        self.numberOfColumn = numberOfColumn

        self._cells = {}
        for rowI in range(numberOfRow):
            for colJ in range(numberOfColumn):
                self._cells[(rowI, colJ)] = Cell(self)
        
        self._coodinates = dict((cell, coodinate) for coodinate, cell in self._cells.items())

    def getCoodinate(self, cell):
        return self._coodinates.get(cell)
    
    def getCell(self, row, column):
        return self._cells.get((row, column))

    def existsBurstPuyo(self): 
        for cell in self._cells.values():
            connectedCells = cell.connectedPuyoCells()
            if len(connectedCells) >= 4:
                return True
        return False

    def burst(self):
        burstedPuyoGroups = []
        for cell in self._cells.values():
            connectedCells = cell.connectedPuyoCells()
            if len(connectedCells) >= 4:
                burstedPuyoGroups.append(PuyoGroup(cell.puyo.color, len(connectedCells)))
                for connectedCell in connectedCells:
                    connectedCell.puyo = None
        return burstedPuyoGroups

class Cell:
    def __init__(self, field):
        self._field = field
        self.puyo = None

    # for debug
    def __str__(self):
        return '(%s, %s, %s)' % (self.row, self.column, self.puyo)
    def __repr__(self):
        return self.__str__()
        
    @property
    def row(self):
        return self._field.getCoodinate(self)[0]
    
    @property
    def column(self):
        return self._field.getCoodinate(self)[1]

    @property
    def upperCell(self):
        return self.shiftStraight(Direction.VERTICAL, 1)

    @property
    def bottomCell(self):
        return self.shiftStraight(Direction.VERTICAL, -1)

    @property
    def rightCell(self):
        return self.shiftStraight(Direction.HORIZONTAL, 1)

    @property
    def leftCell(self):
        return self.shiftStraight(Direction.HORIZONTAL, -1)

    @property
    def adjacentCells(self):
        adjacentCells = (self.upperCell, self.bottomCell, self.leftCell, self.rightCell)
        noneExcepted = {cell for cell in adjacentCells if cell != None}
        return noneExcepted

    @property
    def adjacentSameColorCells(self):
        adjacentCells = self.adjacentCells
        return {adjacentCell for adjacentCell in adjacentCells if self.puyo != None and #
                                                                  self.puyo == adjacentCell.puyo}

    def connectedPuyoCells(self):
        connectedCells = set()

        def searchConnectedCells(cell):
            connectedCells.add(cell)
            targetCells = (cell.adjacentSameColorCells - connectedCells)
            for targetCell in targetCells:
                searchConnectedCells(targetCell)
        searchConnectedCells(self)

        return connectedCells

    def shift(self, rowShift, columnShift):
        originalCoord = self._field.getCoodinate(self)
        distRow = originalCoord[0] + rowShift
        distCol = originalCoord[1] + columnShift
        return self._field.getCell(distRow, distCol)

    def shiftStraight(self, direction, value):
        if direction == Direction.VERTICAL:
            return self.shift(value, 0)
        elif direction == Direction.HORIZONTAL:
            return self.shift(0, value)
        else:
            return self

    # def up(self):
    #     coodinate = self.field.getCoodinate(self)
    #     if coodinate[0] > self.field.numberOfRow - 1