import pygame
from pygame.sprite import Sprite
import random

class RainDrop(Sprite):
    """A class to manage stars"""
    def __init__(self,grid):
        super().__init__()
        self.screen=grid.screen
        self.screen_rect=self.screen.get_rect()

        self.image=pygame.image.load('image/rain_drop.bmp')
        self.image=pygame.transform.smoothscale(self.image,(3,50))

        self.rect=self.image.get_rect()

        #self.rect.x=self.rect.width
        #self.rect.y=self.rect.height

        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

        self.speed=random.uniform(1,4)

    def update(self):
        self.y+=1*self.speed
        self.rect.y=self.y
        if self.rect.y>=self.screen_rect.height:
            self._reset_drops()

    def _reset_drops(self):
        self.y=random.uniform(-100,-10)
        self.rect.y=self.y


