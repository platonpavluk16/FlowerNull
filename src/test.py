from engine.graphics.draw import *
from engine.physic.collision import *
from engine.physic.physic import *

x = 10


def game_update(dt):
    global x 
    if KeyClick(key.A):
        x -= 10
        print("нажато")
        update_position(player, x=x)

    if KeyClick(key.D):
        x += 10
        print("нажато")
        update_position(player, x=x)

createWin(1920, 1080, "Моя гра")
setBackgroundColor(66, 135, 245)
player = createImage("smile.png", 100, 100)
setScale(20)

setUpdate(game_update)
Run()
