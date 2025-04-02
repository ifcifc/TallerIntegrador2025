from pygame import Rect, Vector2

class Transform:
    position: Vector2
    size: Vector2
    scale: Vector2
    rotate: float

    def __init__(self, position=Vector2(), size=Vector2(), scale=Vector2(1,1), rotate=0):
        self.position = position
        self.size = size
        self.scale = scale
        self.rotate = rotate

    def from_parent(self, parent: "Transform") -> "Transform":
        return Transform(parent.position + self.position,
                         self.size,
                         parent.scale + self.scale,
                         (parent.rotate + self.rotate)%360)

    def get_rect(self) -> Rect:
        return Rect(*self.position.xy, *self.size.xy)