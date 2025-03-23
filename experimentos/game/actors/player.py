from pygame import Color, Rect, Surface
import pygame

from render.render_object import RenderObject

class Player(RenderObject):
    velocity_up: float = 300
    velocity_forward: float = 300

    def __init__(self):
        super().__init__(Rect(100,100,64,64))
    
    def draw(self, screen:Surface):
        pygame.draw.rect(screen, Color(255,0,0,255), self._rect)

    def update(self, delta):
        keys = pygame.key.get_pressed()
        
        forward = -1 if keys[pygame.K_a] else 0
        forward += 1 if keys[pygame.K_d] else 0
        forward *= delta*Player.velocity_forward

        up = -1 if keys[pygame.K_w] else 0
        up += 1 if keys[pygame.K_s] else 0
        up *= delta*Player.velocity_up


        self._rect = self._rect.move(forward, up)
