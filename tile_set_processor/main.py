import os
from PIL import Image


def main() -> None:
    tileSizeInImage = 64
    scaleToPixels = 64
    imagePath = "./assets/roads2W.png"
    imageFileName = imagePath[imagePath.rindex("/")+1:imagePath.rindex(".")]
    tilePath = f"./assets/{imageFileName}-generated"
    if not os.path.exists(tilePath):
        os.makedirs(tilePath)
    with Image.open(imagePath) as im:
        rows = im.height // tileSizeInImage
        columns = im.width // tileSizeInImage

        for row in range(rows):
            for column in range(columns):
                bb = (column * tileSizeInImage, row * tileSizeInImage, (column + 1) * tileSizeInImage, (row + 1) * tileSizeInImage)
                tile = im.resize((scaleToPixels, scaleToPixels), box = bb)
                tileFile = f"./{tilePath}/{imageFileName}-{column}-{row}.png"
                open(tileFile, "+ab").close()
                tile.save(tileFile)


if __name__ == '__main__':
    main()
