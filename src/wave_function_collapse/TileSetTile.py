from dataclasses import dataclass
from enum import Enum
from typing import Optional


class TileSetColor(Enum):
    BROWN = "Brown"
    GREEN = "Green"
    BLUE = "Blue"
    WHITE = "White"


@dataclass
class TileSetTile:
    text: Optional[str]
    fill: Optional[TileSetColor]
    image: Optional[str]
