from typing import List, Optional
import graphics as g

from .IUIElement import IUIElement


class UIRoot:
    def __init__(self, window: g.GraphWin) -> None:
        self.__window: g.GraphWin = window
        self.__children: List[IUIElement] = []

    def addChild(self, child: IUIElement) -> None:
        self.__children.append(child)

    def start(self) -> None:
        self.__updateView()
        while self.__window.isOpen():
            self.__handleMouseClick(self.__window.checkMouse())
            self.__handleKeyPress(self.__window.checkKey())

    def __updateView(self) -> None:
        for child in self.__children:
            child.draw()

    def __handleMouseClick(self, mouseClickPosition: Optional[g.Point]) -> None:
        if mouseClickPosition is not None:
            for child in self.__children:
                if child.boundingBox.contains(mouseClickPosition):
                    handled: bool = child.onMouseClick(mouseClickPosition)
                    if handled:
                        break

    def __handleKeyPress(self, pressedKey: Optional[str]) -> None:
        if pressedKey != "":
            for child in self.__children:
                handled: bool = child.onKeyPress(pressedKey)
                if handled:
                    break
