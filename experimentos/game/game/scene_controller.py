from typing import List

import pygame
from game.game_state import GameState
from game.script import Script
from render.scene import Scene

class SceneController(Script):
    _scenes: List[Scene]
    _active_scene: int
    _key_press: bool

    def __init__(self, *scenes):
        super().__init__()
        self._scenes = scenes
        self._active_scene = 0
        self._key_press = False
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_KP_ENTER]:
            if not self._key_press:
                self._active_scene += 1
                self._active_scene %= len(self._scenes)
                self._key_press = True
                GameState.set_active_scene(self._scenes[self._active_scene])
        else:
            self._key_press = False
