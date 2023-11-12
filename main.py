import json
from typing import Optional
import graphics as g

from src.wave_function_collapse.NoTilePossibilitiesError import NoTilePossibilitiesError
from src.wave_function_collapse.TileSet import TileSet
from src.wave_function_collapse.TileSetTile import TileSetTile, TileSetColor
from src.wave_function_collapse.WfcWorld import WfcWorld
from src.World import World


def main() -> None:
    rulesFile = "./assets/roads2W-tiles/rules.json"

    with (open(rulesFile, "r") as f):
        def decoder(d: dict):
            # Detect the type by doing duck typing
            if 'tiles' in d and 'tileRestrictions' in d and 'tileSize' in d:
                # TODO convert the lists to tuples
                return TileSet(d['tiles'], d['tileRestrictions'], d['tileSize'])
            elif 'text' in d and 'fill' in d and 'image' in d:
                return TileSetTile(d['text'], d['fill'], d['image'])
            return d
        tileSet: TileSet = json.load(f, object_hook=decoder)

    window: Optional[g.GraphWin] = None
    try:
        # Width and height should be a multiple of at least 128 and be less than the full screen on 1080p
        window = g.GraphWin("My WFC World", 128 * 14, 128 * 7, autoflush=False)
        world = World(window.width // tileSet.tileSize, window.height // tileSet.tileSize, tileSet.tileSize, window)
        wfcWorld = WfcWorld(tileSet, world)
        world.draw()

        while True:
            window.getMouse()  # Pause to view result
            wfcWorld.clear()
            try:
                while not wfcWorld.doWaveFunctionCollapseStep():
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
