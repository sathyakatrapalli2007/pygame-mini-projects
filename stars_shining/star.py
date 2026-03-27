import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to manage stars"""
    def __init__(self,grid):
        super().__init__()
        self.screen=grid.screen
        self.screen_rect=self.screen.get_rect()

        self.image=pygame.image.load('images13/star.bmp')
        self.image=pygame.transform.smoothscale(self.image,(60,60))
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

