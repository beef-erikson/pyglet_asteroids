"""
    Main asteroid file used to launch the game. Contains main game loop.
"""
import pyglet
from game import load, player

# Window setup
game_window = pyglet.window.Window(800, 600)

# Graphics batch
main_batch = pyglet.graphics.Batch()

# Text labels
score_label = pyglet.text.Label(text='Score: 0',
                                x=10, y=game_window.height - 20, batch=main_batch)
level_label = pyglet.text.Label(text='My Amazing Game', x=game_window.width//2,
                                y=game_window.height - 20, anchor_x='center', batch=main_batch)

# Load sprites
player_ship = player.Player(x=400, y=300, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, batch=main_batch)
player_lives = load.player_lives(3, main_batch)

# Grab all objects into a list
game_objects = [player_ship] + asteroids

# Tell the window the player object responds to events.
game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
    """ Draws everything to screen. """
    game_window.clear()

    # Draw assets
    main_batch.draw()


def update(dt):
    """ Updates the position of the game objects and handles collisions. """
    # Collision checking
    # pylint: disable=consider-using-enumerate
    for i in range(len(game_objects)):
        for j in range(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision()
                    obj_2.handle_collision()

    # Update positions of game_objects and adds any new objects.
    to_add = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    # Removes dead objects.
    for to_remove in [obj for obj in game_objects if obj.dead]:
        # If dying object spawned new objects, add those to list
        to_add.extend(obj.new_objects)
        to_remove.delete()
        game_objects.remove(to_remove)

    # Adds back into game objects.
    game_objects.extend(to_add)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
