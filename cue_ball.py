import pygame
import numpy as np
class CueBall:
    '''Class for cue ball and cue ball related things'''
    def __init__(self, billiards):
        self.settings = billiards.settings
        self.screen = billiards.screen
        self.screen_rect = self.screen.get_rect()
        self.x = self.settings.screen_width / 3
        self.y = self.settings.screen_height / 2
        self.x_vel = 0
        self.y_vel = 0
        self.radius = 10
    
    def draw_cue_ball(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.radius)
    
    def update_cue_ball(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.x_vel *= 0.9998
        self.y_vel *= 0.9998
        if self.x_vel**2 + self.y_vel**2 < 0.0001:
            self.x_vel = 0
            self.y_vel = 0
    
    def detect_wall_collision(self):
        if (self.x + self.radius >= self.screen_rect.right - self.settings.border_thickness) or \
            (self.x - self.radius <= self.screen_rect.left + self.settings.border_thickness):
            self.x_vel *= -1
        #Wall collision for bottom
        if (self.y + self.radius >= self.screen_rect.bottom - self.settings.border_thickness) and \
            ((self.x > self.screen_rect.centerx + self.settings.pocket_radius) or (self.x < self.screen_rect.centerx - self.settings.pocket_radius)):
            self.y_vel = -np.abs(self.y_vel)
        #Wall collision for top
        if (self.y - self.radius <= self.settings.border_thickness) and \
            ((self.x > self.screen_rect.centerx + self.settings.pocket_radius) or (self.x < self.screen_rect.centerx - self.settings.pocket_radius)):
            self.y_vel = np.abs(self.y_vel)
    
    def detect_pocket_collision(self):
        self.x_tab = self.x - self.settings.border_thickness
        self.y_tab = self.y - self.settings.border_thickness
        #Check for top left pocket
        if np.sqrt(self.x_tab**2 + self.y_tab**2) < self.settings.pocket_radius:
            self.reset_cue_ball()
        #Check for top right pocket
        if np.sqrt((self.settings.screen_width - 2 * self.settings.border_thickness
            - self.x_tab)**2 + self.y_tab**2) < self.settings.pocket_radius:
            self.reset_cue_ball()
        #Check for bottom right pocket
        if np.sqrt((self.settings.screen_width - 2 * self.settings.border_thickness - self.x_tab)**2
            + (self.settings.screen_height - 2 * self.settings.border_thickness - self.y_tab)**2) < self.settings.pocket_radius:
            self.reset_cue_ball()
        #Check for bottom left pocket
        if np.sqrt(self.x_tab**2 + (self.settings.screen_height - 2 * self.settings.border_thickness - self.y_tab)**2) < self.settings.pocket_radius:
            self.reset_cue_ball()
        #Check for side pockets
        if (self.y < self.settings.border_thickness) or (self.y > self.screen_rect.bottom - self.settings.border_thickness):
            self.reset_cue_ball()

    def reset_cue_ball(self):
        self.x = self.settings.screen_width / 3
        self.y = self.settings.screen_height / 2
        self.x_vel = 0
        self.y_vel = 0