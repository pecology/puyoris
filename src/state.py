import pyxel
from core.direction import FourDirection
from core.gravity import Gravity
from core.score import Score
from core.puyoGroup import PuyoGroup
from core.color import Color

class WhileChaining:
    def __init__(self):
        self.chainingCount = 0

    def update(self, **params):
        field = params["field"]
        if field.existsBurstPuyo():
            return Delay(5, WhileChaining.WhileBursting(self))
        else:
            return Idle()

    class WhileBursting:
        def __init__(self, whileChaining):
            self.whileChaining = whileChaining

        def update(self, **params):
            field = params["field"]
            score = params["score"]

            burstedPuyoGroups = field.burst()
            self.whileChaining.chainingCount += 1
            score.add(Score.calcScore(self.whileChaining.chainingCount, burstedPuyoGroups))

            return Delay(10, WhileChaining.WhileDropping(self.whileChaining))

    class WhileDropping:
        def __init__(self, whileChaining):
            self.whileChaining = whileChaining

        def update(self, **params):
            field = params["field"]
            Gravity.drop(field)
            return self.whileChaining

class Delay:
    def __init__(self, delayFrame, afterState):
        self.afterState = afterState
        self.delayFrame = delayFrame
        self.startFrameCount = 0
    def update(self, **params):
        self.startFrameCount += 1
        if self.startFrameCount < self.delayFrame:
            return self
        else:
            return self.afterState



class Idle:
    def update(self, **params):
        tsumoQueue = params["tsumoQueue"]
        field = params["field"]
        hold = params["hold"]
        tsumo = tsumoQueue.current
        if pyxel.btnp(pyxel.KEY_LEFT):
            if (tsumo.childPuyoDirection == FourDirection.LEFT and tsumo.xPosition > 1) or \
               (tsumo.childPuyoDirection != FourDirection.LEFT and tsumo.xPosition > 0):
                tsumo.xPosition -= 1
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            if (tsumo.childPuyoDirection == FourDirection.RIGHT and tsumo.xPosition < field.numberOfColumn - 2) or \
               (tsumo.childPuyoDirection != FourDirection.RIGHT and tsumo.xPosition < field.numberOfColumn - 1):
                tsumo.xPosition += 1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            tsumo.drop(field)
            tsumoQueue.dequeue()
            # 状態遷移
            return WhileChaining()
        elif pyxel.btnp(pyxel.KEY_A):
            if tsumo.childPuyoDirection == FourDirection.UP and tsumo.xPosition == 0:
                tsumo.xPosition += 1
            elif tsumo.childPuyoDirection == FourDirection.DOWN and tsumo.xPosition == field.numberOfColumn - 1:
                tsumo.xPosition -= 1
            tsumo.rotateLeft()
        elif pyxel.btnp(pyxel.KEY_Z):
            if tsumo.childPuyoDirection == FourDirection.UP and tsumo.xPosition == field.numberOfColumn - 1:
                tsumo.xPosition -= 1
            elif tsumo.childPuyoDirection == FourDirection.DOWN and tsumo.xPosition == 0:
                tsumo.xPosition += 1
            tsumo.rotateRight()
        elif pyxel.btnp(pyxel.KEY_H):
            holdTsumo = hold.toggle(tsumoQueue.queue[0])
            if holdTsumo is None:
                tsumoQueue.dequeue()
            else:
                tsumoQueue.queue[0] = holdTsumo
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        return self
