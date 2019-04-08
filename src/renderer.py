import pyxel

from core.color import Color
from core.direction import FourDirection


class TsumoRenderer:
    def __init__(self):
        self.relativePositionX = 32
        self.relativePositionY = 16

    def draw(self, tsumo):
        parentPuyoImg = PuyoImg(tsumo.parentPuyo)
        parentX = tsumo.xPosition * 8 + self.relativePositionX
        pyxel.blt(parentX, self.relativePositionY, parentPuyoImg.imgBankNo, parentPuyoImg.x, parentPuyoImg.y, parentPuyoImg.width, parentPuyoImg.height)

        childPuyoImg = PuyoImg(tsumo.childPuyo)
        childX = tsumo.xPosition * 8 + self.relativePositionX
        childY = self.relativePositionY
        if tsumo.childPuyoDirection == FourDirection.UP:
            childY -= 8
        elif tsumo.childPuyoDirection == FourDirection.DOWN:
            childY += 8
        elif tsumo.childPuyoDirection == FourDirection.LEFT:
            childX -= 8
        elif tsumo.childPuyoDirection == FourDirection.RIGHT:
            childX += 8

        pyxel.blt(childX, childY, childPuyoImg.imgBankNo, childPuyoImg.x, childPuyoImg.y, childPuyoImg.width, childPuyoImg.height)

class HoldRenderer:
    def __init__(self):
        self.relativePositionX = 2
        self.relativePositionY = 8

    def draw(self, hold):
            holdTsumo = hold.holdTsumo
            if holdTsumo is None:
                return

            childPuyoImg = PuyoImg(holdTsumo.childPuyo)
            childX = self.relativePositionX + 7
            childY = self.relativePositionY + 2
            pyxel.blt(childX, childY, childPuyoImg.imgBankNo, childPuyoImg.x, childPuyoImg.y, childPuyoImg.width, childPuyoImg.height)
            
            parentPuyoImg = PuyoImg(holdTsumo.parentPuyo)
            parentX = self.relativePositionX + 7
            parentY = self.relativePositionY + 10
            pyxel.blt(parentX, parentY, parentPuyoImg.imgBankNo, parentPuyoImg.x, parentPuyoImg.y, parentPuyoImg.width, parentPuyoImg.height)

class TsumoQueueRenderer:
    def __init__(self):
        self.relativePositionX = 96
        self.relativePositionY = 8
    def draw(self, tsumoQueue):
        for i in range(1, tsumoQueue.size()):
            tsumo = tsumoQueue.next(i)

            childPuyoImg = PuyoImg(tsumo.childPuyo)
            childX = self.relativePositionX + 7
            childY = self.relativePositionY + 2 + (i - 1) * 20
            pyxel.blt(childX, childY, childPuyoImg.imgBankNo, childPuyoImg.x, childPuyoImg.y, childPuyoImg.width, childPuyoImg.height)
            
            parentPuyoImg = PuyoImg(tsumo.parentPuyo)
            parentX = self.relativePositionX + 7
            parentY = self.relativePositionY + 10 + (i - 1) * 20
            pyxel.blt(parentX, parentY, parentPuyoImg.imgBankNo, parentPuyoImg.x, parentPuyoImg.y, parentPuyoImg.width, parentPuyoImg.height)

class ScoreRenderer:
    def __init__(self):
        self.relativePositionX = 52
        self.relativePositionY = 132

    def draw(self, score):
        pyxel.text(self.relativePositionX, self.relativePositionY, "%07d" % score.score, 6)

class FieldRenderer:
    def __init__(self):
        self.relativePositionX = 32
        self.relativePositionY = 8

    def draw(self, field):
        for x in range(field.numberOfRow):
            for y in range(field.numberOfColumn):
                self.drawCell(field.getCell(x,y))

    def drawCell(self, cell):
        pos = self.getCellPosition(cell)

        puyoImg = PuyoImg(cell.puyo)

        pyxel.blt(pos["x"], pos["y"], puyoImg.imgBankNo, puyoImg.x, puyoImg.y, puyoImg.width, puyoImg.height)

    def getCellPosition(self, cell):
        x = cell.column * 8 + self.relativePositionX
        y = (13 - cell.row) * 8  + self.relativePositionY
        return {"x": x, "y": y}

class PuyoImg:
    def __init__(self, puyo):
        if puyo is None:
            self.x = 20
            self.y = 0
        elif puyo.color == Color.RED:
            self.x = 0
            self.y = 0
        elif puyo.color == Color.YELLOW:
            self.x = 0
            self.y = 8
        elif puyo.color == Color.BLUE:
            self.x = 8
            self.y = 0
        elif puyo.color == Color.GREEN:
            self.x = 8
            self.y = 8

        self.width = 8
        self.height = 8
        self.imgBankNo = 1  
