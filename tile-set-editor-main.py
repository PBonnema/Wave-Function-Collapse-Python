import json
from typing import Optional
import graphics as g

from src.TileSetEditor import TileSetEditor
from src.TileSetEditorScreen import TileSetEditorScreen
from src.UI.UIRoot import UIRoot
from src.wave_function_collapse.TileSet import TileSet
from src.wave_function_collapse.TileSetTile import TileSetTile


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
        window = g.GraphWin("My WFC World", 700, 700, autoflush=False)
        editorScreen = TileSetEditorScreen(tileSet, 50, window)
        editor = TileSetEditor(editorScreen)
        uiRoot = UIRoot(window)
        uiRoot.addChild(editorScreen)
        uiRoot.start()

        # world = World(10, 10, 64, window)
        # world.draw()

        # while True:
        #     window.getMouse()  # Pause to view result
        #     try:
        #         while not wfcWorld.doWaveFunctionCollapseStep():
        #             # pass
        #             window.update()
        #             # window.getMouse()  # Pause to view result
        #     except NoTilePossibilitiesError:
        #         print("No tile possibilities remaining. Starting over...")
        #     window.update()
    finally:
        if window is not None:
            window.close()


if __name__ == "__main__":
    main()
