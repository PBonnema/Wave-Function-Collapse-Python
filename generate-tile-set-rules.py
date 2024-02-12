import json
import os
from typing import List, Dict, Tuple, cast

from PIL import Image

from src.wave_function_collapse.TileSet import TileSet
from src.wave_function_collapse.TileSetTile import TileSetTile


def calculateSimilarity(image: Image.Image, image2: Image.Image, ruleIndex: int) -> int:
    line: List[Tuple[int, int, int, int]] = []
    line2: List[Tuple[int, int, int, int]] = []
    # Only support the non-diagonals
    if ruleIndex == 0:
        line = list(image.getdata())[:image.width]
        line2 = list(image2.getdata())[-image.width:]
    elif ruleIndex == 2:
        line = list(image.getdata())[image.width-1::image.width]
        line2 = list(image2.getdata())[::image.width]
    elif ruleIndex == 4:
        line = list(image.getdata())[-image.width:]
        line2 = list(image2.getdata())[:image.width]
    elif ruleIndex == 6:
        line = list(image.getdata())[::image.width]
        line2 = list(image2.getdata())[image.width-1::image.width]
    return sum(map(lambda a, b: a != b, line, line2))


class TileSetTileEncoder(json.JSONEncoder):
    def default(self, obj: TileSetTile):
        if isinstance(obj, TileSetTile):
            return obj.__dict__
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


def generateTileSetRules(tileImageDirectory: str, maxDifferingPixels: int, tileSize: int) -> None:
    images: Dict[str, Image.Image] = {}
    for filename in os.listdir(tileImageDirectory):
        if filename != "rules.json":
            imagePath = os.path.join(tileImageDirectory, filename)
            images[imagePath] = Image.open(imagePath, 'r').copy()
            images[imagePath].load() # Close the image file but keep the image in memory

    tileSet: TileSet = TileSet([], [], tileSize)

    for filename, image in images.items():
        tileSet.tiles.append(TileSetTile(None, None, filename))
        rules: List[Tuple[bool, bool, bool, bool, bool, bool, bool, bool]] = []
        for filename2, image2 in images.items():
            # The diagonals will be True by default
            rule: List[bool, bool, bool, bool, bool, bool, bool, bool] = [True] * 8
            # Now skip the diagonals
            for ruleIndex in range(0, len(rule), 2):
                differingPixels: int = calculateSimilarity(image, image2, ruleIndex)
                rule[ruleIndex] = differingPixels <= maxDifferingPixels
            rules.append(cast(Tuple[bool, bool, bool, bool, bool, bool, bool, bool], tuple(rule)))
        tileSet.tileRestrictions.append(rules)

    with open(os.path.join(tileImageDirectory, "rules.json"), "w+") as f:
        json.dump(tileSet.__dict__, f, cls=TileSetTileEncoder, indent=None)


def main() -> None:
    generateTileSetRules("./assets/roads2W-tiles", 10, 64)
    # generateTileSetRules("./assets/Dungeon Tile Set-tiles", 4, 16)
    # generateTileSetRules("./assets/terrain-map-v7-generated", 6, 32)
    # generateTileSetRules("./assets/map1-generated", 4, 16)


if __name__ == '__main__':
    main()
