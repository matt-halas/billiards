import pygame
import numpy as np

class Ball:
    def __init__(self, billiards, loc, color):
        self.settings = billiards.settings
        self.screen = billiards.screen
        self.screen_rect = self.screen.get_rect()
        self.x, self.y = loc
        self.x_vel = 0
        self.y_vel = 0
        self.radius = 10
        self.color = color

    def draw_ball(self):
        pygame.draw.circle(self.screen, (self.color), (self.x, self.y), self.radius)
    
    def update_ball(self):
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
            self.sink_ball()
        #Check for top right pocket
        if np.sqrt((self.settings.screen_width - 2 * self.settings.border_thickness
            - self.x_tab)**2 + self.y_tab**2) < self.settings.pocket_radius:
            self.sink_ball()
        #Check for bottom right pocket
        if np.sqrt((self.settings.screen_width - 2 * self.settings.border_thickness - self.x_tab)**2
            + (self.settings.screen_height - 2 * self.settings.border_thickness - self.y_tab)**2) < self.settings.pocket_radius:
            self.sink_ball()
        #Check for bottom left pocket
        if np.sqrt(self.x_tab**2 + (self.settings.screen_height - 2 * self.settings.border_thickness - self.y_tab)**2) < self.settings.pocket_radius:
            self.sink_ball()
        #Check for side pockets
        if (self.y < self.settings.border_thickness) or (self.y > self.screen_rect.bottom - self.settings.border_thickness):
            self.sink_ball()
        
    def sink_ball(self):
        self.x = -100
        self.y = -100
        self.x_vel = 0
        self.y_vel = 0