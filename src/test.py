from draw import *
from physic import apply_physics, enable_physics, _physics_objects
from collision import enable_collision
from scene_manager import SceneManager
from pyglet import *

x = 300
y = 300

createWin(1920, 1080, "Моя гра")
setBackgroundColor(66, 135, 245)

rr1 = createRectangle(x, y, 100, 100, color=(111, 111, 111))
r1 = createRectangle(100, 100, 800, 50, color=(186, 186, 186))
spike = createRectangle(500, 150, 50, 100, color=(180, 180, 180))
scene_manager = SceneManager()



enable_collision(r1)
enable_physics(r1, solid=True)

enable_collision(rr1)
enable_physics(rr1)

class GameScene:
    def __init__(self):
        self.x = x
        setBackgroundColor(103, 161, 118)

    def update(self, dt):
        setBackgroundColor(103, 161, 118)

        if KeyClick(key.A):
            self.x -= 10
            update_position(rr1, x=self.x)

        if KeyClick(key.D):
            self.x += 10
            update_position(rr1, x=self.x)

        player_body = next((b for b in _physics_objects if b.obj == rr1), None)

        if KeyClick(key.SPACE) and player_body and player_body.on_ground:
            player_body.vy = 450

        if is_touching(rr1, spike):
            scene_manager.change_scene("menu")
            del_obj(rr1)
            del_obj(r1)
            del_obj(spike)



        apply_physics(dt)


class MenuScene:
    def update(self, dt):
        setBackgroundColor(3, 43, 14)
        textDraw("YOU DIED", "Arial", 24, 1000, 1000, anchor_x="center", anchor_y="center")



scene_manager = SceneManager()
scene_manager.add_scene("game", GameScene())
scene_manager.add_scene("menu", MenuScene())
scene_manager.set_start_scene("game")


def game_update(dt):
    scene_manager.update(dt)
    if KeyClick(key.Q):
        scene_manager.change_scene("menu")
        del_obj(rr1)
        del_obj(r1)
        



setUpdate(game_update)
Run()
