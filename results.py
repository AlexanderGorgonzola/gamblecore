import pygame.font
import pygame
import random
class Results:
    def __init__(self, gs_game):
        self.screen = gs_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gs_game.settings
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 400)
        self.left_roll()
        self.center_roll()
        self.right_roll()
    def left_roll(self):
        self.left_roll_str = str(random.randint(1,9))
        self.left_roll_image = self.font.render(self.left_roll_str, True, self.text_color, (255,255,255))
        self.left_roll_rect = self.left_roll_image.get_rect()
        self.left_roll_rect.center = self.screen_rect.center
        self.left_roll_rect.left = self.screen_rect.left + 290
    def right_roll(self):
        self.right_roll_str = str(random.randint(1,9))
        self.right_roll_image = self.font.render(self.right_roll_str, True, self.text_color, (255,255,255))
        self.right_roll_rect = self.right_roll_image.get_rect()
        self.right_roll_rect.center = self.screen_rect.center
        self.right_roll_rect.right = self.screen_rect.right - 360
    def center_roll(self):
        self.center_roll_str = str(random.randint(1,9))
        self.center_roll_image = self.font.render(self.center_roll_str, True, self.text_color, (255,255,255))
        self.center_roll_rect = self.center_roll_image.get_rect()
        self.center_roll_rect.center = self.screen_rect.center
        self.center_roll_rect.left = self.screen_rect.left + 480
    def show_roll(self):
        self.screen.blit(self.left_roll_image, self.left_roll_rect)
        self.screen.blit(self.right_roll_image, self.right_roll_rect)
        self.screen.blit(self.center_roll_image, self.center_roll_rect)