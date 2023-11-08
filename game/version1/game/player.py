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
        self.keys = {'left': False, 'right': False, 'up': False}

    def on_key_press(self, symbol, _):
        """ Key has been pressed, sets flag True if movement control. """
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, _):
        """ Key has been released, sets flag False if movement control. """
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False

    def update(self, dt):
        """ Updates player position """
        super().update(dt)

        # Rotation
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        if self.keys['right']:
            self.rotation += self.rotate_speed * dt

        # Thrust forward
        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
