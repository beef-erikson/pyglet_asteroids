"""
    Used to load asteroids in random positions away from the player.
"""
import pyglet
import random
import math
from . import resources


def asteroids(num_asteroids: int, player_position: tuple) -> list:
    """ Creates asteroids away from the player and returns a list of their positions. """
    asteroid_list = []

    for x in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position

        # If distance is within 100 pixels, respawn random position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)

        # Creates asteroids and sets a random rotation
        new_asteroid = pyglet.sprite.Sprite(
            img=resources.asteroid_image, x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)

        asteroid_list.append(new_asteroid)

    return asteroid_list


def distance(point_1=(0, 0), point_2=(0, 0)) -> float:
    """ Returns the distance between two points """
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)
