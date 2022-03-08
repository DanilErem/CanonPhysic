import math
import pygame
import config as cfg
from bullet import Bullet


class Canon:
    def __init__(self, sc: pygame.Surface):
        self.sc = sc
        self.x = 10
        self.y = 10
        self.rotation = 45
        self.power = cfg.CANON_POWER
        self.size = cfg.CANON_SIZE
        self.color = cfg.GREEN
        self.surface = pygame.Surface((self.size[0], self.size[1]))
        self.surface.set_colorkey(cfg.WHITE)
        self.surface.fill(cfg.BLACK)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x, cfg.RES[1]-self.y)
        self.wait_counter = 0
        self.bullets = []

    def shoot(self):
        bullet = Bullet(self.sc, self.x, self.y, self.power, self.rotation)
        self.bullets.append(bullet)

    def update(self):
        mx, my = pygame.mouse.get_pos()
        tan = (cfg.RES[1]-my)/(mx+1)

        self.rotation = math.atan(tan)/math.pi * 180

        if self.rotation > 90:
            self.rotation = 90
        if self.rotation < 0:
            self.rotation = 0

    def draw(self):
        old_center = self.rect.center
        render_surface = pygame.transform.rotate(self.surface, self.rotation)
        self.rect = render_surface.get_rect()
        self.rect.center = old_center

        self.sc.blit(render_surface, self.rect)
        pygame.draw.circle(self.sc, self.color, (self.x, cfg.RES[1] - self.y), self.size[2])

