"""
    Used to load asteroids in random positions away from the player.
"""
import random
import math
import pyglet
from . import resources, physical_object


def asteroids(num_asteroids: int, player_position: tuple, batch=None) -> list:
    """ Creates asteroids away from the player and returns a list of their positions. """
    asteroid_list = []

    for _ in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position

        # If distance is within 100 pixels, respawn random position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)

        # Creates asteroids and sets a random rotation, velocity
        new_asteroid = physical_object.PhysicalObject(
            img=resources.asteroid_image, x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random()*40
        new_asteroid.velocity_y = random.random()*40

        asteroid_list.append(new_asteroid)

    return asteroid_list


def distance(point_1=(0, 0), point_2=(0, 0)) -> float:
    """ Returns the distance between two points """
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def player_lives(num_icons: int, batch=None) -> list:
    """ Returns a list of player lives to display. """
    lives_list = []

    # Adds icons to list equal to num_icons.
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=785-i*30, y=585, batch=batch)
        new_sprite.scale = 0.5
        new_sprite.rotation = 270
        lives_list.append(new_sprite)

    return lives_list
