import pygame
from sprites.player import Player
from sprites.invader import Invader

class Space:
    def __init__(self, x, y):
        self.mapwidth = x
        self.mapheight = y
        self.player = None
        self.invaders = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.initsprites()
        self.invadersgoleft = True
        self.invadersgodown = False

    def initsprites(self):
        #player
        self.player = Player(self.mapwidth/2, self.mapheight-100)
        
        #invaders
        localx = 100
        localy = 20
        row = 1
        for i in range(64):
            self.invaders.add(Invader(localx, localy))
            if localx + 100 > self.mapwidth:
                if row%2 == 1:
                    localx = 100
                else:
                    localx = 100
                localy += 60
                row += 1
            else:
                localx += 75

        self.allsprites.add(
            self.player,
            self.invaders
        )

    def move_player(self, dx=0, dy=0):
        if dx > 0:
            if self.player.rect.x + dx > self.mapwidth:
                return
            else:
                self.player.rect.move_ip(dx, dy)
        else:
            if self.player.rect.x + dx < 0:
                return
            else:
                self.player.rect.move_ip(dx, dy)



    def move_invaders(self, dx=0, dy=0):
        for i in self.invaders:
            if not self.invadersgoleft:
                if i.rect.x + 40 + dx > self.mapwidth:
                    self.invadersgodown = True
                    self.invadersgoleft = True
            else:
                if i.rect.x - dx < 0:
                    self.invadersgodown = True
                    self.invadersgoleft = False
        for i in self.invaders:
            if self.invadersgodown:
                i.rect.move_ip(0, 5)
            elif self.invadersgoleft:
                i.rect.move_ip(-dx, 0)
            elif not self.invadersgoleft:
                i.rect.move_ip(dx, 0)
        self.invadersgodown = False