"""
    Player class - handles controls, thrust and so on.
"""
import math
from pyglet.window import key
from . import physical_object, resources


class Player(physical_object.PhysicalObject):
    """ Player class that responds to input. """
    def __init__(self, *args, **kwargs):
        """ Initializes thrust, rotate speed, and key state. """
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        """ Updates player position """
        super().update(dt)

        # Rotation
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        # Thrust forward
        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
