import math
import pygame
from constants import BULLET_SPEED, Display, Color


class Bullet(GameObject):

    def __init__(self, x: int, y: int,
                 direction: float, surface: pygame.Surface):
        self.x = x
        self.y = y
        self.dir = direction
        self.live_frames_left = 30
        self.surface = surface

    def updateBullet(self):
        self.x += BULLET_SPEED * math.cos(self.dir * math.pi / 180)
        self.y += BULLET_SPEED * math.sin(self.dir * math.pi / 180)

        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height
        self.live_frames_left -= 1

        def draw(self):
            pygame.draw.circle(
                self.surface, Color.white,
                (int(self.x), int(self.y)), 3)