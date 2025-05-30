import pyglet
from pyglet.shapes import Rectangle, Circle
from pyglet.window import key
from pyglet.sprite import Sprite
from pyglet.gl import glClearColor

_batch = pyglet.graphics.Batch()
_window = None
_keys = key.KeyStateHandler()
user_update = None
_current_scene = None
_current_sprite = None


def createWin(width, height, title):
    global _window
    _window = pyglet.window.Window(width, height, title)
    _window.push_handlers(_keys)

    @_window.event
    def on_draw():
        _window.clear()
        if _current_scene:
            _current_scene.draw()
        else:
            _batch.draw()

def setUpdate(func):
    global user_update
    user_update = func

def internal_update(dt):
    if user_update:
        user_update(dt)
    if _current_scene:
        _current_scene.update(dt)


def createRectangle(x, y, width, height, color):
    if _current_scene:
        rect = Rectangle(x, y, width, height, color=color, batch=_current_scene.batch)
        _current_scene.objects.append(rect)
    else:
        rect = Rectangle(x, y, width, height, color=color, batch=_batch)
    return rect

def createCircle(x, y, radius, color):
    if _current_scene:
        circle = Circle(x, y, radius, color=color, batch=_current_scene.batch)
        _current_scene.objects.append(circle)
    else:
        circle = Circle(x, y, radius, color=color, batch=_batch)
    return circle

def update_position(obj, x=None, y=None):
    if obj:
        if x is not None and hasattr(obj, 'x'):
            obj.x = x
        if y is not None and hasattr(obj, 'y'):
            obj.y = y

def createImage(path, x, y):
    global _current_sprite
    image = pyglet.image.load(path)
    _current_sprite = Sprite(image, x=x, y=y, batch=_batch)
    return _current_sprite

def setScale(percent):
    if _current_sprite:
        _current_sprite.scale = percent / 100.0


def KeyClick(k):
    return _keys[k]


def setBackgroundColor(r, g, b, a=255):
    glClearColor(r/255, g/255, b/255, a/255)


def Run():
    pyglet.clock.schedule_interval(internal_update, 1/60)
    pyglet.app.run()

