from support_functions import *


class GameObject:
    def __init__(self, color, x_y, width_height, vx_vy, hp, dm, endurance):
        self.color = color
        self.x, self.y = x_y
        self.vx, self.vy = vx_vy
        self.width, self.height = width_height
        self.hp = hp
        self.dm = dm
        self.endurance = endurance
        self.direction = ""

    def move(self):
        if not_in_border(self.x, self.y, self.direction):
            if self.direction == "left":
                self.x -= self.vx * dt()
            if self.direction == "right":
                self.x += self.vx * dt()
            if self.direction == "down":
                self.y += self.vy * dt()
            if self.direction == "up":
                self.y -= self.vy * dt()

    def shoot(self, other):
        pass

    def get_damage(self, dm):
        self.hp -= dm * self.endurance

    def draw(self, screen):
        pass

    def collision(self, other):
        pass