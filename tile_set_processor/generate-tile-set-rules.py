import json
import os
from typing import List, Dict, Tuple, cast

from PIL import Image

from TileSet import TileSet
from TileSetTile import TileSetTile


def calculateSimilarity(image: Image.Image, image2: Image.Image, ruleIndex: int) -> int:
    return image.width


class TileSetTileEncoder(json.JSONEncoder):
    def default(self, obj: TileSetTile):
        if isinstance(obj, TileSetTile):
            return obj.__dict__
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


def generateTileSetRules(tileImageDirectory: str) -> None:
    images: Dict[str, Image.Image] = {}
    for filename in os.listdir(tileImageDirectory):
        if filename != "rules.json":
            imagePath = os.path.join(tileImageDirectory, filename)
            images[imagePath] = Image.open(imagePath, 'r')

    tileSet: TileSet = TileSet([], [])

    for filename, image in images.items():
        tileSet.tiles.append(TileSetTile(None, None, filename))
        rules: List[Tuple[bool, bool, bool, bool, bool, bool, bool, bool]] = []
        for filename2, image2 in images.items():
            rule: List[bool, bool, bool, bool, bool, bool, bool, bool] = [False] * 8
            for ruleIndex in range(len(rule)):
                differingPixels: int = calculateSimilarity(image, image2, ruleIndex)
                rule[ruleIndex] = differingPixels == 0
            rules.append(cast(Tuple[bool, bool, bool, bool, bool, bool, bool, bool], tuple(rule)))
        tileSet.tileRestrictions.append(rules)

    with open(os.path.join(tileImageDirectory, "rules.json"), "w+") as f:
        json.dump(tileSet.__dict__, f, cls=TileSetTileEncoder)


def main() -> None:
    generateTileSetRules("./assets/roads2W-tiles")


if __name__ == '__main__':
    main()
