from core.puyo import Puyo
from core.direction import FourDirection
from core.field import Field
from core.field import Cell

class Tsumo:
    def __init__(self, parentPuyo, childPuyo, xPosition = 2, childPuyoPosition = FourDirection.UP):
        self.parentPuyo = parentPuyo
        self.childPuyo = childPuyo
        self.xPosition = xPosition
        self.childPuyoDirection = childPuyoPosition

    def rotateRight(self):
        if self.childPuyoDirection == FourDirection.UP:
            self.childPuyoDirection = FourDirection.RIGHT
        elif self.childPuyoDirection == FourDirection.RIGHT:
            self.childPuyoDirection = FourDirection.DOWN
        elif self.childPuyoDirection == FourDirection.DOWN:
            self.childPuyoDirection = FourDirection.LEFT
        elif self.childPuyoDirection == FourDirection.LEFT:
            self.childPuyoDirection = FourDirection.UP

    def rotateLeft(self):
        if self.childPuyoDirection == FourDirection.UP:
            self.childPuyoDirection = FourDirection.LEFT
        elif self.childPuyoDirection == FourDirection.LEFT:
            self.childPuyoDirection = FourDirection.DOWN
        elif self.childPuyoDirection == FourDirection.DOWN:
            self.childPuyoDirection = FourDirection.RIGHT
        elif self.childPuyoDirection == FourDirection.RIGHT:
            self.childPuyoDirection = FourDirection.UP

    def drop(self, field):
        if self.childPuyoDirection == FourDirection.UP:
            self.dropPuyo(field, self.xPosition, self.parentPuyo)
            self.dropPuyo(field, self.xPosition, self.childPuyo)
        elif self.childPuyoDirection == FourDirection.DOWN:
            self.dropPuyo(field, self.xPosition, self.childPuyo)
            self.dropPuyo(field, self.xPosition, self.parentPuyo)
        elif self.childPuyoDirection == FourDirection.LEFT:
            self.dropPuyo(field, self.xPosition - 1, self.childPuyo)
            self.dropPuyo(field, self.xPosition    , self.parentPuyo)
        elif self.childPuyoDirection == FourDirection.RIGHT:
            self.dropPuyo(field, self.xPosition + 1, self.childPuyo)
            self.dropPuyo(field, self.xPosition    , self.parentPuyo)

    
    def dropPuyo(self, field, column, puyo):
        cell = field.getCell(field.numberOfRow - 1, column)
        while True :
            if cell.bottomCell is None or \
               cell.bottomCell.puyo is not None:
                cell.puyo = puyo
                return
            
            cell = cell.bottomCell