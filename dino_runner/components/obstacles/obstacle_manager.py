import pygame

from dino_runner.components.cactus import Cactus

from dino_runner.components.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.list_cactus = SMALL_CACTUS + LARGE_CACTUS
        self.bird = Bird()
                                                                                                                                                                                                                                                                                                                                                         
    def update(self,game):
        if len(self.obstacles) == 0:
            cactus = Cactus(self.list_cactus)
            self.obstacles.append(cactus)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)