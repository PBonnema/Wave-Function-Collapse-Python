import graphics as g


class DrawableTile:
    def __init__(self, position: g.Point, size: g.Point, window: g.GraphWin, text: str = "", fill: str = "White") -> None:
        self.__rectangle: g.Rectangle = g.Rectangle(position, g.Point(position.getX() + size.getX(), position.getY() + size.getY()))
        self.__rectangle.setFill(fill)
        self.__text: g.Text = g.Text(g.Point(position.getX() + size.getX() / 2.0, position.getY() + size.getY() / 2.0), text)
        self.__window: g.GraphWin = window

    def draw(self) -> None:
        self.__rectangle.draw(self.__window)
        self.__text.draw(self.__window)

    @property
    def text(self) -> str:
        return self.__text.getText()

    @text.setter
    def text(self, text: str) -> None:
        self.__text.setText(text)

    def setFill(self, color: str) -> str:
        return self.__rectangle.setFill(color)
