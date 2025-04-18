from pygame import Color, Surface, Vector2
import pygame

from game.game_state import GameState
from render.render_object import RenderObject
from render.transform import Transform

class Player(RenderObject):
    velocity_up: float = 300*2
    velocity_forward: float = 300*2
    gravity: float = 250

    def __init__(self):
        super().__init__(transform=Transform(Vector2(100,100),Vector2(64,64)))
        self._last_position = Vector2(100,100)
    
    def draw(self, screen:Surface):
        rect = self._transform.get_rect()
        pygame.draw.rect(screen, Color(255,0,0,255), rect)

    def update(self, delta):
        keys = pygame.key.get_pressed()
        
        forward = -1 if keys[pygame.K_a] else 0
        forward += 1 if keys[pygame.K_d] else 0
        forward *= delta*Player.velocity_forward

        up = -1 if keys[pygame.K_w] else 0


        rect = self._transform.get_rect()

        pos_bottom = rect.bottom
        grav = 0
        collisions = GameState.get_active_scene().find_collisions(self)
        collisions = tuple(filter(lambda obj: (pos_bottom-obj.get_transform().get_rect().bottom)<0, collisions))
        #pos_y = min(collisions, key=lambda obj: obj.get_rect().y)
        if len(collisions)==0:
            grav = Player.gravity * delta
            if keys[pygame.K_s]:
                up += 1 

        up = up*delta*Player.velocity_up + grav

        if forward!=0 or up!=0:
            self._transform.position+=Vector2(forward, up)
