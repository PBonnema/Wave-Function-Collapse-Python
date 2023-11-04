import graphics as g

from NoTilePossibilitiesError import NoTilePossibilitiesError
from TileSet import TileSet
from TileSetTile import TileSetTile, TileSetColor
from World import World


def main() -> None:
    tileSet: TileSet = TileSet([
        TileSetTile(None, None, "./assets/roads2W-tiles/cross-roads.png"),
        TileSetTile(None, None, "./assets/roads2W-tiles/end-down.png"),
        TileSetTile(None, None, "./assets/roads2W-tiles/end-left.png"),
        TileSetTile(None, None, "./assets/roads2W-tiles/end-right.png"),
        TileSetTile(None, None, "./assets/roads2W-tiles/end-up.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/straight-horizontal.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/straight-vertical.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-down.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-left.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-right.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-up.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/turn-down-left.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/turn-down-right.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/turn-up-left.png"),
        # TileSetTile(None, None, "./assets/roads2W-tiles/turn-up-right.png"),
    ], [
        [
            (True, True, True, True, True, True, True, True),
            (True, True, False, True, False, True, False, True),
            (False, True, True, True, False, True, False, True),
            (False, True, False, True, False, True, True, True),
            (False, True, False, True, True, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
        ],
        [
            (False, True, False, True, True, True, False, True),
            (False, True, True, True, False, True, True, True),
            (True, True, False, True, False, True, True, True),
            (True, True, True, True, False, True, False, True),
            (True, True, True, True, True, True, True, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
        ],
        [
            (False, True, False, True, False, True, True, True),
            (False, True, True, True, True, True, False, True),
            (True, True, False, True, True, True, False, True),
            (True, True, True, True, True, True, True, True),
            (True, True, True, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
        ],
        [
            (False, True, True, True, False, True, False, True),
            (False, True, False, True, True, True, True, True),
            (True, True, True, True, True, True, True, True),
            (True, True, False, True, True, True, False, True),
            (True, True, False, True, False, True, True, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
        ],
        [
            (True, True, False, True, False, True, False, True),
            (True, True, True, True, True, True, True, True),
            (False, True, False, True, True, True, True, True),
            (False, True, True, True, True, True, False, True),
            (False, True, True, True, False, True, True, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
            # (False, True, False, True, False, True, False, True),
        ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
        # [
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        #     (False, True, False, True, False, True, False, True),
        # ],
    ])

    window = g.GraphWin("My WFC World", 1280, 960, autoflush=False)
    try:
        world = World(20, 15, 64, tileSet, window)
        world.draw()

        while True:
            window.getMouse()  # Pause to view result
            world.clear()
            try:
                while not world.doWaveFunctionCollapseStep():
                    pass
                    # window.getMouse()  # Pause to view result
                    # g.update()
            except NoTilePossibilitiesError:
                print("No tile possibilities remaining. Starting over...")
            g.update()
    finally:
        window.close()


if __name__ == '__main__':
    main()
