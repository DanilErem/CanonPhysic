import random
import pygame
import config as cfg
from utility import get_collider_from_circle


class Point:
    def __init__(self, sc, x, y):
        self.sc = sc
        self.x = x
        self.y = y
        self.size = random.randrange(10, 30, 5)
        self.collider = get_collider_from_circle(self.x, self.y, self.size)

    def check_collision(self, bullets):
        px, py, pa = self.collider
        for bullet in bullets:
            bx, by, ba = bullet.collider
            if px <= bx and py <= by:
                if px+pa >= bx and py+pa >= by-pa:
                    bullets.remove(bullet)
                    return True
            elif px <= bx and py >= by:
                if px+pa >= bx and py-pa <= by:
                    bullets.remove(bullet)
                    return True
            elif px >= bx and py <= by:
                if px-pa <= bx and py+pa >= by-pa:
                    bullets.remove(bullet)
                    return True
            elif px >= bx and py >= by:
                if px-pa <= bx and py-pa <= by:
                    bullets.remove(bullet)
                    return True
        return False

    def draw_collider(self):
        x, y, a = self.collider
        pygame.draw.rect(self.sc, cfg.GREEN, (x, cfg.RES[1] - y, a, a), 1)

    def draw(self):
        pygame.draw.circle(self.sc, cfg.BLUE, (self.x, cfg.RES[1] - self.y), self.size)