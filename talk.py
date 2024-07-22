import pygame.font
import pygame
from results import Results
class Talk:
    def __init__(self, gs_game):
        self.screen = gs_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gs_game.settings
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 100)
        self.results = Results(self)
        self.prep_talk()
    def prep_talk(self):
        if (self.results.left_roll == self.results.center_roll) and (self.results.right_roll == self.results.center_roll) and (self.results.left_roll == self.results.right_roll):
            talk_str = "Jackpot!"
            self.talk_image = self.font.render(talk_str, True, self.text_color, self.settings.bg_color)
            self.talk_rect = self.talk_image.get_rect()
            self.talk_rect.center = self.screen_rect.center
            self.talk_rect.top = self.screen_rect.top
        elif not((self.results.left_roll == self.results.center_roll) and not(self.results.right_roll == self.results.center_roll) and not(self.results.left_roll == self.results.right_roll)):
            talk_str = "Womp Womp"
            self.talk_image = self.font.render(talk_str, True, self.text_color, self.settings.bg_color)
            self.talk_rect = self.talk_image.get_rect()
            self.talk_rect.center = self.screen_rect.center
            self.talk_rect.top = self.screen_rect.top
        else:
            talk_str = "So Close..."
            self.talk_image = self.font.render(talk_str, True, self.text_color, self.settings.bg_color)
            self.talk_rect = self.talk_image.get_rect()
            self.talk_rect.center = self.screen_rect.center
            self.talk_rect.top = self.screen_rect.top
    def show_talk(self):
        self.screen.blit(self.talk_image, self.talk_rect)