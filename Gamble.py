import time
import pygame
import sys
from settings import Settings
from results import Results, Effect
from talk import Talk
class GambleSimulator:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.r = Results(self)
        self.t = Talk(self)
        self.e = Effect(self)

        self.money = 500

        pygame.display.set_caption("Gamblecore")
        pygame.mixer.music.load("sounds/gamblecore.mp3")
        pygame.mixer.music.set_volume(100)
        pygame.mixer.music.play(-1)
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.r.left_roll()
                    self.r.center_roll()
                    self.r.right_roll()
                    self.t.prep_talk(self.r.left_roll_str, self.r.center_roll_str, self.r.right_roll_str)
                    if self.t.win == True:
                        self.money += 110
                    elif self.t.win == "maybe":
                        self.money += 30
                    self.money -= 10
                    time.sleep(0.3)
    def _update_screen(self):
        self.screen.blit(self.settings.bg, (0,-60))
        self.t.money(self.money)
        self.r.show_roll()
        self.t.show_talk()
        self.e.draw_effect()
        pygame.display.flip()
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

if __name__ == "__main__":
    gs = GambleSimulator()
    gs.run_game()