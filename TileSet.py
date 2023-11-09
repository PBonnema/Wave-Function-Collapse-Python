from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

from TileSetTile import TileSetTile


# Lees de matrix als:
# Een rij is voor één van de mogelijke tiles. Een kolom is voor het type tile van een neighbour en heeft 8 booleans, één voor iedere richting van die neighbour inclusief diagonalen.
# Een boolean geeft aan of dat tile mogelijk is als die neigbour an die zijde het type van die kolom is.
# De index van de rij en de index van een kolom in een rij zijn gelijk aan de index in de meegegeven tiles array
@dataclass
class TileSet:
    type TileSetRule = Tuple[bool, bool, bool, bool, bool, bool, bool, bool] # North, North East, East, South East, South, South West, West, North West

    tiles: List[TileSetTile]
    tileRestrictions: List[List[TileSet.TileSetRule]]
    tileSize: int
