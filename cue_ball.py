import pygame
class CueBall:
    '''Class for cue ball and cue ball related things'''
    def __init__(self, billiards):
        self.settings = billiards.settings
        self.screen = billiards.screen
        self.screen_rect = self.screen.get_rect()
        self.x = self.settings.screen_width / 3
        self.y = self.settings.screen_height / 2
        self.x_vel = 0.1
        self.y_vel = -0.2
        self.radius = 10
    
    def draw_cue_ball(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), self.radius)
    
    def update_cue_ball(self):
        self.x += self.x_vel
        self.y += self.y_vel
    
    def detect_wall_collision(self):
        if (self.x + self.radius >= self.screen_rect.right - self.settings.border_thickness) or \
            (self.x - self.radius <= self.screen_rect.left + self.settings.border_thickness):
            self.x_vel *= -1
        if (self.y + self.radius >= self.screen_rect.bottom - self.settings.border_thickness) or \
            (self.y - self.radius <= self.screen_rect.top + self.settings.border_thickness):
            self.y_vel *= -1