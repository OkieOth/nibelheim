description = """Mine simulator
1. There is a mine ... considered as a field of elements 
"""

# size of the mine in x axis

def initMineWithGold(mineParam):
    print ('now it gives some gold ...')
    # hard coded will improved later
    # TODO: initialize the mine with random gold spots
    print ('done.')


# I am only a function ... to structure the program
def main():
    columnCount = 20
    mine = [0] * columnCount
    # this defines the fields of the mine
    mineSize = len(mine)
    print ("size of mine: " + str(mineSize))

    # give me some gold
    initMineWithGold(mine)

    # let's walk through the mine :D
    for i in range(columnCount):
        print ("Field {}: {}".format(i, mine[i]))

# this tests if the script is running as main module
if __name__ == '__main__':
    print ('main func from nibelheim.py (1)')
    main()
else:
    print ('I am loaded as import')