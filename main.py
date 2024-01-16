import pygame
from constants import *
from support_functions import *
from Enemy import Enemy
from Player import Player

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
BULLETS = []
ENEMIES = [Enemy((255, 0, 0), (100, 0), (50, 25), "down", (30, 30), 1500, 30, 50, 0.1),
           Enemy((255, 0, 0), (200, 100), (50, 25), "down", (30, 30), 1500, 30, 50, 0.1)]
PLAYER = Player((0, 125, 255), (100, 460), (50, 30), (250, 250), 300, 100, 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                PLAYER.direction = "right"
            if event.key == pygame.K_LEFT:
                PLAYER.direction = "left"
            if event.key == pygame.K_UP:
                PLAYER.direction = "up"
            if event.key == pygame.K_DOWN:
                PLAYER.direction = "down"
            if event.key == pygame.K_SPACE:
                PLAYER.shoot(BULLETS)
        if event.type == pygame.KEYUP:
            PLAYER.direction = ""

    SCREEN.fill((0, 0, 0))
    PLAYER.move()
    PLAYER.draw(SCREEN)
    dell = list()
    for enemy in ENEMIES:
        enemy.shoot(BULLETS)
        enemy.move()
        enemy.draw(SCREEN)
        if not not_in_border(enemy.x, enemy.y, "down"):
            dell.append(enemy)
    for i in dell:
        ENEMIES.pop(ENEMIES.index(i))
    dell.clear()
    for bullet in BULLETS:
        if PLAYER.collision(bullet):
            PLAYER.get_damage(bullet.dm)
            dell.append(bullet)
        for enemy in ENEMIES:
            if enemy.collision(bullet):
                enemy.get_damage(bullet.dm)
                dell.append(bullet)
                if enemy.hp <=0:
                    ENEMIES.pop(ENEMIES.index(enemy))
        bullet.move()
        bullet.draw(SCREEN)
        if not not_in_border(bullet.x, bullet.y, "down") or not not_in_border(bullet.x, bullet.y, "up"):
            dell.append(bullet)
    for i in dell:
        BULLETS.pop(BULLETS.index(i))
    pygame.display.flip()
    CLOCK.tick(FPS)
    if PLAYER.hp <= 0:
        quit()