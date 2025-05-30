from collision import check_collisions

_physics_objects = []

GRAVITY = -500

class PhysicsBody:
    def __init__(self, obj, solid=False):
        self.obj = obj
        self.vy = 0
        self.solid = solid
        self.on_ground = False
        _physics_objects.append(self)

def apply_physics(dt):
    for body in _physics_objects:
        if body.solid:
            continue

        body.vy += GRAVITY * dt
        old_y = body.obj.y
        body.obj.y += body.vy * dt

        collisions = check_collisions(body.obj)
        body.on_ground = False
        for other in collisions:
            body.obj.y = old_y
            body.vy = 0
            body.on_ground = True 
            break

def enable_physics(obj, solid=False):
    return PhysicsBody(obj, solid)

def set_gravity(value):
    global GRAVITY
    GRAVITY = value
