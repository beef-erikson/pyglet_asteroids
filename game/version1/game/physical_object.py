""" Handles motion of objects """
import pyglet


class PhysicalObject(pyglet.sprite.Sprite):
    """ Sprite object for movement, etc. """
    def __init__(self, *args, **kwargs):
        """ Initialization, including x/y velocities. """
        super().__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0

    def update(self, dt, _):
        """ Updates x and y position of object """
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.check_bounds()

    def check_bounds(self):
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
