import random

import pygame

from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Bird(Sprite):
    BIRD_HEIGHTS = [260, 220, 170]
    def __init__(self):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = SCREEN_WIDTH
        self.pos_y = random.choice(self.BIRD_HEIGHTS)
        self.step_index = 0
        self.bird_fly = True


    def update(self, game):
        if self.bird_fly:
            self.fly()
           

        if self.step_index > 10:
            self.step_index = 0


        if self.bird_rect.x < -SCREEN_WIDTH:
            self.bird_rect.x = SCREEN_WIDTH
            self.bird_rect.y = random.choice(self.BIRD_HEIGHTS)

        if game.player.dino_rect.colliderect(self.bird_rect):
                game.playing = False

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.bird_rect = self.image.get_rect()
         self.bird_rect.x = 
        self.bird_rect.y = self.pos_y 
        self.step_index += 1

    def map(self):


    def draw(self, screen):
       screen.blit(self.image, (self.bird_rect.x, self.bird_rect.y))


