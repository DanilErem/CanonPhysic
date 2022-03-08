import pygame
import config as cfg
import math
from utility import get_collider_from_circle


class Bullet:
    def __init__(self, sc, x, y, speed, alpha):
        self.sc = sc
        self.start_x = x
        self.start_y = y
        self.x = 0
        self.y = 0
        self.time = 0
        self.speed = speed
        self.alpha = alpha/180 * math.pi
        self.size = cfg.BULLET_SIZE
        self.x_p = math.cos(self.alpha) * self.speed
        self.y_p = math.sin(self.alpha) * self.speed
        self.collider = get_collider_from_circle(self.x, self.y, self.size)

    def draw_collider(self):
        x, y, a = self.collider
        pygame.draw.rect(self.sc, cfg.GREEN, (x, cfg.RES[1] - y, a, a), 1)

    def update(self):
        self.x = self.x_p * self.time + self.start_x
        self.y = self.start_y - (cfg.G * self.time ** 2) / 2 + (self.y_p * self.time)
        self.collider = get_collider_from_circle(self.x, self.y, self.size)

        self.time += cfg.BULLET_TIME

    def get_pos(self):
        return self.x, self.y

    def draw(self):
        pygame.draw.circle(self.sc, cfg.RED, (self.x, cfg.RES[1] - self.y), self.size)

