""" Handles motion of objects """
import pyglet
from . import util


class PhysicalObject(pyglet.sprite.Sprite):
    """ Sprite object for movement, etc. """
    def __init__(self, *args, **kwargs):
        """ Initialization, including x/y velocities. """
        super().__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.dead = False

    # pylint: disable=arguments-differ
    def update(self, dt) -> None:
        """ Updates x and y position of object """
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.check_bounds()

    def check_bounds(self) -> None:
        """ Checks if object has left bounds. If so, wraps to other side."""
        # Set properties to check against.
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2

        # Check bounds and wrap if over.
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def collides_with(self, other_object) -> bool:
        """ Determines if a collision has occurred. """
        collision_distance = self.image.width/2 + other_object.width/2
        actual_distance = util.distance(self.position, other_object.position)

        return actual_distance <= collision_distance

    def handle_collision(self):
        """ On collision, set self to dead """
        self.dead = True
