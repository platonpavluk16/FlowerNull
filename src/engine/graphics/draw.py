import pyglet
from pyglet.shapes import Rectangle, Circle
from pyglet.window import key
from pyglet.sprite import Sprite
from pyglet.image import load as load_image
from pyglet.gl import glClearColor

_images = []
_batch = pyglet.graphics.Batch()
_window = None
_keys = key.KeyStateHandler()
user_update = None
_rectangles = []
_circles = []
_scale_percent = 100
_current_sprite = None

def createWin(width, height, title):
    global window
    window = pyglet.window.Window(width, height, title)
    window.push_handlers(_keys)

    @window.event
    def on_draw():
        window.clear()
        _batch.draw()

def createRectangle(x, y, width, height, color):
    rect = Rectangle(x, y, width, height, color=color, batch=_batch)
    _rectangles.append(rect)
    return rect
def createCircle(x, y, radius, color):
    circle = Circle(x, y, radius, color=color, batch=_batch)
    _circles.append(circle)
    return circle


def KeyClick(k):
    return _keys[k]

def setUpdate(func):
    global user_update
    user_update = func

def internal_update(dt):
    if user_update:
        user_update(dt)

def update_position(obj, x=None, y=None):
    if obj:
        if x is not None and hasattr(obj, 'x'):
            obj.x = x
        if y is not None and hasattr(obj, 'y'):
            obj.y = y

def createImage(path, x, y):
    global current_sprite
    image = pyglet.image.load(path)
    current_sprite = pyglet.sprite.Sprite(image, x=x, y=y, batch=_batch)
    return current_sprite

def setScale(percent):
    if current_sprite:
        current_sprite.scale = percent / 100.0

background_color = [0, 0, 0, 1]

def _setBackgroundColor(r, g, b, a=1):
    global background_color
    background_color = [r, g, b, a]
    glClearColor(r, g, b, a)

def setBackgroundColor(r, g, b, a=255):
    _setBackgroundColor(r/255, g/255, b/255, a/255)



def Run():
    pyglet.clock.schedule_interval(internal_update, 1/60)
    pyglet.app.run()
