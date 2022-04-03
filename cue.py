import pygame
import numpy as np

class Cue:
    def __init__(self, billiards):
        self.screen = billiards.screen

        self.x = 200
        self.y = 200
        self.max_length = 250
        self.strength = 0.1
        self.max_strength = 0.2
    
    def draw_cue(self, cue_ball):
        self.x, self.y = pygame.mouse.get_pos()
        self.cue_ball_x = cue_ball.x
        self.cue_ball_y = cue_ball.y
        dx = self.x - self.cue_ball_x
        dy = self.y - self.cue_ball_y
        self.unit_vec_x = dx / np.sqrt(dx**2 + dy**2)
        self.unit_vec_y = dy / np.sqrt(dx**2 + dy**2)
        self.length = self.strength / self.max_strength * self.max_length
        self.x_end = self.unit_vec_x * self.length + self.x
        self.y_end = self.unit_vec_y * self.length + self.y
        pygame.draw.line(self.screen, (70, 55, 0), (self.x, self.y), (self.x_end, self.y_end), 5)
    
    def cue_hit(self, cue_ball):
        #TODO: Add speed changes to cue
        cue_ball.x_vel = -self.unit_vec_x * self.strength
        cue_ball.y_vel = -self.unit_vec_y * self.strength
    
    def power_up(self):
        if self.strength < self.max_strength:
            self.strength += 0.01

    def power_down(self):
        if self.strength > 0.03:
            self.strength -= 0.01