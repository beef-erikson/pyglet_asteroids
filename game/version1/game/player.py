"""
    Player class - handles controls, thrust and so on.
"""
import math

import pyglet.sprite
from pyglet.window import key
from . import physical_object, resources


class Player(physical_object.PhysicalObject):
    """ Player class that responds to input. """
    def __init__(self, *args, **kwargs):
        """ Initializes thrust, rotate speed, key handler, and engine sprite. """
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.key_handler = key.KeyStateHandler()
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False  # We'll be setting this to true when firing the engine.

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
            # Thrust calculations
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

            # Engine sprite handling
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False

    def delete(self):
        """ Cleans up resources and player death. """
        self.engine_sprite.delete()
        super().delete()
