import json
from typing import Optional
import graphics as g

from NoTilePossibilitiesError import NoTilePossibilitiesError
from TileSet import TileSet
from TileSetTile import TileSetTile, TileSetColor
from World import World


def main() -> None:
    # tileSet: TileSet = TileSet([
    #     TileSetTile(None, None, "./assets/roads2W-tiles/cross-roads.png"),
    #     TileSetTile(None, None, "./assets/roads2W-tiles/end-down.png"),
    #     TileSetTile(None, None, "./assets/roads2W-tiles/end-left.png"),
    #     TileSetTile(None, None, "./assets/roads2W-tiles/end-right.png"),
    #     TileSetTile(None, None, "./assets/roads2W-tiles/end-up.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/straight-horizontal.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/straight-vertical.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-down.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-left.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-right.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/t-junction-up.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/turn-down-left.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/turn-down-right.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/turn-up-left.png"),
    #     # TileSetTile(None, None, "./assets/roads2W-tiles/turn-up-right.png"),
    # ], [
    #     [
    #         (True, True, True, True, True, True, True, True),
    #         (True, True, False, True, False, True, False, True),
    #         (False, True, True, True, False, True, False, True),
    #         (False, True, False, True, False, True, True, True),
    #         (False, True, False, True, True, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #     ],
    #     [
    #         (False, True, False, True, True, True, False, True),
    #         (False, True, True, True, False, True, True, True),
    #         (True, True, False, True, False, True, True, True),
    #         (True, True, True, True, False, True, False, True),
    #         (True, True, True, True, True, True, True, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #     ],
    #     [
    #         (False, True, False, True, False, True, True, True),
    #         (False, True, True, True, True, True, False, True),
    #         (True, True, False, True, True, True, False, True),
    #         (True, True, True, True, True, True, True, True),
    #         (True, True, True, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #     ],
    #     [
    #         (False, True, True, True, False, True, False, True),
    #         (False, True, False, True, True, True, True, True),
    #         (True, True, True, True, True, True, True, True),
    #         (True, True, False, True, True, True, False, True),
    #         (True, True, False, True, False, True, True, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #     ],
    #     [
    #         (True, True, False, True, False, True, False, True),
    #         (True, True, True, True, True, True, True, True),
    #         (False, True, False, True, True, True, True, True),
    #         (False, True, True, True, True, True, False, True),
    #         (False, True, True, True, False, True, True, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #         # (False, True, False, True, False, True, False, True),
    #     ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    #     # [
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     #     (False, True, False, True, False, True, False, True),
    #     # ],
    # ])

    rulesFile = "./assets/roads2W-tiles/rules.json"
    with (open(rulesFile, "r") as f):
        def decoder(d: dict):
            if 'tiles' in d and 'tileRestrictions' in d:
                # TODO convert the lists to tuples
                return TileSet(d['tiles'], d['tileRestrictions'])
            elif 'text' in d and 'fill' in d and 'image' in d:
                return TileSetTile(d['text'], d['fill'], d['image'])
            return d
        tileSet: TileSet = json.load(f, object_hook=decoder)

    window: Optional[g.GraphWin] = None
    try:
        window = g.GraphWin("My WFC World", 1280, 960, autoflush=False)
        world = World(20, 15, 64, tileSet, window)
        world.draw()

        while True:
            window.getMouse()  # Pause to view result
            world.clear()
            try:
                while not world.doWaveFunctionCollapseStep():
                    # pass
                    window.update()
                    # window.getMouse()  # Pause to view result
            except NoTilePossibilitiesError:
                print("No tile possibilities remaining. Starting over...")
            window.update()
    finally:
        if window is not None:
            window.close()


if __name__ == '__main__':
    main()
