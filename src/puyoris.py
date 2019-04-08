import os
import pyxel
from core.field import Field
from core.tsumoQueue import TsumoQueue
from core.hold import Hold
from core.score import Score

from state import Idle
from renderer import FieldRenderer, HoldRenderer, ScoreRenderer, TsumoQueueRenderer, TsumoRenderer


class Puyoris:
    def __init__(self):

        self.fieldRenderer = FieldRenderer()
        self.tsumoRenderer = TsumoRenderer()
        self.tsumoQueueRenderer = TsumoQueueRenderer() 
        self.holdRenderer = HoldRenderer()
        self.scoreRenderer = ScoreRenderer()
        self.field = Field(13, 6)
        self.tsumoQueue = TsumoQueue()
        self.hold = Hold()
        self.state = Idle()
        self.score = Score()
        pyxel.init(124, 148, caption="Puyoris")
        pyxel.load(os.getcwd() + "/resource/my_resource.pyxel")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.state = self.state.update(field = self.field, tsumoQueue = self.tsumoQueue, hold = self.hold, score = self.score)

    def draw(self):
        pyxel.cls(0)

        #フィールドの枠
        pyxel.blt(24, 24, 1, 0, 16, 64, 104)
        self.fieldRenderer.draw(self.field)
        self.tsumoRenderer.draw(self.tsumoQueue.current)

        #ホールドの枠
        pyxel.rectb(2, 8, 22, 28, 6)

        #ネクストの枠
        pyxel.rectb(96, 8, 116, 28, 6)
        pyxel.rectb(96, 28, 116, 48, 6)
        pyxel.rectb(96, 48, 116, 68, 6)
        pyxel.rectb(96, 68, 116, 88, 6)
        pyxel.rectb(96, 88, 116, 108, 6)

        #↑こいつら全部タイルにしたい

        self.tsumoQueueRenderer.draw(self.tsumoQueue)
        self.holdRenderer.draw(self.hold)
        self.scoreRenderer.draw(self.score)

Puyoris()
