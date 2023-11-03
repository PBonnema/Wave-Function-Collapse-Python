from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from DrawableTile import DrawableTile
from TileSetTile import TileSetTile, TileSetColor


@dataclass
class WorldTile:
    type Entropy = int

    drawableTile: DrawableTile
    tileSetPossibilities: List[bool]
    neighbours: List[Optional[WorldTile]] # North, North East, East, South East, South, South West, West, North West
    tileSetIndex: Optional[int] = None

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
        self.drawableTile.setImage(tileSetTile.image)
        if tileSetTile.fill is not None:
            self.drawableTile.setFill(tileSetTile.fill.value)
        else:
            self.drawableTile.setDrawRectangle(False)
        self.drawableTile.text = tileSetTile.text

    def updateViewForEntropy(self) -> None:
        self.drawableTile.text = str(self.entropy)

    def clearView(self) -> None:
        self.drawableTile.setDrawRectangle(True)
        self.drawableTile.setImage(None)
        self.updateViewForEntropy()