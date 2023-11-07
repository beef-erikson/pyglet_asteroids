from game import resources
import pyglet

game_window = pyglet.window.Window(800, 600)

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

score_label = pyglet.text.Label(text='Score: 0', x=10, y=game_window.height - 20)
level_label = pyglet.text.Label(text='My Amazing Game', x=game_window.width//2,
                                y=game_window.height - 20, anchor_x='center')


@game_window.event
def on_draw():
    game_window.clear()

    # Draws labels
    level_label.draw()
    score_label.draw()

    # Draws player
    player_ship.draw()
    

if __name__ == '__main__':
    pyglet.app.run()
