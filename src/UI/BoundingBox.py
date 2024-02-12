from dataclasses import dataclass
import graphics as g


@dataclass
class BoundingBox:
    topLeft: g.Point
    bottomRight: g.Point

    def contains(self, point: g.Point) -> bool:
        return self.topLeft.x <= point.x <= self.bottomRight.x and self.topLeft.y <= point.y <= self.bottomRight.y
