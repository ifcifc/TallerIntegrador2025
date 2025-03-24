import pygame

pygame.init()

from actors.player import Player
from actors.text import Text
from actors.box import Box
from game.game_state import GameState
from game.scene_controller import SceneController
from render.scene import Scene

screen = pygame.display.set_mode((1280, 720))

scene1: Scene = Scene()
scene2: Scene = Scene()

scene1.add_object(Player())
scene2.add_object(Player())
scene2.add_object(Box())
scene2.add_object(Text())

#GameState.set_active_scene(scene)
GameState.add_global_script(SceneController(scene1, scene2))

GameState.set_active_scene(scene2)

#Interpolar es dificil
def game_logic():
    logic_clock = pygame.time.Clock() 

    while not GameState.quit:
        GameState.fixed_delta_time = logic_clock.tick(30)/1000
        
        ACTIVE_SCENE = GameState.get_active_scene()

        if ACTIVE_SCENE is None:
            continue 

        ACTIVE_SCENE.update(GameState.fixed_delta_time)


def render():
    clock = pygame.time.Clock()

    while not GameState.quit:
        ACTIVE_SCENE = GameState.get_active_scene()
        GameState.update()
        
        GameState.delta_time = clock.tick(60) / 1000

        pygame.display.set_caption(f"fps: {(clock.get_fps())}")

        if ACTIVE_SCENE is None:
            continue    
        
        ACTIVE_SCENE.draw(screen)

        pygame.display.flip()

        ACTIVE_SCENE.update(GameState.delta_time)
    

#logic_thread = threading.Thread(target=game_logic)

#logic_thread.start()
render()

#logic_thread.join()
pygame.quit()