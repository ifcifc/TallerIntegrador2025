import pygame

pygame.init()

from actors.player import Player
from actors.text import Text
from game.game_state import GameState
from game.scene_controller import SceneController
from render.scene import Scene

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

scene1: Scene = Scene()
scene2: Scene = Scene()

scene1.add_object(Player())
scene2.add_object(Text())

#GameState.set_active_scene(scene)
GameState.add_global_script(SceneController(scene1, scene2))


while not GameState.quit:
    ACTIVE_SCENE = GameState.get_active_scene()
    GameState.update()
    
    dt = clock.tick(60) / 1000

    pygame.display.set_caption(f"fps: {(clock.get_fps())}")

    if ACTIVE_SCENE is None:
        continue    
    
    ACTIVE_SCENE.draw(screen)

    pygame.display.flip()

    ACTIVE_SCENE.update(dt)
    
