import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER, BACKGROUND

class Menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2

    def __init__(self, screen):
        screen.blit(BACKGROUND, (0, 0))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.font_list_end = pygame.font.Font(FONT_STYLE, 20)
        self.image_game_over = GAME_OVER
        self.max_score = 0

    def update(self, game):
        self.hundle_event_on_menu(game)
        pygame.display.update()

    def draw(self, screen, death, score, message, game, x = half_screen_width, y = half_screen_height ):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        screen.blit(self.text, self.text_rect)
        if not game.playing:
            if score > self.max_score:
                self.max_score = score
            deaths = f"DEATHS: {death}"
            scores = f"SCORE: {score}"
            max_score_lis = f"MAX SCORE: {self.max_score}"
            deaths = self.font_list_end.render(deaths, True, (0, 0, 0))
            scores = self.font_list_end.render(scores, True, (0, 0, 0))
            max_score_lis = self.font_list_end.render(max_score_lis, True, (0, 0, 0))
            if death > 0:
                screen.blit(self.image_game_over,(self.half_screen_width - 200 , self.half_screen_height -250))
                screen.blit(scores ,(self.half_screen_width - 70, self.half_screen_height + 20))
                screen.blit(deaths ,(self.half_screen_width - 70, self.half_screen_height + 50))
                screen.blit(max_score_lis,(self.half_screen_width - 70, self.half_screen_height + 80))

    def reset_screen_color(self, screen):
        screen.blit(BACKGROUND, (0, 0))

    def hundle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()


