from collections import deque
import random

from core.color import Color
from core.puyo import Puyo
from core.tsumo import Tsumo

class TsumoQueue:
    def __init__(self, size = 6):
        self.queue = deque()
        for i in range(size):
            self.enqueue()

    @property
    def current(self):
        return self.queue[0]

    def next(self, index = 1):
        return self.queue[index]
        
    def size(self):
        return len(self.queue)

    def dequeue(self):
        self.enqueue()
        return self.queue.popleft()

    def enqueue(self, tsumo = None):
        if tsumo is None:
            tsumo = Tsumo(self.createRandomPuyo(), self.createRandomPuyo())
        self.queue.append(tsumo)

    def createRandomPuyo(self):
        randomColorNumber = random.randint(0, len(Color) - 1)
        randomColor = tuple(Color)[randomColorNumber]
        return Puyo(randomColor)
