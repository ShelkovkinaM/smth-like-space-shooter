import pygame
from GameObject import GameObject
from Bullet import Bullet


class Enemy(GameObject):
    def __init__(self, color, x_y, width_height, direction, vx_vy, shoot_v, hp, dm, endurance):
        super().__init__(color, x_y, width_height, vx_vy, hp, dm, endurance)
        self.direction = direction
        self.shoot_v = shoot_v
        self.last_shoot = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [(self.x, self.y), (self.x + (self.width // 2), self.y - self.height * 2),
                                                 (self.x - (self.width // 2), self.y - self.height * 2)])

    def shoot(self, bullets):
        t = pygame.time.get_ticks()
        if t - self.last_shoot >= self.shoot_v:
            b = Bullet(True, (225, 125, 3), (self.x, self.y), 10, (150, 150), self.dm)
            b.direction = "down"
            bullets.append(b)
            self.last_shoot = t

    def collision(self, other):
        if not other.enemy:
            e = pygame.Rect(other.x - other.r, other.y - other.r, 2 * other.r, 2 * other.r)
            s = pygame.Rect(self.x - (self.width // 2), self.y - self.height * 2, self.width, self.height)
            if e.colliderect(s):
                return True

