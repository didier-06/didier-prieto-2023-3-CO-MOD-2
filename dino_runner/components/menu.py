import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER

class Menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2

    def __init__(self, screen, message):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.font_list_end = pygame.font.Font(FONT_STYLE, 20)
        self.list_end = ""
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)
        self.image_game_over = GAME_OVER
        self.max_score = 0

    def update(self, game):
        self.hundle_event_on_menu(game)
        pygame.display.update()

    def draw(self, screen, death, score):
        if score > self.max_score:
            self.max_score = score

        data_game = f""" SCORE = {score}
                         DEATHS = {death}
                         MAX SCORE = {self.max_score}              """

        self.list_end = self.font_list_end.render(data_game, True, (0, 0, 0))
        screen.blit(self.text, self.text_rect)
        if death > 0:
            scrren.blit(self.image_game_over,(self.half_screen_width, self.half_screen_height -50)
            screen.blit(self.list_end, (self.half_screen_width, self.half_screen_height -80) 





    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def hundle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
                game.death += 1
            elif event.type == pygame.KEYDOWN:
                game.run()
