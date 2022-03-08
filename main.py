import random
import pygame
import config as cfg
from canon import Canon
from point import Point

pygame.init()
sc = pygame.display.set_mode(cfg.RES)
clock = pygame.time.Clock()

canon = Canon(sc)

points = []

count = 0
font_score = pygame.font.SysFont('Arial', 26, bold=True)


def add_point():
    x = random.randrange(50, cfg.RES[0] - 200, 5)
    y = random.randrange(25, cfg.RES[1] - 25, 5)
    points.append(Point(sc, x, y))


for i in range(5):
    add_point()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONUP:
            canon.shoot()

    sc.fill(cfg.WHITE)

    [bullet.draw() for bullet in canon.bullets]
    [point.draw() for point in points]
    canon.draw()

    render_score = font_score.render(f'SCORE: {count}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    canon.update()
    [bullet.update() for bullet in canon.bullets]

    for bullet in canon.bullets:
        if bullet.y <= 0:
            canon.bullets.remove(bullet)
        elif bullet.x >= cfg.RES[0]:
            canon.bullets.remove(bullet)

    for point in points:
        if point.check_collision(canon.bullets):
            points.remove(point)
            add_point()
            count += 1

    pygame.display.flip()
    clock.tick(cfg.FPS)



