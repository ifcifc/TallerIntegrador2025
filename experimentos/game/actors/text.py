from tkinter.font import Font
from pygame import Color, Surface
import pygame

from actors.player import Player

class Text(Player):
    _font:Font = pygame.font.SysFont('Arial', 36)
    _text_surface:Surface = _font.render('¡Esto es un jugador!', True, (255, 255, 255))

    def __init__(self):
        super().__init__()
        self._rect = self._text_surface.get_rect()
    
    def draw(self, screen:Surface):
        pygame.draw.rect(screen, Color(255,128,0,255), self._rect)
        screen.blit(Text._text_surface, self._rect)