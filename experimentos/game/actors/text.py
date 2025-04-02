from tkinter.font import Font
from pygame import Color, Surface, Vector2
import pygame

from actors.player import Player
from render.transform import Transform

class Text(Player):
    _font:Font = pygame.font.SysFont('Arial', 36)
    _text_surface:Surface = _font.render('¡Esto es un jugador!', True, (255, 255, 255))

    def __init__(self):
        super().__init__()
        rect = self._text_surface.get_rect()
        self._transform = Transform(Vector2(rect.x, rect.y), Vector2(rect.w, rect.h))
    
    def draw(self, screen:Surface):
        pygame.draw.rect(screen, Color(255,128,0,255), self._transform.get_rect())
        screen.blit(Text._text_surface, self._transform.get_rect())