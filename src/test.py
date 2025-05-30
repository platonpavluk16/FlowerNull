from grafics.draw import *
from physic.physic import apply_physics, enable_physics, _physics_objects
from collision.collision import enable_collision

x = 300
y = 300

createWin(1920, 1080, "Моя гра")
setBackgroundColor(66, 135, 245)

rr1 = createRectangle(x, y, 100, 100, color=(111, 111, 111))  # Гравець
r1 = createRectangle(100, 100, 800, 50, color=(186, 186, 186))  # Платформа

enable_collision(r1)
enable_physics(r1, solid=True)

enable_collision(rr1)
enable_physics(rr1)

def game_update(dt):
    global x

    player_body = next((b for b in _physics_objects if b.obj == rr1), None)

    if KeyClick(key.A):
        x -= 10
        update_position(rr1, x=x)

    if KeyClick(key.D):
        x += 10
        update_position(rr1, x=x)

    if KeyClick(key.SPACE) and player_body and player_body.on_ground:
        player_body.vy = 250

    apply_physics(dt)

setUpdate(game_update)
Run()
