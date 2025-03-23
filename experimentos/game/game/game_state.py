from typing import Any, Callable, List
from pygame.event import Event
import pygame


from game.script import Script
from render.scene import Scene

class GameState:
    quit: bool = False
    _active_scene: Scene = None
    _global_scripts: List[Script] = []


    @staticmethod
    def update(func:Callable[[Event], Any]=None):
        scripts = filter(lambda s: not s.is_disabled(), GameState._global_scripts) 

        for script in scripts:
            script.update()

        for event in pygame.event.get():
            if not func is None:
                func(event)

            if event.type == pygame.QUIT:
                GameState.quit = True

    @staticmethod
    def get_active_scene() -> Scene:
        return GameState._active_scene
    
    @staticmethod
    def add_global_script(script:Script):
        GameState._global_scripts.append(script)

    @staticmethod
    def set_active_scene(scene: Scene) -> Scene:
        GameState._active_scene = scene