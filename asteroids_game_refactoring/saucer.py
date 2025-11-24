import math
import random
import pygame
from typing import TYPE_CHECKING
from game_object import GameObject

if TYPE_CHECKING:
    from game

from bullet import Bullet
from constants import SAUCER_SPEED, Display, Color
from sounds import snd_saucerB, snd_saucerS


class Saucer(GameObject):
    def __init__(self, game: Game):
        self.x = 0
        self.y = 0
        self.state = "Dead"
        self.type = "Large"
        self.dirchoice = ()
        self.bullets = []
        self.cd = 0
        self.bdir = 0
        self.soundDelay = 0
        self.game = game

    def update(self):
        self.x += SAUCER_SPEED * math.cos(self.dir * math.pi / 180)
        self.y += SAUCER_SPEED * math.sin(self.dir * math.pi / 180)

        if random.randrange(0, 100) == 1:
            self.dir = random.choice(self.dirchoice)

        if self.y < 0:
            self.y = Display.height
        elif self.y > Display.height:
            self.y = 0
        if self.x < 0 or self.x > Display.width:
            self.state = "Dead"

        if self.type == "Large":
            self.bdir = random.randint(0, 360)
        if self.cd == 0:
            self.bullets.append(
                Bullet(self.x, self.y, self.bdir, self.game.gameDisplay))
            self.cd = 30
        else:
            self.cd -= 1

        if self.type == "Large":
            pygame.mixer.Sound.play(snd_saucerB)
        else:
            pygame.mixer.Sound.play(snd_saucerS)

    def reset(self):
        self.state = "Alive"

        self.x = random.choice((0, Display.width))
        self.y = random.randint(0, Display.height)

        if random.randint(0, 1) == 0:
            self.type = "Large"
            self.size = 20
        else:
            self.type = "Small"
            self.size = 10

        if self.x == 0:
            self.dir = 0
            self.dirchoice = (0, 45, -45)
        else:
            self.dir = 180
            self.dirchoice = (180, 135, -135)

        self.cd = 0

    def draw(self):
        pygame.draw.polygon(
            self.game.gameDisplay, Color.white,
            ((self.x + self.size, self.y),
             (self.x + self.size / 2, self.y + self.size / 3),
             (self.x - self.size / 2, self.y + self.size / 3),
             (self.x - self.size, self.y),
             (self.x - self.size / 2, self.y - self.size / 3),
             (self.x + self.size / 2, self.y - self.size / 3)), 1)
        pygame.draw.line(
            self.game.gameDisplay, Color.white,
            (self.x - self.size, self.y),
            (self.x + self.size, self.y))
        pygame.draw.polygon(
            self.game.gameDisplay, Color.white,
            ((self.x - self.size / 2, self.y - self.size / 3),
             (self.x - self.size / 3, self.y - 2 * self.size / 3),
             (self.x + self.size / 3, self.y - 2 * self.size / 3),
             (self.x + self.size / 2, self.y - self.size / 3)), 1)
