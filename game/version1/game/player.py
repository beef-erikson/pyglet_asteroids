"""
    Player class - handles controls, thrust and so on.
"""
import math
import pyglet.sprite
from pyglet.window import key
from . import physical_object, resources, bullet


class Player(physical_object.PhysicalObject):
    """ Player class that responds to input. """
    def __init__(self, *args, **kwargs):
        """ Initializes thrust, rotate speed, key handler, and engine sprite. """
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.key_handler = key.KeyStateHandler()
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False
        self.bullet_speed = 700.0

    def update(self, dt):
        """ Updates player position, thrust sprite """
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

        # Fire bullets.
        if self.key_handler[key.SPACE]:
            self.fire()

    def fire(self):
        """ Fires the bullet from the front of the ship. """
        angle_radians = -math.radians(self.rotation)

        # Bullet position and spawning.
        ship_radius = self.image.width / 2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)

        # Bullet velocity.
        bullet_vx = self.velocity_x + math.cos(angle_radians) * self.bullet_speed
        bullet_vy = self.velocity_y * math.cos(angle_radians) * self.bullet_speed

        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy

        # Add bullet to list for spawning in main loop.
        self.new_objects.append(new_bullet)

    def delete(self):
        """ Cleans up resources and player death. """
        self.engine_sprite.delete()
        super().delete()
