
import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    #image es una lista
    def __init__(self, image, bird_cord_y):
        #self.type es como un indice
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = bird_cord_y