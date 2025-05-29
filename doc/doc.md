🚀 Getting Started
Basic example:

from draw import *

def update(dt):
    if get_key_state(key.RIGHT):
        print("Right key is held")

create_window(800, 600, "My Game")
create_rectangle(100, 100, 200, 100, color=(255, 0, 0))
create_circle(400, 300, 50, color=(0, 255, 0))
create_image("hero.png", 100, 100)
set_scale(150)  # scale last image to 150%
set_update(update)
run()

📘 API Reference
create_window(width, height, title)

Creates the game window.

    width: int — window width in pixels

    height: int — window height in pixels

    title: str — title displayed in the window bar

create_rectangle(x, y, width, height, color=(255, 255, 255))

Draws a rectangle on screen.

    x, y: int — bottom-left corner position

    width, height: int — dimensions

    color: tuple(int, int, int) — RGB color (0-255)

create_circle(x, y, radius, color=(255, 255, 255))

Draws a circle on screen.

    x, y: int — center position

    radius: int — size of the circle

    color: tuple(int, int, int) — RGB

create_image(path, x, y)

Loads and displays an image as a sprite.

    path: str — path to the image file (e.g. "player.png")

    x, y: int — position

set_scale(percent)

Scales the most recently created sprite.

    percent: int or float — e.g. 150 means 150% size

get_key_state(key_code)

Returns True if a key is held down.

    key_code: use pyglet.window.key (e.g. key.LEFT, key.SPACE)

set_update(callback, interval=1/60)

Sets a function to be called every frame (default 60 FPS).

    callback: function — your update logic

    interval: float — seconds between calls (default: 1/60)

run()

Starts the Pyglet app and game loop.
🔒 Internal / Private Variables

All internal variables like _window, _batch, _current_sprite are hidden from the user API by convention. Please use the public functions provided above