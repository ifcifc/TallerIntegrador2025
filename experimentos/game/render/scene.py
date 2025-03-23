from typing import Dict
from uuid import UUID

from pygame import Surface

from render.render_object import RenderObject


class Scene:
    _objects : Dict[UUID, RenderObject] 

    def __init__(self):
        self._objects = {}

    def add_object(self, render_object: RenderObject) -> bool:
        if render_object.get_id() in self._objects: 
            return False

        self._objects[render_object.get_id()] = render_object

        return True
    
    def draw(self, screen:Surface):
        screen.fill("black")
        
        draw_object = filter(lambda obj: not obj.is_hidden(), self._objects.values())
        for obj in draw_object:
            obj.draw(screen)
    
    def update(self, delta:float):
        for obj in self._objects.values():
            obj.update(delta)
