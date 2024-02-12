from abc import ABC
from typing import List, override
import graphics as g

from .BoundingBox import BoundingBox
from .IUIElement import IUIElement


class Container(IUIElement, ABC):
    def __init__(self, window: g.GraphWin) -> None:
        self._window: g.GraphWin = window
        self._children: List[IUIElement] = []

    def addChild(self, child: IUIElement) -> None:
        self._children.append(child)

    @property
    def boundingBox(self) -> BoundingBox:
        return BoundingBox(g.Point(0, 0), g.Point(self._window.width, self._window.height))

    @override
    def draw(self) -> None:
        for child in self._children:
            child.draw()

    @override
    def onMouseClick(self, mouseClickPosition: g.Point) -> bool:
        print(f"Container Clicked on {mouseClickPosition}!")
        for child in self._children:
            if child.boundingBox.contains(mouseClickPosition):
                handled: bool = child.onMouseClick(mouseClickPosition)
                if handled:
                    return True
        return False

    @override
    def onKeyPress(self, pressedKey: str) -> bool:
        for child in self._children:
            handled: bool = child.onKeyPress(pressedKey)
            if handled:
                return True
        return False
