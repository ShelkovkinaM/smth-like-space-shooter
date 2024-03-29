import pygame
from GameObject import GameObject
from Bullet import Bullet


class Player(GameObject):
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def shoot(self, bullets):
        b = Bullet(False, (125, 125, 3), (self.x + (self.width // 2), self.y + (self.height // 2)), 10, (150, 150), self.dm)
        b.direction = "up"
        bullets.append(b)

    def collision(self, other):
        if other.enemy:
            e = pygame.Rect(other.x - other.r, other.y - other.r, 2 * other.r, 2 * other.r)
            s = pygame.Rect(self.x, self.y, self.width, self.height)
            if e.colliderect(s):
                return True
