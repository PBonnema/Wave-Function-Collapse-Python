import random
from typing import List
import graphics as g

from DrawableTile import DrawableTile
from TileSet import TileSet
from WorldTile import WorldTile


class World:
    def __init__(self, width: int, height: int, tileSize: int, tileSet: TileSet, window: g.GraphWin) -> None:
        self.__tileSet: TileSet = tileSet
        self.__maxTileEntropy: WorldTile.entropy = len(self.__tileSet.tiles)
        self.__tiles: List[List[WorldTile]] = self.__initWorld(width, height, tileSize, window)

    def __initWorld(self, width: int, height: int, tileSize: int, window: g.GraphWin) -> List[List[WorldTile]]:
        worldTiles: List[List[WorldTile]] = []
        for y in range(height):
            row: List[WorldTile] = []
            for x in range(width):
                position: g.Point = g.Point(x * tileSize, y * tileSize)
                drawableTile = DrawableTile(position, g.Point(tileSize, tileSize), window, str(self.__maxTileEntropy))

                # Fetch some neighbours that already exist
                northNeighbour = worldTiles[-1][len(row)] if y > 0 else None
                northEastNeighbour = worldTiles[-1][len(row) + 1] if y > 0 and x < width - 1 else None
                westNeighbour = row[-1] if x > 0 else None
                northWestNeighbour = worldTiles[-1][len(row) - 1] if x > 0 and y > 0 else None

                # North, North East, East, South East, South, South West, West, North West
                neighbours = [northNeighbour, northEastNeighbour, None, None, None, None, westNeighbour, northWestNeighbour]

                worldTile = WorldTile(drawableTile, [True] * len(self.__tileSet.tiles), neighbours)

                # Set the new tile as the neighbour of our neighbours
                if northNeighbour is not None:
                    northNeighbour.neighbours[4] = worldTile

                if northEastNeighbour is not None:
                    northEastNeighbour.neighbours[5] = worldTile

                if westNeighbour is not None:
                    westNeighbour.neighbours[2] = worldTile

                if northWestNeighbour is not None:
                    northWestNeighbour.neighbours[3] = worldTile

                row.append(worldTile)
            worldTiles.append(row)
        return worldTiles

    def clear(self):
        for row in self.__tiles:
            for tile in row:
                tile.tileSetIndex = None
                tile.tileSetPossibilities = [True] * len(self.__tileSet.tiles)
                tile.clearView()

    def draw(self) -> None:
        for row in self.__tiles:
            for tile in row:
                tile.drawableTile.draw()

    def doWaveFunctionCollapseStep(self) -> bool:
        # Get list of lowest entropy tiles. Doesn't return already collapsed tiles.
        lowestEntropyTiles: List[WorldTile] = self.__getLowestEntropyTiles()

        # Done if no tiles are returned (because all are collapsed)
        if len(lowestEntropyTiles) == 0:
            return True

        # Pick random tile to collapse
        tileToCollapse = random.choice(lowestEntropyTiles)

        # Collapse the tile
        self.__collapseTile(tileToCollapse)

        # Update entropy of neighbours
        self.__updateNeighbourEntropy(tileToCollapse)

        return False

    def __getLowestEntropyTiles(self) -> List[WorldTile]:
        lowestEntropy: WorldTile.Entropy = self.__maxTileEntropy
        lowestEntropyTiles: List[WorldTile] = []

        for row in self.__tiles:
            for tile in row:
                if not tile.isCollapsed:
                    entropy: WorldTile.Entropy = tile.entropy
                    if entropy < lowestEntropy:
                        lowestEntropy = entropy
                        lowestEntropyTiles = [tile]
                    elif entropy == lowestEntropy:
                        lowestEntropyTiles.append(tile)

        return lowestEntropyTiles

    def __collapseTile(self, tile: WorldTile) -> None:
        tilePossibilityIndices = list(filter(lambda p: p[1], enumerate(tile.tileSetPossibilities)))

        # Set all remaining possibilities to False
        tile.tileSetPossibilities = [False] * len(self.__tileSet.tiles)

        # Except for a randomly chosen possibility
        tile.tileSetIndex = random.choice(tilePossibilityIndices)[0]
        tile.tileSetPossibilities[tile.tileSetIndex] = True

        tile.updateViewForCollapsed(self.__tileSet.tiles[tile.tileSetIndex])

    def __updateNeighbourEntropy(self, updatedTile: WorldTile) -> None:
        for neighbourIndex, neighbour in enumerate(updatedTile.neighbours):
            if neighbour is not None and not neighbour.isCollapsed:
                possibilitiesChanged = False
                for tileSetIndex, stillPossible in enumerate(neighbour.tileSetPossibilities):
                    if stillPossible:
                        updatedTileIndex = WorldTile.calculateOppositeNeighbourIndex(neighbourIndex)
                        possible = False
                        for updatedTileSetIndex, updatedStillPossible in enumerate(updatedTile.tileSetPossibilities):
                            if updatedStillPossible and self.__tileSet.tileRestrictions[tileSetIndex][updatedTileSetIndex][updatedTileIndex]:
                                possible = True
                                break
                        neighbour.tileSetPossibilities[tileSetIndex] = possible
                        possibilitiesChanged = possibilitiesChanged or not possible

                if possibilitiesChanged:
                    neighbour.updateViewForEntropy()

                    # Recursively update entropy of the neighbours of the neighbour
                    self.__updateNeighbourEntropy(neighbour)
