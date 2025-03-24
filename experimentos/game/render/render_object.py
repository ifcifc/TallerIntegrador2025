from uuid import UUID

from pygame import Rect, Surface

class RenderObject:
    _rect: Rect
    _object_id: UUID
    _is_hidden:bool

    def __init__(self, rect=Rect(0,0,0,0), object_id=None):
        self._rect = rect
        self._object_id = object_id
        self._is_hidden = False
    
    def get_rect(self) -> Rect:
        return self._rect
    
    def get_id(self) -> UUID:
        return self._object_id
    
    def is_hidden(self) -> bool:
        return self._is_hidden

    def set_hidden(self, hidden=False):
        self._is_hidden = hidden

    def draw(self, screen:Surface):
        pass

    def update(self, delta:float):
        pass
    