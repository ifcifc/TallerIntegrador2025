from pygame import Color, Surface, Vector2
import pygame
from render.render_object import RenderObject
from render.transform import Transform

class Box(RenderObject):

    def __init__(self):
        super().__init__(Transform(Vector2(0,600),Vector2(800,64)))
    
    def draw(self, screen:Surface):

        pygame.draw.rect(screen, Color(128,128,0,255), self._transform.get_rect())
