import pyglet
import random
import math
from . import resources


def asteroids(num_asteroids: int) -> list:
    asteroid_list = []
    for x in range(num_asteroids):
        asteroid_x = random.randint(0, 800)
        asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)
        asteroid_list.append(new_asteroid)

    return asteroid_list


def distance(point_1=(0, 0), point_2=(0, 0)):
    """ Returns the distance between two points """
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)
