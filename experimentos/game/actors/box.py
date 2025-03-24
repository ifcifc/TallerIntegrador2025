from pygame import Color, Rect, Surface
import pygame
from render.render_object import RenderObject

class Box(RenderObject):

    def __init__(self):
        super().__init__(Rect(0,600,800,64))
    
    def draw(self, screen:Surface):
        pygame.draw.rect(screen, Color(128,128,0,255), self._rect)
