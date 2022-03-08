import math


def get_collider_from_circle(x, y, r):
    a = math.sqrt(2*r**2)
    nx = x - a/2
    ny = y + a/2
    return nx, ny, a
