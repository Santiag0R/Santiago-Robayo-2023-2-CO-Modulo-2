import random
import pygame
from dino_runner.components import obstacles

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        cactus_list = [SMALL_CACTUS,LARGE_CACTUS]
        cactus_type = random.randint(0,1)
        
        if len(self.obstacles)==0:
            cactus_cord_y = 0
            if cactus_type == 0:
                cactus_cord_y = 330
            else:
                cactus_cord_y = 305
            cactus = Cactus(cactus_list[cactus_type],cactus_cord_y)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw (self, screen):
        for obstacle in self.obstacles:  
            obstacle.draw(screen)
            