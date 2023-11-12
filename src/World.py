from typing import List
import graphics as g

from .DrawableTile import DrawableTile


class World:
    def __init__(self, width: int, height: int, tileSize: int, window: g.GraphWin) -> None:
        self.__tiles: List[List[DrawableTile]] = World.__initWorld(width, height, tileSize, window)

    @staticmethod
    def __initWorld(width: int, height: int, tileSize: int, window: g.GraphWin) -> List[List[DrawableTile]]:
        tiles: List[List[DrawableTile]] = []
        for y in range(height):
            row: List[DrawableTile] = []
            for x in range(width):
                position = g.Point(x * tileSize, y * tileSize)
                drawableTile = DrawableTile(position, g.Point(tileSize, tileSize), window, True)
                row.append(drawableTile)
            tiles.append(row)
        return tiles

    @property
    def tiles(self) -> List[List[DrawableTile]]:
        return self.__tiles

    def draw(self) -> None:
        for row in self.__tiles:
            for tile in row:
                tile.draw()
