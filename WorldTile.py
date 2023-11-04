from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from DrawableTile import DrawableTile
from DrawableTileScope import DrawableTileScope
from TileSetTile import TileSetTile


@dataclass
class WorldTile:
    type Entropy = int

    __drawableTile: DrawableTile
    tileSetPossibilities: List[bool]
    neighbours: List[Optional[WorldTile]] # North, North East, East, South East, South, South West, West, North West
    tileSetIndex: Optional[int] = None

    def draw(self) -> None:
        self.__drawableTile.draw()

    @property
    def entropy(self) -> Entropy:
        return sum(self.tileSetPossibilities)

    @property
    def isCollapsed(self) -> bool:
        return self.tileSetIndex is not None

    @staticmethod
    def calculateOppositeNeighbourIndex(neighbourIndex) -> int:
        return (neighbourIndex + 4) % 8

    def updateViewForCollapsed(self, tileSetTile: TileSetTile) -> None:
        self.__drawableTile.setImage(tileSetTile.image)
        if tileSetTile.fill is not None:
            self.__drawableTile.setFill(tileSetTile.fill.value)
        else:
            self.__drawableTile.setDrawRectangle(False)
        self.__drawableTile.text = tileSetTile.text

    def updateViewForEntropy(self) -> None:
        self.__drawableTile.text = str(self.entropy)

    def clearView(self) -> None:
        self.__drawableTile.setDrawRectangle(True)
        self.__drawableTile.setImage(None)
        self.updateViewForEntropy()

    def updateViewForEntropyOfNeighbourUpdate(self) -> None:
        if not self.isCollapsed:
            self.__drawableTile.setFill("orange")
        else:
            self.__drawableTile.setDrawRectangle(True)
            self.__drawableTile.setEdgeColor("orange")
            self.__drawableTile.setEdgeThickness(5)

    def updateViewForEntropyUpdate(self) -> None:
        if not self.isCollapsed:
            self.__drawableTile.setFill("blue")
        else:
            self.__drawableTile.setDrawRectangle(True)
            self.__drawableTile.setEdgeColor("blue")
            self.__drawableTile.setEdgeThickness(5)
            
    def startScopedDrawing(self) -> DrawableTileScope:
        return self.__drawableTile.startScopedDrawing()

    def startUnscopedDrawing(self) -> DrawableTileScope:
        return self.__drawableTile.startUnscopedDrawing()