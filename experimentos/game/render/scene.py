from typing import Dict, List
from uuid import UUID, uuid4

from pygame import Rect, Surface
import pygame

from render.render_object import RenderObject


class Scene:
    _objects : Dict[UUID, RenderObject] 

    def __init__(self):
        self._objects = {}

    def add_object(self, render_object: RenderObject) -> bool:
        if render_object.get_id() is None:
            #no se deberia de hacer, solucionar
            render_object._object_id = uuid4()

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

    def find_collisions(self, r_obj:RenderObject|Rect)->List[RenderObject]:
        if isinstance(r_obj, Rect):
            return r_obj.collideobjectsall(tuple(self._objects.values()), key=lambda obj: obj.get_rect())
        else:
            r_obj_id = r_obj.get_id()
            flt = filter(lambda obj: obj.get_id()!=r_obj_id, self._objects.values())
            return r_obj.get_transform().get_rect().collideobjectsall(tuple(flt), key=lambda obj: obj.get_transform().get_rect())
