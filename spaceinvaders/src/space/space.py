import random
import pygame
from sprites.player import Player
from sprites.invader import Invader
from sprites.pellet import Pellet
from sprites.item import Item


class Space:
    def __init__(self, map_x, map_y):
        self.mapwidth = map_x
        self.mapheight = map_y
        self.player = None
        self.invaders = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.initsprites()
        self.invadersgoleft = True
        self.invadersgodown = False
        self.pierce = False

    def initsprites(self):
        # player
        self.player = Player(self.mapwidth/2, self.mapheight-100)

        # invaders
        localx = 100
        localy = 20
        row = 1
        for i in range(64):
            self.invaders.add(Invader(localx, localy))
            if localx + 100 > self.mapwidth:
                if row % 2 == 1:
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

    def move_player(self, direct_x=0, direct_y=0):
        if direct_x > 0:
            if self.player.rect.x + direct_x > self.mapwidth - self.player.width:
                pass
            else:
                self.player.rect.move_ip(direct_x, direct_y)
        else:
            if self.player.rect.x + direct_x < 0:
                pass
            else:
                self.player.rect.move_ip(direct_x, direct_y)

    def move_invaders(self, direct_x=0, direct_y=0):
        for i in self.invaders:
            if not self.invadersgoleft:
                if i.rect.x + 40 + direct_x > self.mapwidth:
                    self.invadersgodown = True
                    self.invadersgoleft = True
            else:
                if i.rect.x - direct_x < 0:
                    self.invadersgodown = True
                    self.invadersgoleft = False
        for i in self.invaders:
            if self.invadersgodown:
                i.rect.move_ip(0, 5)
            elif self.invadersgoleft:
                i.rect.move_ip(-direct_x, direct_y)
            elif not self.invadersgoleft:
                i.rect.move_ip(direct_x, direct_y)
        self.invadersgodown = False

    def shoot_a_pellet(self, playerx, playery=620):
        if self.pierce:
            self.pellets.add(Pellet(playerx, playery, True))
            self.pierce = False
        else:
            self.pellets.add(Pellet(playerx, playery))

    def move_pellets(self, horizontalspeed=0, verticalspeed=0):
        for i in self.pellets:
            i.rect.move_ip(horizontalspeed, verticalspeed)
            if i.rect.y < -50:
                i.kill()
            if i.pierce:
                pygame.sprite.spritecollide(i, self.invaders, True)
                return True
            else:
                if pygame.sprite.spritecollide(i, self.invaders, True):
                    if random.randint(1, 10) < 3:
                        self.items.add(Item(i.rect.x, i.rect.y))
                    i.kill()
                    return True

    def move_items(self, horizontalspeed=0, verticalspeed=0):
        for i in self.items:
            i.rect.move_ip(horizontalspeed, verticalspeed)
            if i.rect.y < -50:
                i.kill()
            if pygame.sprite.collide_rect(i, self.player):
                i.kill()
                self.pierce = True