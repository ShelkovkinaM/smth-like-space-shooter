import pygame


class Level:
    def __init__(self, objects, shoot_v):
        self.objects = objects
        self.shown_objects = list()
        self.last_obj = 0
        self.shoot_v = shoot_v
        self.last_shoot = 0

    def draw(self):
        t = pygame.time.get_ticks()
        if t - self.last_shoot >= self.shoot_v and self.last_obj < len(self.objects):
            self.shown_objects.append(self.objects[self.last_obj])
            self.last_shoot = t
            self.last_obj += 1