class Score:
    def __init__(self):
        self.score = 0

    def add(self, added):
        self.score += added

    @staticmethod
    def calcScore(numOfChain, puyoGroups):
        #1連鎖4個消しは、例外として常に40点
        if len(puyoGroups) == 1 and \
            puyoGroups[0].size == 4 and \
            numOfChain == 1:
            return 40

        colors = set(puyoGroup.color for puyoGroup in puyoGroups)
        colorBornus = Score.colorBornus[len(colors)]

        groupBornus = sum(Score.groupBornus[group.size] for group in puyoGroups)

        chainBornus = Score.chainBornus[numOfChain]

        clearedPuyoAmount = sum([group.size for group in puyoGroups])

        score = clearedPuyoAmount * (chainBornus + groupBornus + colorBornus) * 10
        return score
        
    colorBornus = {
        1: 0,
        2: 3,
        3: 6,
        4: 12,
        5: 24
    }

    groupBornus = {
        4 : 0,
        5 : 2,
        6 : 3,
        7 : 4,
        8 : 5,
        9 : 6,
        10: 7,
        11: 10
    }

    chainBornus = {
        1 : 0,
        2 : 8,
        3 : 16,
        4 : 32,
        5 : 64,
        6 : 96,
        7 : 128,
        8 : 160,
        9 : 192,
        10: 224,
        11: 256,
        12: 288,
        13: 320,
        14: 352,
        15: 384,
        16: 416,
        17: 448,
        18: 480,
        19: 512
    }


        
