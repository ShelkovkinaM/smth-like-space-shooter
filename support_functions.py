from constants import *


def dt():
    return 1 / FPS


def not_in_border(x, y, direction):
    if direction == "up" and y <= 0:
        return False
    elif direction == "down" and y >= HEIGHT:
        return False
    elif direction == "left" and x <= 0:
        return False
    elif direction == "right" and x >= WIDTH:
        return False
    else:
        return True