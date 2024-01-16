import pygame
from support_functions import *


class Bullet:
    def __init__(self, enemy, color, x_y, r, vx_vy, dm):
        self.enemy = enemy
        self.color = color
        self.x, self.y = x_y
        self.vx, self.vy = vx_vy
        self.r = r
        self.dm = dm
        self.direction = ""

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
            if self.direction == "left":
                self.x -= self.vx * dt()
            if self.direction == "right":
                self.x += self.vx * dt()
            if self.direction == "down":
                self.y += self.vy * dt()
            if self.direction == "up":
                self.y -= self.vy * dt()
