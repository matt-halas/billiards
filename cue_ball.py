import pygame
class CueBall:
    '''Class for cue ball and cue ball related things'''
    def __init__(self, billiards):
        self.settings = billiards.settings
        self.screen = billiards.screen
        self.x = self.settings.screen_width / 3
        self.y = self.settings.screen_height / 2
        self.x_vel = 0
        self.y_vel = 0
    
    def draw_cue_ball(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 10)
    
    def update_cue_ball(self):
        self.x += self.x_vel
        self.y += self.y_vel