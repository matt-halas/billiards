import pygame
import numpy as np

class Cue:
    def __init__(self, billiards):
        self.screen = billiards.screen

        self.x = 200
        self.y = 200
        self.length = 200
    
    def draw_cue(self, cue_ball):
        self.x, self.y = pygame.mouse.get_pos()
        self.cue_ball_x = cue_ball.x
        self.cue_ball_y = cue_ball.y
        dx = self.x - self.cue_ball_x
        dy = self.y - self.cue_ball_y
        unit_vec_x = dx / np.sqrt(dx**2 + dy**2)
        unit_vec_y = dy / np.sqrt(dx**2 + dy**2)
        self.x_end = unit_vec_x * self.length + self.x
        self.y_end = unit_vec_y * self.length + self.y
        pygame.draw.line(self.screen, (70, 55, 0), (self.x, self.y), (self.x_end, self.y_end), 5)