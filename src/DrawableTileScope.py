from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class DrawableTileScope:
    drawableTile: 'DrawableTile'
    fillColor: str
    edgeColor: str
    edgeThickness: float
    imagePath: Optional[str]
    drawRectangle: bool
    text: Optional[str]

    def __enter__(self) -> DrawableTileScope:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.drawableTile.restoreFromScope(self)
