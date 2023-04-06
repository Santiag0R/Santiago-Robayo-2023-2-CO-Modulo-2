import random
import pygame
from dino_runner.components.power_ups.hammer import Hammer

from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups=[]
        self.duration = random.randint(3,5)
        self.when_appears = random.randint(50,70)

    def update(self, game):
        # game.score = 55
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)  #para que el dino no muera al estrellarse
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                if isinstance(power_up,Shield):
                    game.player.type = SHIELD_TYPE
                elif isinstance(power_up,Hammer):
                    game.player.type = HAMMER_TYPE               
                game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)
            #elif game.player.dino_rect.colliderect(power_up.rect):
             #   power_up.start_time = pygame.time.get_ticks()
              #  game.player.has_power_up = True
               # game.player.type = HAMMER_TYPE
                #game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                #self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(50,70)
    
    def generate_power_up(self):  
        self.when_appears += random.randint(150,300)
        power_up = random.choice((Shield(),Hammer()))
        #power_up = self.power_list[0]
        self.power_ups.append(power_up)