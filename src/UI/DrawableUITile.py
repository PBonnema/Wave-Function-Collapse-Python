import graphics as g

from src.DrawableTile import DrawableTile
from src.UI.BoundingBox import BoundingBox
from src.UI.IUIElement import IUIElement
from src.wave_function_collapse.TileSetTile import TileSetTile


class DrawableUITile(IUIElement):
    def __init__(self, position: g.Point, size: g.Point, window: g.GraphWin, tile: TileSetTile) -> None:
        oppositePoint: g.Point = g.Point(position.getX() + size.getX(), position.getY() + size.getY())
        self.__boundingBox = BoundingBox(position, oppositePoint)
        self.__drawableTile = DrawableTile(
            position,
            size,
            window,
            drawRectangle=tile.fill is not None,
            text=tile.text,
            imagePath=tile.image)

        if tile.fill is not None:
            self.__drawableTile.setFill(tile.fill.value)

    @property
    def boundingBox(self) -> BoundingBox:
        return self.__boundingBox

    def draw(self) -> None:
        self.__drawableTile.draw()

    def onMouseClick(self, mouseClickPosition: g.Point) -> bool:
        pass

    def onKeyPress(self, pressedKey: str) -> bool:
        pass
