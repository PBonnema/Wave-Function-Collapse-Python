import random
from typing import List

from .NoTilePossibilitiesError import NoTilePossibilitiesError
from .TileSet import TileSet
from .WfcWorldTile import WfcWorldTile
from ..World import World


class WfcWorld:
    def __init__(self, tileSet: TileSet, world: World) -> None:
        self.__tileSet: TileSet = tileSet
        self.__maxTileEntropy: WfcWorldTile.entropy = len(self.__tileSet.tiles)
        self.__world: World = world
        self.__wcfTiles: List[List[WfcWorldTile]] = self.__initWorld(world)

    def __initWorld(self, world: World) -> List[List[WfcWorldTile]]:
        worldTiles: List[List[WfcWorldTile]] = []
        width = len(world.tiles[0])

        # Wrap each DrawableTile in the World with a WcfTile so it can control its appearance.
        for y, rowDrawableTiles in enumerate(world.tiles):
            rowWorldTiles: List[WfcWorldTile] = []
            for x, drawableTile in enumerate(rowDrawableTiles):
                # Create a WcfTile and link it to its neighbours
                # Fetch some neighbours that already exist
                northNeighbour = worldTiles[-1][x] if y > 0 else None
                northEastNeighbour = worldTiles[-1][x + 1] if y > 0 and x < width - 1 else None
                westNeighbour = rowWorldTiles[-1] if x > 0 else None
                northWestNeighbour = worldTiles[-1][x - 1] if x > 0 and y > 0 else None

                # North, North East, East, South East, South, South West, West, North West
                neighbours = [northNeighbour, northEastNeighbour, None, None, None, None, westNeighbour, northWestNeighbour]

                worldTile = WfcWorldTile(drawableTile, [True] * len(self.__tileSet.tiles), neighbours)

                # Set the new tile as the neighbour of our neighbours
                if northNeighbour is not None:
                    northNeighbour.neighbours[4] = worldTile

                if northEastNeighbour is not None:
                    northEastNeighbour.neighbours[5] = worldTile

                if westNeighbour is not None:
                    westNeighbour.neighbours[2] = worldTile

                if northWestNeighbour is not None:
                    northWestNeighbour.neighbours[3] = worldTile

                rowWorldTiles.append(worldTile)
            worldTiles.append(rowWorldTiles)
        return worldTiles

    def clear(self):
        for row in self.__wcfTiles:
            for tile in row:
                tile.tileSetIndex = None
                tile.tileSetPossibilities = [True] * len(self.__tileSet.tiles)
                tile.clearView()

    def doWaveFunctionCollapseStep(self) -> bool:
        # Get list of lowest entropy tiles. Doesn't return already collapsed tiles.
        lowestEntropyTiles: List[WfcWorldTile] = self.__getLowestEntropyTiles()

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

    def __getLowestEntropyTiles(self) -> List[WfcWorldTile]:
        lowestEntropy: WfcWorldTile.Entropy = self.__maxTileEntropy
        lowestEntropyTiles: List[WfcWorldTile] = []

        for row in self.__wcfTiles:
            for tile in row:
                if not tile.isCollapsed:
                    entropy: WfcWorldTile.Entropy = tile.entropy
                    if entropy < lowestEntropy:
                        lowestEntropy = entropy
                        lowestEntropyTiles = [tile]
                    elif entropy == lowestEntropy:
                        lowestEntropyTiles.append(tile)

        return lowestEntropyTiles

    def __collapseTile(self, tile: WfcWorldTile) -> None:
        tilePossibilityIndices = list(filter(lambda p: p[1], enumerate(tile.tileSetPossibilities)))

        # Set all remaining possibilities to False
        tile.tileSetPossibilities = [False] * len(self.__tileSet.tiles)

        # Except for a randomly chosen possibility
        try:
            tile.tileSetIndex = random.choice(tilePossibilityIndices)[0]
        except IndexError as e:
            raise NoTilePossibilitiesError from e
        tile.tileSetPossibilities[tile.tileSetIndex] = True

        tile.updateViewForCollapsed(self.__tileSet.tiles[tile.tileSetIndex])

    def __updateNeighbourEntropy(self, updatedTile: WfcWorldTile) -> None:
        with updatedTile.drawableTile.startScopedDrawing():
            updatedTile.updateViewForEntropyOfNeighbourUpdate()
            window = updatedTile.drawableTile.window
            window.update()
            # window.getMouse()

            for neighbourIndex, neighbour in enumerate(updatedTile.neighbours):
                if neighbour is not None and not neighbour.isCollapsed:
                    # We cannot optimize this by skipping this step if the neighbour already has 1 entropy
                    # (but isn't collapsed yet) because, in rare cases, even the last possibility might be invalidated
                    with neighbour.drawableTile.startScopedDrawing():
                        neighbour.updateViewForEntropyUpdate()
                        window.update()
                        # window.getMouse()

                        updatedTileIndex = WfcWorldTile.calculateOppositeNeighbourIndex(neighbourIndex)
                        possibilitiesChanged = False
                        for tileSetIndex, stillPossible in enumerate(neighbour.tileSetPossibilities):
                            if stillPossible:
                                possible = False
                                # TODO optimize by not doing all tileSetPossibilities but first filter on which are still possible. Hmm, is probably not an optimization at all
                                # TODO possibly optimize by also passing along which tileset possiblity of the updated Tile was updated and only check that one
                                for updatedTileSetIndex, updatedStillPossible in enumerate(updatedTile.tileSetPossibilities):
                                    if updatedStillPossible and self.__tileSet.tileRestrictions[tileSetIndex][updatedTileSetIndex][updatedTileIndex]:
                                        possible = True
                                        break
                                neighbour.tileSetPossibilities[tileSetIndex] = possible
                                possibilitiesChanged = possibilitiesChanged or not possible

                        if possibilitiesChanged:
                            neighbour.updateViewForEntropy()
                            window.update()
                            # window.getMouse()
                            with neighbour.drawableTile.startUnscopedDrawing():
                                neighbour.updateViewForEntropy()

                            window.update()
                            # window.getMouse()
                            # Recursively update entropy of the neighbours of the neighbour
                            self.__updateNeighbourEntropy(neighbour)

                    window.update()

        window.update()
        # window.getMouse()
