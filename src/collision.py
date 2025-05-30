_collidable_objects = []

def enable_collision(obj):
    _collidable_objects.append(obj)

def get_bounds(obj):
    if hasattr(obj, 'width') and hasattr(obj, 'height'):
        return obj.x, obj.y, obj.x + obj.width, obj.y + obj.height
    elif hasattr(obj, 'radius'):
        return obj.x - obj.radius, obj.y - obj.radius, obj.x + obj.radius, obj.y + obj.radius
    else:
        raise ValueError("Unknown object type")

def check_collision(obj1, obj2):
    x1_min, y1_min, x1_max, y1_max = get_bounds(obj1)
    x2_min, y2_min, x2_max, y2_max = get_bounds(obj2)

    return (
        x1_min < x2_max and x1_max > x2_min and
        y1_min < y2_max and y1_max > y2_min
    )

def check_collisions(obj):
    collisions = []
    for other in _collidable_objects:
        if other is not obj and check_collision(obj, other):
            collisions.append(other)
    return collisions
