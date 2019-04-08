from unittest import TestCase
from src.core.field import Field
from src.core.puyo import Puyo
from src.core.color import Color

class TestField(TestCase):
    
    def testGetCell(self):
        field = Field(3, 4)

        #normal
        cell = field.getCell(1, 3)
        self.assertEquals(field.getCoodinate(cell), (1, 3))

        #boundary
        cell = field.getCell(2, 0)
        self.assertEquals(field.getCoodinate(cell), (2, 0))
        cell = field.getCell(0, 3)
        self.assertEquals(field.getCoodinate(cell), (0, 3))
        cell = field.getCell(2, 3)
        self.assertEquals(field.getCoodinate(cell), (2, 3))

        self.assertEquals(field.getCell(3, 0), None)
        self.assertEquals(field.getCell(-1, 0), None)
        self.assertEquals(field.getCell(0, 4), None)
        self.assertEquals(field.getCell(0, -1), None)
        self.assertEquals(field.getCell(-1, 4), None)
        self.assertEquals(field.getCell(3, -1), None)

    def testCellRowColumn(self):
        field = Field(10, 20)

        #normal
        cell = field.getCell(4, 5)
        self.assertEquals(cell.row, 4)
        self.assertEquals(cell.column, 5)

        #boundary
        cell = field.getCell(0, 0)
        self.assertEquals(cell.row, 0)
        self.assertEquals(cell.column, 0)

        cell = field.getCell(9, 19)
        self.assertEquals(cell.row, 9)
        self.assertEquals(cell.column, 19)

    def testShift(self):
        field = Field(10, 20)
        cell = field.getCell(3,4)

        self.assertEquals(cell.shift(0, 0), field.getCell(3, 4))
        self.assertEquals(cell.shift(2, 3), field.getCell(5, 7))
        self.assertEquals(cell.shift(-1, -2), field.getCell(2, 2))
        self.assertEquals(cell.shift(6, 15), field.getCell(9, 19))
        self.assertEquals(cell.shift(7, 15), None)
        self.assertEquals(cell.shift(6, 16), None)
        self.assertEquals(cell.shift(-3, -4), field.getCell(0, 0))
        self.assertEquals(cell.shift(-4, -4), None)
        self.assertEquals(cell.shift(-3, -5), None)

    def testUpDownRightLeft(self):
        field = Field(10, 20)
        cell = field.getCell(3,4)

        self.assertEqual(cell.upperCell , field.getCell(4,4))
        self.assertEqual(cell.bottomCell , field.getCell(2,4))
        self.assertEqual(cell.rightCell  , field.getCell(3,5))
        self.assertEqual(cell.leftCell  , field.getCell(3,3))

        upperRightCell = field.getCell(9, 19)
        self.assertEqual(upperRightCell.upperCell , None)
        self.assertEqual(upperRightCell.rightCell  , None)

        bottomLeftCell = field.getCell(0, 0)
        self.assertEqual(bottomLeftCell.bottomCell , None)
        self.assertEqual(bottomLeftCell.leftCell  , None)

    def testAdjacentCells(self):
        field = Field(3,5)

        notBorderCell = field.getCell(1,2)
        adjacentCells = notBorderCell.adjacentCells
        self.assertIn(field.getCell(0, 2), adjacentCells)
        self.assertIn(field.getCell(2, 2), adjacentCells)
        self.assertIn(field.getCell(1, 1), adjacentCells)
        self.assertIn(field.getCell(1, 3), adjacentCells)
        self.assertEqual(4, len(adjacentCells))

        bottomLeftCornerCell = field.getCell(0, 0)
        adjacentCells = bottomLeftCornerCell.adjacentCells
        self.assertIn(field.getCell(0, 1), adjacentCells)
        self.assertIn(field.getCell(1, 0), adjacentCells)
        self.assertEqual(2, len(adjacentCells))

        upperRightCornerCell = field.getCell(2, 4)
        adjacentCells = upperRightCornerCell.adjacentCells
        self.assertIn(field.getCell(1, 4), adjacentCells)
        self.assertIn(field.getCell(2, 3), adjacentCells)
        self.assertEqual(2, len(adjacentCells))

    def testAdjacentSameColorCell(self):
        field = Field(6,13)

        field.getCell(2, 5).puyo = Puyo(Color.RED)
        field.getCell(1, 5).puyo = Puyo(Color.RED)
        field.getCell(3, 5).puyo = Puyo(Color.RED)
        field.getCell(2, 4).puyo = Puyo(Color.RED)
        field.getCell(2, 6).puyo = Puyo(Color.RED)

        cell = field.getCell(2, 5)
        adjacentCells = cell.adjacentCells
        for adjacentCell in adjacentCells:
            adjacentCell.puyo = Puyo(Color.RED)
        
        cell.puyo = None
        self.assertEqual(0, len(cell.adjacentSameColorCells))

        cell.puyo = Puyo(Color.RED)
        self.assertEqual(cell.adjacentCells, cell.adjacentSameColorCells)

        cell.puyo = Puyo(Color.BLUE)
        self.assertEqual(0, len(cell.adjacentSameColorCells))

    def testConnectedPuyoCells(self):
        field = Field(5,7)

        #adjacent
        targetCell = field.getCell(2,3)
        targetCell.puyo = Puyo(Color.BLUE)
        targetCell.upperCell.puyo = Puyo(Color.BLUE)
        targetCell.bottomCell.puyo = Puyo(Color.BLUE)
        targetCell.leftCell.puyo = None
        targetCell.rightCell.puyo = Puyo(Color.PURPLE)
        self.assertEqual(set([targetCell, 
                              targetCell.upperCell, 
                              targetCell.bottomCell]), 
                              targetCell.connectedPuyoCells())

        #notattached
        upperCell = targetCell.upperCell
        upperCell.puyo = Puyo(Color.BLUE)
        upperCell.upperCell.puyo = Puyo(Color.BLUE)
        upperCell.leftCell.puyo = Puyo(Color.BLUE)
        upperCell.rightCell.puyo = Puyo(Color.BLUE)
        upperCell.rightCell.bottomCell.puyo = Puyo(Color.BLUE)
        self.assertEqual(set([targetCell, 
                              targetCell.upperCell, 
                              targetCell.bottomCell,
                              upperCell.upperCell,
                              upperCell.leftCell,
                              upperCell.rightCell,
                              upperCell.rightCell.bottomCell]), 
                              targetCell.connectedPuyoCells())

        #none
        targetCell.puyo = None
        self.assertEqual(set([targetCell]), targetCell.connectedPuyoCells())


