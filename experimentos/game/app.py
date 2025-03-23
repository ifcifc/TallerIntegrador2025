import pygame

from actors.player import Player
from game.game_state import GameState
from render.scene import Scene

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

scene: Scene = Scene()

scene.add_object(Player())

GameState.set_active_scene(scene)

while not GameState.quit:
    GameState.update()
    active_scene = GameState.get_active_scene()
    
    dt = clock.tick(60) / 1000

    screen.fill("black")

    active_scene.draw(screen)

    pygame.display.flip()

    active_scene.update(dt)
    
