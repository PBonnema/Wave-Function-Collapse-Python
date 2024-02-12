from typing import override

import graphics as g

from .UI.Button import Button
from .UI.Container import Container
from .UI.DrawableUITile import DrawableUITile
from .wave_function_collapse.TileSet import TileSet


class TileSetEditorScreen(Container):
    def __init__(self, tileSet: TileSet, tileSpacingPixels: int, window: g.GraphWin) -> None:
        super().__init__(window)
        self.__init_view(tileSet, tileSpacingPixels, window)
        # self.addChild(Button(g.Point(100, 200), g.Point(100, 200), window, text="Text"))

    @override
    def onMouseClick(self, mouseClickPosition: g.Point) -> bool:
        print(f"TileSetEditorScreen Clicked on {mouseClickPosition}!")
        return super().onMouseClick(mouseClickPosition)

    def __init_view(self, tileSet: TileSet, tileSpacingPixels: int, window: g.GraphWin) -> None:
        spacing = tileSpacingPixels + tileSet.tileSize
        for index, tile in enumerate(tileSet.tiles):
            position = g.Point(index * spacing + tileSpacingPixels, tileSpacingPixels)
            # TODO add line wrapping
            size = g.Point(tileSet.tileSize, tileSet.tileSize)
            self.addChild(DrawableUITile(position, size, window, tile))
