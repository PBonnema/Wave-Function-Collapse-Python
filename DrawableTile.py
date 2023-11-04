import dataclasses
from typing import Optional
import graphics as g

from DrawableTileScope import DrawableTileScope
from NoRectangleShownError import NoRectangleShownError


class DrawableTile:
    DEFAULT_RECTANGLE_FILL_COLOR = ""
    DEFAULT_RECTANGLE_EDGE_COLOR = "black"
    DEFAULT_RECTANGLE_EDGE_THICKNESS = 1

    def __init__(self, position: g.Point, size: g.Point, window: g.GraphWin, drawRectangle: bool = True, text: Optional[str] = None, imagePath: Optional[str] = None) -> None:
        self.__position: g.Point = position
        self.__size: g.Point = size
        self.__midPoint: g.Point = g.Point(position.getX() + size.getX() / 2.0, position.getY() + size.getY() / 2.0)
        self.__oppositePoint: g.Point = g.Point(self.__position.getX() + self.__size.getX(), self.__position.getY() + self.__size.getY())

        # Create the assets in reverse Z-order (from bottom to top)
        self.__image: Optional[g.Image] = g.Image(self.__midPoint, imagePath) if imagePath is not None else None
        self.__rectangle: Optional[g.Rectangle] = g.Rectangle(position, self.__oppositePoint) if drawRectangle else None
        self.__text: Optional[g.Text] = g.Text(self.__midPoint, text) if text is not None else None

        self.__window: g.GraphWin = window

        # These default values were copied from the graphics library sources
        self.__currentDrawableTileScope = DrawableTileScope(
            self,
            DrawableTile.DEFAULT_RECTANGLE_FILL_COLOR,
            DrawableTile.DEFAULT_RECTANGLE_EDGE_COLOR,
            DrawableTile.DEFAULT_RECTANGLE_EDGE_THICKNESS,
            imagePath,
            drawRectangle,
            text)
        self.__originalDrawableTileScope = self.__currentDrawableTileScope

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

        self.__currentDrawableTileScope.text = text

    def setDrawRectangle(self, draw: bool) -> None:
        if draw:
            if self.__rectangle is None:
                self.__rectangle = g.Rectangle(self.__position, self.__oppositePoint)
                self.__rectangle.draw(self.__window)
                self.__currentDrawableTileScope.fillColor = DrawableTile.DEFAULT_RECTANGLE_FILL_COLOR
                self.__currentDrawableTileScope.edgeColor = DrawableTile.DEFAULT_RECTANGLE_EDGE_COLOR
                self.__currentDrawableTileScope.edgeThickness = DrawableTile.DEFAULT_RECTANGLE_EDGE_THICKNESS
        elif self.__rectangle is not None:
            self.__rectangle.undraw()
            self.__rectangle = None

        self.__currentDrawableTileScope.drawRectangle = draw

    def setFill(self, color: str) -> None:
        if self.__rectangle is None:
            raise NoRectangleShownError
        self.__rectangle.setFill(color)

        self.__currentDrawableTileScope.fillColor = color

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

        self.__currentDrawableTileScope.imagePath = path

    def setEdgeColor(self, color: str) -> None:
        if self.__rectangle is None:
            raise NoRectangleShownError
        self.__rectangle.setOutline(color)

        self.__currentDrawableTileScope.edgeColor = color

    def setEdgeThickness(self, thickness: float) -> None:
        if self.__rectangle is None:
            raise NoRectangleShownError
        self.__rectangle.setWidth(thickness)

        self.__currentDrawableTileScope.edgeThickness = thickness

    def startScopedDrawing(self) -> DrawableTileScope:
        oldScope: DrawableTileScope = self.__currentDrawableTileScope
        self.__currentDrawableTileScope = dataclasses.replace(self.__currentDrawableTileScope)
        return oldScope

    def startUnscopedDrawing(self) -> DrawableTileScope:
        oldScope: DrawableTileScope = self.__currentDrawableTileScope
        self.__currentDrawableTileScope = self.__originalDrawableTileScope
        self.restoreFromScope(self.__currentDrawableTileScope)
        return oldScope

    def restoreFromScope(self, scope: DrawableTileScope) -> None:
        self.__currentDrawableTileScope = scope
        self.setDrawRectangle(scope.drawRectangle)
        if scope.drawRectangle:
            self.setEdgeColor(scope.edgeColor)
            self.setFill(scope.fillColor)
            self.setEdgeThickness(scope.edgeThickness)
        self.text = scope.text
        self.setImage(scope.imagePath)
