import pygame
import sys
import numpy as np
from settings import Settings
from cue_ball import CueBall
from cue import Cue
from ball import Ball


class BilliardsGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height

        self.screen = pygame.display.set_mode((self.screen_width,
            self.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.border_thickness = self.settings.border_thickness

        self.table_width = self.screen_width - 2 *self.border_thickness
        self.table_height = self.screen_height - 2 * self.border_thickness
        self.table_rect = pygame.Rect(self.border_thickness,
            self.border_thickness, self.table_width, self.table_height)
        
        self.cue_ball = CueBall(self)
        self.cue = Cue(self)
        # TODO: Add game control
        self.ball_colors = [(230, 191, 0), (21, 0, 128), (255, 85, 0),
            (119, 0, 179), (0, 128, 0), (0, 0, 0), (255, 25, 25),
            (200, 0, 0), (0, 0, 200), (0, 200, 0)] 
        self.ball_loc = [(500, 200), (520,  185), (520, 215),
            (540, 200), (540,  170), (540, 230), (560, 185),
            (560, 155), (560, 215), (560, 245)]
        self.balls = []
        for color, loc in zip(self.ball_colors, self.ball_loc):
            self.balls.append(Ball(self, loc, color))

        pygame.display.set_caption("Chilliard Billiard")

        self.run_game()
    
    def run_game(self):
        while True:
            self.check_events()
            self.draw_game()
            self.cue_ball.detect_wall_collision()
            self.cue_ball.detect_pocket_collision()
            self.detect_collisions()
            for ball in self.balls:
                ball.detect_wall_collision()
                ball.detect_pocket_collision()
                ball.update_ball()
            self.cue_ball.update_cue_ball()
            pygame.display.flip()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.cue.power_up()
                if event.key == pygame.K_DOWN:
                    self.cue.power_down()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.cue.cue_hit(self.cue_ball)
    
    def draw_game(self):
        self.screen.fill((51, 26, 0))
        self.draw_side_pockets()
        self.draw_table()
        self.draw_pockets()
        self.cue_ball.draw_cue_ball()
        for ball in self.balls:
            ball.draw_ball()
        self.cue.draw_cue(self.cue_ball)

    def draw_pockets(self):
        t = self.border_thickness
        pocket_locations = [(t, t), (self.screen_rect.right - t, t),
            (self.screen_rect.right - t, self.screen_rect.bottom - t),
            (t, self.screen_rect.bottom - t)]
        for loc in pocket_locations:
            pygame.draw.circle(self.screen, (0, 0, 0), loc, self.settings.pocket_radius)
    
    def draw_side_pockets(self):
        t = self.border_thickness
        pygame.draw.circle(self.screen, (0, 0, 0), (self.screen_rect.centerx, t), self.settings.pocket_radius)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.screen_rect.centerx, self.screen_rect.bottom - t),
            self.settings.pocket_radius)

    def draw_table(self):
        pygame.draw.rect(self.screen, (27, 77, 0), self.table_rect)
    
    def detect_collisions(self):
        for ball in self.balls:
            if np.sqrt((self.cue_ball.x - ball.x)**2 + (self.cue_ball.y - ball.y)**2) <= 2 * ball.radius:
                self.collision(self.cue_ball, ball)

        for i in range(len(self.balls) - 1):
            for ball in self.balls[(i+1):]:
                if np.sqrt((self.balls[i].x - ball.x)**2 + (self.balls[i].y - ball.y)**2) <= 2 * ball.radius:
                    self.collision(self.balls[i], ball)
        
    def collision(self, ball_1, ball_2):
        if ball_1.x_vel !=  0:
            theta_1 = np.arctan2(ball_1.y_vel, ball_1.x_vel)
        else:
            theta_1 = np.pi / 2
        
        if ball_2.x_vel !=  0:
            theta_2 = np.arctan2(ball_2.y_vel, ball_2.x_vel)
        else:
            theta_2 = np.pi / 2
        
        phi = np.arctan2(ball_2.y - ball_1.y, ball_2.x - ball_1.x)
        v_1 = np.sqrt(ball_1.x_vel**2 + ball_1.y_vel**2)
        v_2 = np.sqrt(ball_2.x_vel**2 + ball_2.y_vel**2)

        ball_1.x_vel = v_2 * np.cos(theta_2 - phi) * np.cos(phi) + v_1 * np.sin(theta_1 - phi) * np.cos(phi + np.pi / 2)
        ball_1.y_vel = v_2 * np.cos(theta_2 - phi) * np.sin(phi) + v_1 * np.sin(theta_1 - phi) * np.sin(phi + np.pi / 2)
        ball_2.x_vel = v_1 * np.cos(theta_1 - phi) * np.cos(phi) + v_2 * np.sin(theta_2 - phi) * np.cos(phi + np.pi / 2)
        ball_2.y_vel = v_1 * np.cos(theta_1 - phi) * np.sin(phi) + v_2 * np.sin(theta_2 - phi) * np.sin(phi + np.pi / 2)



if __name__ == "__main__":
    billiards = BilliardsGame()
    billiards.run_game()

# TODO: Add oof and related words when cue ball is sunk
# TODO: Hide and disable cue while balls are moving
# TODO: Refactor code