from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    BROWN = "Brown"
    GREEN = "Green"
    BLUE = "Blue"
    WHITE = "White"


@dataclass
class TileSetTile:
    text: str
    fill: Color
