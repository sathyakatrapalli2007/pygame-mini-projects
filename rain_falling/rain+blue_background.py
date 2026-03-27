import pygame
import sys
from rain import RainDrop
import random
class Blue:
    def __init__(self):
        pygame.init()

        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Rain")
        self.current_speed={}
        self.rain_drops=pygame.sprite.Group()
        self._create_drops()

        pygame.mixer.music.load("sound/rain.wav")
        pygame.mixer.music.play(-1)


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        sys.exit()

            self.screen.fill((208,235,246))
            self._update_drops()
            self.rain_drops.draw(self.screen)
            pygame.display.flip()

    def _update_drops(self):
        self.rain_drops.update()



    def _create_drops(self):
        drop=RainDrop(self)
        drop_width,drop_height=drop.rect.size
        current_x=0
        current_y=0
        while current_y<drop.screen_rect.height:
            while current_x<drop.screen_rect.width:
                new_drop=RainDrop(self)
                if current_x not in self.current_speed:
                    self.current_speed[current_x]=random.uniform(1,4)
                
                new_drop.rect.x=current_x
                new_drop.rect.y=current_y+random.randint(-50,50)
                new_drop.y=current_y+random.randint(-50,50)
                new_drop.speed=self.current_speed[current_x]
                current_x+=drop_width*3
                self.rain_drops.add(new_drop)
            current_x=0
            current_y+=drop_height*3

if __name__=="__main__":
    run=Blue()
    run.run_game()



