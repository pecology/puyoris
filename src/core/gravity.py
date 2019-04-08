from core.field import Field

class Gravity:
    def __init__(self):
        pass

    @staticmethod
    def drop(field):
        for column in range(field.numberOfColumn):
            for row in range(field.numberOfRow):
                cell = field.getCell(row, column)
                if cell.puyo is None:
                    puyoCell = cell.upperCell
                    while puyoCell is not None and  \
                          puyoCell.puyo is None:
                        puyoCell = puyoCell.upperCell
                    if puyoCell is None:
                        break
                    cell.puyo = puyoCell.puyo
                    puyoCell.puyo = None