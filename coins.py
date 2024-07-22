import pygame
from PIL import Image
class Coins:
    def __init__(self, gs_game):
        self.screen = gs_game.screen
        self.screen_rect = self.screen.get_rect()
        self.frames = []
    for frame in range(pygame.image.load("images/")):
        self.frames.append(frame)