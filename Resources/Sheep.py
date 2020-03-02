import pygame
from pygame.Sprite import Sprite
import Resource

class Sheep(Resource):
    sprite = pygame.image.load("MAKE THE BLOODY IMAGE RESOURCES")

    def __init__(self, **keywords):
        super()/__init__(**keywords)
        self.image = Sheep.sprite

        self.type = "Shep"
        self.resourceChange = 1
        self.resourceChange2 = 2
        self.name = "Sheep"
        
