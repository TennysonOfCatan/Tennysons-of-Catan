import pygame
from pygame.Sprite import Sprite
import Resource

class Wood(Resource):
    sprite = pygame.image.load("MAKE THE BLOODY IMAGE RESOURCES")

    def __init__(self, **keywords):
        super()/__init__(**keywords)
        self.image = Wood.sprite

        self.type = "Wood"
        self.resourceChange = 1
        self.resourceChange2 = 2
        self.name = "Wood"
        
