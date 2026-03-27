import pygame
import sys
from star import Star
from star_shine import StarShine


class Grid:
    """A grid of stars"""
    def __init__(self):
        """Initialize the required attributes"""
        pygame.init()

        """Set the screen"""
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Stars")

        self.stars=pygame.sprite.Group()
        self.starshine=pygame.sprite.Group()
        self._create_star_grid()
        self._create_star_shine_grid()

        self.whatshine=False
        self.timer=0
        self.switch_timer=60

        pygame.mixer.music.load('soothing.mp3')
        pygame.mixer.music.play(-1)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        sys.exit()

            self.timer+=1
            if self.timer>=self.switch_timer:
                self.timer=0
                self.whatshine= not self.whatshine

            self.screen.fill((254,211,225))

            if self.whatshine:
                self.starshine.draw(self.screen)

            else:
                self.stars.draw(self.screen)
            pygame.mouse.set_visible(False)
            pygame.display.flip()
 

    def _create_star_grid(self):
        star=Star(self)
        star_width,star_height=star.rect.size
        current_x=0
        current_y=0
        while current_y<=star.screen_rect.height-star_height:
            while current_x<star.screen_rect.width-star_width:
                new_star=Star(self)
                new_star.rect.x=current_x
                new_star.rect.y=current_y
                current_x+=star_width
                self.stars.add(new_star)
            current_x=0
            current_y+=star_height

    def _create_star_shine_grid(self):
        star=StarShine(self)
        star_width,star_height=star.rect.size
        current_x=0
        current_y=0
        while current_y<=star.screen_rect.height-star_height:
            while current_x<star.screen_rect.width-star_width:
                new_star=StarShine(self)
                new_star.rect.x=current_x
                new_star.rect.y=current_y
                current_x+=star_width
                self.starshine.add(new_star)
            current_x=0
            current_y+=star_height



if __name__=="__main__":
    grid=Grid()
    grid.run_game()