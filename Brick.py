import pygame
from pygame.sprite import Sprite
import Resource

class Brick(Resource):

    sprite = pygame.image.load("MAKE THE GODDAMN RESOURCE IMAGES!!!!!!!!!!")


    def __init__(self, **keywords):
        super().__init__(**keywords)
        self.image = Brick.sprite

        self.type = "Brick
        self.resourceChange = 1
        self.resourceChange2 = 2
        self.name = "Brick"
