""" 
컨트롤러, Esc 핸들러,한글 적용된 Text 클래스 등 기본적인 도구
"""
from ursina import *


class Eye(Entity):
    """
    공간을 둘러보기 위한 컨트롤러. player라고 봐도 무방하다.
    limit 인자로 공간 크기 단위값을 주면 그 안에 가둔다.
    """

    def __init__(self, *, speed=4, fav=90, limit=None, **kwargs):
        super().__init__(**kwargs)
        self.limit = limit
        self.origin_speed = self.speed = speed
        self.sensitivity = 80
        camera.rotation = (0, 0, 0)
        camera.position = (0, 0, 0)
        camera.parent = self
        camera.fov = fav
        mouse.locked = True
        self.fast_speed = self.speed * 6
        self.fixed_positions = {  # x,y,z :position , rotation
            "origin": (Vec3(4.8953, 4.06675, -3.83887), Vec3(-318.219, -1852.87, 0)),
            "center": (Vec3(0, 0, 0), Vec3(0, 0, 0)),
            "center-top": (Vec3(4.15159, 9.707, -0.0154717), Vec3(70.0086, -1169.88, 0)),
            "center-bottom-center": (Vec3(8.85013, 1.31621, 0.0560277), Vec3(3.73638, -1889.11, 0)),
            "left-bottom-default": (Vec3(6.1342, 5.44779, -5.43013), Vec3(-678.071, -5447.75, 0)),
            "right-bottom-default": (Vec3(5.75278, 5.4826, 5.44936), Vec3(-317, -2652.83, 0)),
            "left-top-default": (Vec3(-5.79788, 5.54591, -5.0487), Vec3(-677.139, -5712.55, 0)),
            "right-top-default": (Vec3(-5.24484, 5.41471, 6.26402), Vec3(-677.55, -5621.68, 0)),
        }
        self.position, self.rotation = self.fixed_positions["origin"]
        self.update = self.controller

    def controller(self):
        self.y += held_keys["space"] * time.dt * self.speed
        self.y -= held_keys["alt"] * time.dt * self.speed
        self.rotation_y += mouse.velocity[0] * self.sensitivity
        self.rotation_x -= mouse.velocity[1] * self.sensitivity
        self.direction = Vec3(
            self.forward * (held_keys["w"] - held_keys["s"]) + self.right * (held_keys["d"] - held_keys["a"])
        ).normalized()
        self.position += self.direction * self.speed * time.dt
        if self.limit:
            self.x = clamp(self.x, -self.limit / 2 + 2, self.limit / 2 - 2)
            self.y = clamp(self.y, -self.limit / 2 + 2, self.limit / 2 - 2)
            self.z = clamp(self.z, -self.limit / 2 + 2, self.limit / 2 - 2)

    def input(self, key):
        if key == "left mouse down":
            self.speed = self.fast_speed
        if key == "left mouse up":
            self.speed = self.origin_speed
        # if key == "p":
        # 위치,각도 캡쳐용
        # print(f"position={self.position}\nrotation={self.rotation}")
        if key == "backspace":
            self.position, self.rotation = self.fixed_positions["origin"]
        if key == "0":
            self.position, self.rotation = self.fixed_positions["center"]
        if key == "1":
            self.position, self.rotation = self.fixed_positions["center-top"]
        if key == "2":
            self.position, self.rotation = self.fixed_positions["center-bottom-center"]
        if key == "3":
            self.position, self.rotation = self.fixed_positions["left-bottom-default"]
        if key == "4":
            self.position, self.rotation = self.fixed_positions["right-bottom-default"]
        if key == "5":
            self.position, self.rotation = self.fixed_positions["right-top-default"]
        if key == "6":
            self.position, self.rotation = self.fixed_positions["left-top-default"]
