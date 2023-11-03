from typing import Optional
import graphics as g


class DrawableTile:
    def __init__(self, position: g.Point, size: g.Point, window: g.GraphWin, drawRectangle: bool = True, text: Optional[str] = None, rectangleFill: Optional[str] = None, imagePath: Optional[str] = None) -> None:
        self.__position: g.Point = position
        self.__size: g.Point = size
        self.__midPoint: g.Point = g.Point(position.getX() + size.getX() / 2.0, position.getY() + size.getY() / 2.0)
        self.__oppositePoint: g.Point = g.Point(self.__position.getX() + self.__size.getX(), self.__position.getY() + self.__size.getY())

        # Create the assets in reverse Z-order (from bottom to top)
        self.__image: Optional[g.Image] = g.Image(self.__midPoint, imagePath) if imagePath is not None else None

        self.__rectangle: Optional[g.Rectangle] = g.Rectangle(position, self.__oppositePoint) if drawRectangle else None
        if rectangleFill is not None:
            self.__rectangle.setFill(rectangleFill)

        self.__text: Optional[g.Text] = g.Text(self.__midPoint, text) if text is not None else None
        self.__window: g.GraphWin = window

    def draw(self) -> None:
        if self.__rectangle is not None:
            self.__rectangle.draw(self.__window)
        if self.__text is not None:
            self.__text.draw(self.__window)
        if self.__image is not None:
            self.__image.draw(self.__window)

    @property
    def text(self) -> Optional[str]:
        return self.__text.getText() if self.__text is not None else None

    @text.setter
    def text(self, text: Optional[str]) -> None:
        if text is not None:
            if self.__text is None:
                self.__text = g.Text(self.__midPoint, text)
                self.__text.draw(self.__window)
            else:
                self.__text.setText(text)
        elif self.__text is not None:
            self.__text.undraw()
            self.__text = None

    def setDrawRectangle(self, draw: bool, rectangleFill: Optional[str] = None) -> None:
        if draw:
            if self.__rectangle is None:
                self.__rectangle = g.Rectangle(self.__position, self.__oppositePoint)
                self.__rectangle.draw(self.__window)
            if rectangleFill is not None:
                self.__rectangle.setFill(rectangleFill)
        elif self.__rectangle is not None:
            self.__rectangle.undraw()
            self.__rectangle = None

    def setFill(self, color: Optional[str]) -> None:
        if color is not None:
            if self.__rectangle is None:
                self.__rectangle = g.Rectangle(self.__position, self.__oppositePoint)
                self.__rectangle.draw(self.__window)
            self.__rectangle.setFill(color)
        elif self.__rectangle is not None:
            self.__rectangle.setFill("") # Unset the fill option. The empty string value was copied from the library sources.

    def setImage(self, path: Optional[str]) -> None:
        if self.__image is not None:
            self.__image.undraw()
        self.__image = g.Image(self.__midPoint, path) if path is not None else None
        if self.__image is not None:
            self.__image.draw(self.__window)

        # Recreate the text to correct the Z-order again
        if self.__text is not None:
            text = self.text
            self.text = None
            self.text = text
