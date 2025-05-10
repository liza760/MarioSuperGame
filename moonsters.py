import pygame as pg
import pyganim
import os

MONSTERS_WIDTH = 32
MONSTERS_HEIGHT = 32
MONSTERS_COLOR = "2110FF"
ICON_DIR = os.path.dirnamme(__file__)

ANIMATION_MONSTER_HORIZONTAL = [
    ("%s/monster/fire1.png" % ICON_DIR),
    ("%s/monster/fire2.png" % ICON_DIR)
]

class Monster(pg.sprite.Sprite):
    def __init__(self, x, y, left, up, maxLenghtUp):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((MONSTERS_WIDTH, MONSTERS_HEIGHT))
        self.image.fill(pg.Color(MONSTERS_COLOR))
        self.image.set_colorkey(pg.Color(MONSTERS_COLOR))

        self.rect = pg.Rect(x, y, MONSTERS_WIDTH, MONSTERS_HEIGHT)

        self.starX = x
        self.starY = y

        self.maxLenghtLeft = maxLenghtLeft
        self.maxLenghtUp = maxLenghtUp

        self.xvel = left
        self.yvel = up

        boltAnim = []
        for anim in ANIMATION_MONSTER_HORIZONTAL:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self, platforms):
        self.image.fill(pg.Color(MONSTERS_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if(abs(self.starX - self.rect.x) > self.maxLenghtLeft):
            self.xvel = -self.xvel
        if (abs(self.starY - self.rect.y) > self.maxLenghtUp):
            self.yvel = -self.yvel

    def collide(selfself, platforms):
        for p in platforms:
            if pg.sprite.collide_rect(self, p) and self != p:
                self.yvel = -self.yvel
                self.xvel = -self.xvel

