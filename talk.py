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
        self.prep_talk(self.results.left_roll_str, self.results.center_roll_str, self.results.right_roll_str)
    def prep_talk(self, left_roll, center_roll, right_roll):
        if (left_roll == center_roll) and (right_roll == center_roll) and (left_roll == right_roll):
            talk_str = "Jackpot!"
            self.talk_image = self.font.render(talk_str, True, self.text_color, (255,255,255))
            self.talk_rect = self.talk_image.get_rect()
            self.talk_rect.center = self.screen_rect.center
            self.talk_rect.top = self.screen_rect.top
        elif not((left_roll == center_roll) and not(right_roll == center_roll) and not(left_roll == right_roll)):
            talk_str = "Womp Womp"
            self.talk_image = self.font.render(talk_str, True, self.text_color, (255,255,255))
            self.talk_rect = self.talk_image.get_rect()
            self.talk_rect.center = self.screen_rect.center
            self.talk_rect.top = self.screen_rect.top
        else:
            talk_str = "So Close..."
            self.talk_image = self.font.render(talk_str, True, self.text_color, (255,255,255))
            self.talk_rect = self.talk_image.get_rect()
            self.talk_rect.center = self.screen_rect.center
            self.talk_rect.top = self.screen_rect.top
    def show_talk(self):
        self.screen.blit(self.talk_image, self.talk_rect)