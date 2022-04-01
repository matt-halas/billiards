import pygame
class Pockets:
    def __init__(self, billiards, pos):
        self.screen = billiards.screen
        self.settings = billiards.settings
        pygame.draw.circle(self.screen, (0, 0, 0), pos, 20)