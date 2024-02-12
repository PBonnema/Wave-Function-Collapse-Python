from abc import ABC, abstractmethod
import graphics as g

from .BoundingBox import BoundingBox


class IUIElement(ABC):
    @property
    @abstractmethod
    def boundingBox(self) -> BoundingBox:
        ...

    @abstractmethod
    def draw(self) -> None:
        ...

    @abstractmethod
    def onMouseClick(self, mouseClickPosition: g.Point) -> bool:
        ...

    @abstractmethod
    def onKeyPress(self, pressedKey: str) -> bool:
        ...
