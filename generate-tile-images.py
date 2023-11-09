import os
from PIL import Image


def generateTileImages(imagePath: str, tileSizeInImage: int, scaleToPixels: int) -> None:
    imageFileName = imagePath[imagePath.rindex("/") + 1:imagePath.rindex(".")]
    tilePath = f"./assets/{imageFileName}-generated"
    if not os.path.exists(tilePath):
        os.makedirs(tilePath)
    with Image.open(imagePath) as im:
        rows = im.height // tileSizeInImage
        columns = im.width // tileSizeInImage

        for row in range(rows):
            for column in range(columns):
                bb = (column * tileSizeInImage, row * tileSizeInImage, (column + 1) * tileSizeInImage, (row + 1) * tileSizeInImage)
                tile = im.resize((scaleToPixels, scaleToPixels), box=bb)
                tileFile = f"./{tilePath}/{imageFileName}-{column}-{row}.png"
                open(tileFile, "+ab").close()
                tile.save(tileFile)


def main() -> None:
    # generateTileImages("./assets/roads2W.png", 64, 64)
    # generateTileImages("./assets/Dungeon Tile Set.png", 16, 16)
    # generateTileImages("./assets/terrain-map-v7.png", 32, 32)
    generateTileImages("./assets/map1.png", 16, 16)


if __name__ == '__main__':
    main()
