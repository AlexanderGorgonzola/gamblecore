import pygame
import sys
from settings import Settings
from results import Results
from talk import Talk
class GambleSimulator:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.r = Results(self)
        self.t = Talk(self)
        pygame.display.set_caption("Slot Machine")
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
    def _update_screen(self):
        self.screen.blit(self.settings.bg, (0,-60))
        self.r.show_roll()
        self.t.show_talk()
        pygame.display.flip()
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

if __name__ == "__main__":
    gs = GambleSimulator()
    gs.run_game()