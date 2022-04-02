
from tkinter import CENTER
import pygame
import sys
from settings import Settings
from pockets import Pockets

class BilliardsGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height

        self.screen = pygame.display.set_mode((self.screen_width,
            self.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.border_thickness = 50

        self.table_width = self.screen_width - 2 *self.border_thickness
        self.table_height = self.screen_height - 2 * self.border_thickness
        self.table_rect = pygame.Rect(self.border_thickness,
            self.border_thickness, self.table_width, self.table_height)
        


        pygame.display.set_caption("Chilliard Billiard")

        self.run_game()
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((51, 26, 0))
            self.draw_side_pockets()
            self.draw_table()
            self.draw_pockets()
            pygame.display.flip()
                
    def draw_pockets(self):
        t = self.border_thickness
        pocket_locations = [(t, t), (self.screen_rect.right - t, t),
            (self.screen_rect.right - t, self.screen_rect.bottom - t),
            (t, self.screen_rect.bottom - t)]
        for loc in pocket_locations:
            pygame.draw.circle(self.screen, (0, 0, 0), loc, 40)
            continue
    
    def draw_side_pockets(self):
        t = self.border_thickness
        pygame.draw.circle(self.screen, (0, 0, 0), (self.screen_rect.centerx, t), 40)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.screen_rect.centerx, self.screen_rect.bottom - t), 40)

    def draw_table(self):
        pygame.draw.rect(self.screen, (27, 77, 0), self.table_rect)


if __name__ == "__main__":
    billiards = BilliardsGame()
    billiards.__init__()

#TODO update pocket locations
