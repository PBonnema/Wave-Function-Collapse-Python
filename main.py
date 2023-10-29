import graphics as g

from TileSet import TileSet
from TileSetTile import TileSetTile, Color
from World import World


def main() -> None:
    tileSet: TileSet = TileSet([
        TileSetTile("Zee", Color.BLUE),
        TileSetTile("Land", Color.BROWN),
        TileSetTile("Bos", Color.GREEN),
    ], [
        [(True, True, True, True, True, True, True, True), (True, True, True, True, True, True, True, True),
         (False, True, False, True, False, True, False, True)],
        [(True, True, True, True, True, True, True, True), (True, True, True, True, True, True, True, True),
         (True, True, True, True, True, True, True, True)],
        [(False, True, False, True, False, True, False, True), (True, True, True, True, True, True, True, True),
         (True, True, True, True, True, True, True, True)]
    ])

    window = g.GraphWin("My WFC World", 800, 800)
    try:
        world = World(20, 20, 40, tileSet, window)
        world.draw()

        while True:
            window.getMouse()  # Pause to view result
            world.clear()
            while not world.doWaveFunctionCollapseStep():
                pass
                #window.getMouse()  # Pause to view result
    finally:
        window.close()


if __name__ == '__main__':
    main()
