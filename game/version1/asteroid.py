"""
    Main asteroid file used to launch the game. Contains main game loop.
"""
import pyglet
from game import resources, load

# Window setup
game_window = pyglet.window.Window(800, 600)

# Graphics batch
main_batch = pyglet.graphics.Batch()

# Load sprites
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, batch=main_batch)

# Text labels
score_label = pyglet.text.Label(text='Score: 0',
                                x=10, y=game_window.height - 20, batch=main_batch)
level_label = pyglet.text.Label(text='My Amazing Game', x=game_window.width//2,
                                y=game_window.height - 20, anchor_x='center', batch=main_batch)


@game_window.event
def on_draw():
    """ Draws everything to screen. """
    game_window.clear()

    # Draw assets
    main_batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
