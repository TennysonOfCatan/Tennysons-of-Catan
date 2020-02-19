import pygame, unit, helper, bmpfont
from pygame.sprite import Sprite

SIZE = 50

class BaseResource(Sprite):

    def __init__(self, tile-x = None, tile_y = None, Number = None **keywords):
        Sprite.__init__(self)

        #turn keywords off for now
        self.Number = number

        #pygame reqs
        self.image = None
        self.rect = pygame.Rect(0, 0, SIZE, SIZE)





        
