import pygame.font
import pygame
from results import Results
from pygame import mixer
class Talk:
    def __init__(self, gs_game):
        mixer.init()
        self.screen = gs_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gs_game.settings
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 100)
        self.big_font = pygame.font.SysFont(None, 200)
        self.font_2 = pygame.font.SysFont(None, 70)
        self.results = Results(self)
        self.prep_talk(self.results.left_roll_str, self.results.center_roll_str, self.results.right_roll_str)
        self.info()
        self.money(500)
        self.win = False

        self.win = pygame.mixer.Sound("sounds/win.mp3")
        self.meh = pygame.mixer.Sound("sounds/v.mp3")
        self.never = pygame.mixer.Sound("sounds/pipe.mp3")
    def prep_talk(self, left_roll, center_roll, right_roll):
        if right_roll == center_roll and center_roll == left_roll and right_roll == left_roll:
            self.win = True
            talk_str = "Jackpot!"
            self.talk_image = self.big_font.render(talk_str, True, self.text_color, (255,255,255))
            self.talk_rect = self.talk_image.get_rect()
            pygame.mixer.Sound("sounds/win.mp3").play()
        elif not(left_roll == center_roll) and not(right_roll == center_roll) and not(left_roll == right_roll):
            self.win = False
            talk_str = "Womp Womp"
            self.talk_image = self.big_font.render(talk_str, True, self.text_color, (255,255,255))
            self.talk_rect = self.talk_image.get_rect()
            pygame.mixer.Sound("sounds/pipe.mp3").play()
        elif left_roll == center_roll or left_roll == right_roll or center_roll == right_roll:
            if left_roll == right_roll:
                self.win = "maybe"
            else:
                self.win = False
            talk_str = "So Close..."
            self.talk_image = self.big_font.render(talk_str, True, self.text_color, (255,255,255))
            self.talk_rect = self.talk_image.get_rect()
            pygame.mixer.Sound("sounds/v.mp3").play()

        self.talk_rect.center = self.screen_rect.center
        self.talk_rect.top = self.screen_rect.top

    def info(self):
        self.info_image = self.font.render("PRESS SPACE TO ROLL", True, self.text_color, (255,255,255))
        self.info_rect = self.info_image.get_rect()
        self.info_rect.center = self.screen_rect.center
        self.info_rect.bottom = self.screen_rect.bottom
    
    def money(self, money):
        self.money_image = self.font_2.render(f"Money: {money}", True, self.text_color, (255, 255, 255))
        self.money_rect = self.money_image.get_rect()
        self.money_rect.left = self.screen_rect.left
        self.money_rect.bottom = self.screen_rect.bottom - 400
            
    def show_talk(self):
        self.screen.blit(self.talk_image, self.talk_rect)
        self.screen.blit(self.info_image, self.info_rect)
        self.screen.blit(self.money_image, self.money_rect)