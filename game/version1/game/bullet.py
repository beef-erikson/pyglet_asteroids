"""
     Handles bullet logic.
"""
import pyglet
from . import physical_object, resources


class Bullet(physical_object.PhysicalObject):
    """ Bullets fired by player. """

    def __init__(self, *args, **kwargs):
        """ Initializations. """
        super().__init__(resources.bullet_image, *args, *kwargs)
        pyglet.clock.schedule_once(self.die, 0.5)  # Kills bullet after 0.5 seconds

    def die(self):
        """ Removes the bullet """
        self.dead = True
