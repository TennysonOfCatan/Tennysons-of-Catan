import pygame
from pygame.Sprite import Sprite
import Resource

class Ore(Resource):
    sprite = pygame.image.load("MAKE THE BLOODY IMAGE RESOURCES")

    def __init__(self, **keywords):
        super().__init__(**keywords)
        self.image = Ore.sprite

        self.type = "Ore"
        self.resourceChange = 1
        self.resourceChange2 = 2
        self.name = "Ore"
        
