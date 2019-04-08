class Hold:
    def __init__(self):
        self.holdTsumo = None

    def toggle(self, tsumo):
        buffer = self.holdTsumo
        self.holdTsumo = tsumo
        return buffer