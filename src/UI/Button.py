from typing import Optional, override, Callable
import graphics as g

from .BoundingBox import BoundingBox
from .IUIElement import IUIElement


class Button(IUIElement):
    def __init__(self,
                 position: g.Point,
                 size: g.Point,
                 window: g.GraphWin,
                 clickCallback: Callable[[g.Point], bool],
                 keyCallback: Callable[[str], bool],
                 text: Optional[str] = None,
                 imagePath: Optional[str] = None) -> None:
        self.__position: g.Point = position
        self.__midPoint: g.Point = g.Point(position.getX() + size.getX() / 2.0, position.getY() + size.getY() / 2.0)
        self.__oppositePoint: g.Point = g.Point(position.getX() + size.getX(), position.getY() + size.getY())
        self.__boundingBox: BoundingBox = BoundingBox(position, self.__oppositePoint)

        # Create the assets in reverse Z-order (from bottom to top)
        self.__image: Optional[g.Image] = g.Image(self.__midPoint, imagePath) if imagePath is not None else None
        self.__rectangle: Optional[g.Rectangle] = g.Rectangle(position, self.__oppositePoint)
        self.__text: Optional[g.Text] = g.Text(self.__midPoint, text) if text is not None else None

        self.__clickCallback = clickCallback
        self.__keyCallback = keyCallback

        self.__window: g.GraphWin = window

    @property
    @override
    def boundingBox(self) -> BoundingBox:
        return self.__boundingBox

    @override
    def draw(self) -> None:
        if self.__rectangle is not None:
            self.__rectangle.draw(self.__window)
        if self.__text is not None:
            self.__text.draw(self.__window)
        if self.__image is not None:
            self.__image.draw(self.__window)

    @override
    def onMouseClick(self, mouseClickPosition: g.Point) -> bool:
        print(f"Button Clicked on {mouseClickPosition}!")
        self.__clickCallback(mouseClickPosition)
        return True

    @override
    def onKeyPress(self, pressedKey: str) -> bool:
        print(f"Pressed {pressedKey}!")
        self.__keyCallback(pressedKey)
        return False
