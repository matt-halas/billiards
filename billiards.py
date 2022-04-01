
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

        self.border_thickness = 100

        self.table_width = self.screen_width - self.border_thickness
        self.table_height = self.screen_height - self.border_thickness
        self.table_rect = pygame.Rect(self.border_thickness / 2,
            self.border_thickness / 2, self.table_width, self.table_height)
        


        pygame.display.set_caption("Chilliard Billiard")

        self.run_game()
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((51, 26, 0))
            self.draw_pockets()
            self.draw_table()
            pygame.display.flip()
    
    def draw_pockets(self):
        pocket_locations = [self.screen_rect.topleft, self.screen_rect.midtop,
            self.screen_rect.topright, self.screen_rect.bottomright,
            self.screen_rect.midbottom, self.screen_rect.bottomleft]
        for loc in pocket_locations:
            pygame.draw.circle(self.screen, (0, 0, 0), loc, 40)
    
    def draw_table(self):
        pygame.draw.rect(self.screen, (27, 77, 0), self.table_rect)


if __name__ == "__main__":
    billiards = BilliardsGame()
    billiards.__init__()

#TODO update pocket locations
