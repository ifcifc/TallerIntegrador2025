from uuid import UUID

from pygame import Surface

from render.transform import Transform

class RenderObject:
    _object_id: UUID
    _is_hidden:bool
    _transform: Transform

    def __init__(self, transform=Transform(), object_id=None):
        if not isinstance(transform, Transform):
            raise TypeError("transform no es una instancia de Transform") 
        self._transform = transform
        self._object_id = object_id
        self._is_hidden = False
    
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
    
    def get_transform(self)->Transform:
        return self._transform