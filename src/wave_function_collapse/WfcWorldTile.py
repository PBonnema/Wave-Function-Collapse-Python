from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from ..DrawableTile import DrawableTile
from .TileSetTile import TileSetTile


@dataclass
class WfcWorldTile:
    type Entropy = int

    drawableTile: DrawableTile
    tileSetPossibilities: List[bool]
    neighbours: List[Optional[WfcWorldTile]] # North, North East, East, South East, South, South West, West, North West
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

    def updateViewForCollapsed(self, tile: TileSetTile) -> None:
        self.drawableTile.setImage(tile.image)
        if tile.fill is not None:
            self.drawableTile.setFill(tile.fill.value)
        else:
            self.drawableTile.setDrawRectangle(False)
        self.drawableTile.text = tile.text

    def updateViewForEntropy(self) -> None:
        self.drawableTile.text = str(self.entropy)

    def clearView(self) -> None:
        self.drawableTile.setDrawRectangle(True)
        self.drawableTile.setImage(None)
        self.updateViewForEntropy()

    def updateViewForEntropyOfNeighbourUpdate(self) -> None:
        if not self.isCollapsed:
            self.drawableTile.setFill("orange")
        else:
            self.drawableTile.setDrawRectangle(True)
            self.drawableTile.setEdgeColor("orange")
            self.drawableTile.setEdgeThickness(5)

    def updateViewForEntropyUpdate(self) -> None:
        if not self.isCollapsed:
            self.drawableTile.setFill("blue")
        else:
            self.drawableTile.setDrawRectangle(True)
            self.drawableTile.setEdgeColor("blue")
            self.drawableTile.setEdgeThickness(5)
