import random
import pygame
from dino_runner.components.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, SHIELD_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.list_cactus = SMALL_CACTUS + LARGE_CACTUS
                                                                                                                                                                                                                                                                                                                                                         
    def update(self,game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle_image(random.randint(0, 1))
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                # Controlando si el dino tiene shield o no
                if game.player.type != SHIELD_TYPE:
                    game.playing = False
                    game.death += 1
                    break
                else:
                    self.obstacles.remove(obstacle)

            if game.flag_hammer:
                if game.hammer.rect.colliderect(obstacle.rect):
                    self.obstacles.remove(obstacle)
                    game.hammer.flag_hammer = False

                    
                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def generate_obstacle_image(self, obstacle_type):
        if obstacle_type == 0:
            obstacle = Cactus(self.list_cactus)
        elif obstacle_type == 1:
            obstacle = Bird()
        return obstacle

    def reset_obstacles(self):
        self.obstacles = []
        
