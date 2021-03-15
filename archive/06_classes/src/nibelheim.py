description = """Mine simulator
1. There is a mine ... considered as a matrix 
2. Fields in the mine are randomly filled with gold
3. A dwarf runs around and if he finds gold he filled his pocket with it
"""

class NuggetSpot:
    """Abstraction of a place where nuggets are
    """

    def __init__(self, x, y, nuggetSize):
        pass


class Mine:
    """ The abstraction of a mine. contains basically a list
    of contained gold nuggets
    """

    def __init__(self, rowCount, columnCount):
        # how many segments has the mine in y-axis
        self.rowCount = rowCount
        # how many segments has the mine in x-axis
        self.columnCount = columnCount
        # list current nugget spots
        self.nuggetSpots = []


class Dwarf:
    def __init__(self):
        # number of found nuggets
        self.goldCount = 0
        # row in the mine where the dwarf is currently in
        self.currentRow = 0
        # column in the mine where the dwarf is currently in
        self.currentCol = 0        


def main():
    # TODO
    pass

if __name__ == '__main__':
    main()