from draw import *

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None
        self.current_scene_name = None
        self.managed_objects = [] 

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_start_scene(self, name):
        if name not in self.scenes:
            raise ValueError(f"Scene '{name}' not found")
        self.current_scene = self.scenes[name]
        self.current_scene_name = name
        if hasattr(self.current_scene, 'on_enter'):
            self.current_scene.on_enter()

    def change_scene(self, name):
        if name not in self.scenes:
            raise ValueError(f"Scene '{name}' not found")
        if self.current_scene and hasattr(self.current_scene, 'on_exit'):
            self.current_scene.on_exit()
        self.current_scene = self.scenes[name]
        self.current_scene_name = name
        if hasattr(self.current_scene, 'on_enter'):
            self.current_scene.on_enter()

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)

    def register_object(self, obj):
        if obj not in self.managed_objects:
            self.managed_objects.append(obj)

