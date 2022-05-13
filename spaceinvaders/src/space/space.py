import random
import pygame
from sprites.player import Player
from sprites.invader import Invader
from sprites.pellet import Pellet
from sprites.item import Item


class Space:
    """Class that compiles all assets used for the game
    """
    def __init__(self, map_x, map_y):
        """Class constructor which creates the game

        Args:
            map_x (integer): the width of the game area
            map_y (integer): the height of the game area 
        """
        self.mapwidth = map_x
        self.mapheight = map_y
        self.player = None
        self.invaders = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.invaderpellets = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.initsprites()
        self.invadersgoleft = True
        self.invadersgodown = False
        self.invaderspeed = 1
        self.pierce = False
        self.shottimer = 0
        self.victorious = False
        self.gameover = False
        self.score = 0
        self.time = 300

    def initsprites(self):
        """Initializes all the preliminary sprites for the game
        """
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
        """Moves the player

        Args:
            direct_x (int, optional): amount of pixels moved horizontally. Defaults to 0.
            direct_y (int, optional): amount of pixels moved vertically (not used). Defaults to 0.
        """
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
        """Moves the enemies

        Args:
            direct_x (int, optional): amount of pixels moved horizontally. Defaults to 0.
            direct_y (int, optional): amount of pixels moved vertically. Defaults to 0.
        """
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
            if random.randint(1, 1000) < 3:
                canshoot = True
                for j in self.invaders:
                    if i.rect.y + 60 == j.rect.y:
                        canshoot = False
                        break
                if canshoot:
                    self.invaderpellets.add(Pellet(i.rect.x, i.rect.y))
            if self.invadersgodown:
                i.rect.move_ip(0, 5)
                if i.rect.y > 600:
                    self.gameover = True
                    break
            elif self.invadersgoleft:
                i.rect.move_ip(-direct_x, direct_y)
            elif not self.invadersgoleft:
                i.rect.move_ip(direct_x, direct_y)
        self.invadersgodown = False

    def shoot_a_pellet(self, playerx, playery=620):
        """Adds a pellet

        Args:
            playerx (int): players position horizontally
            playery (int, optional): players position vertically. Defaults to 620.
        """
        if self.pierce:
            self.pellets.add(Pellet(playerx + (self.player.width/2), playery, True))
            self.pierce = False
        else:
            self.pellets.add(Pellet(playerx + (self.player.width/2), playery))

    def move_pellets(self, horizontalspeed=0, verticalspeed=0):
        """Moves pellets if there are any

        Args:
            horizontalspeed (int, optional): amount of pixels moved horizontally. Defaults to 0.
            verticalspeed (int, optional): amount of pixels moved vertically. Defaults to 0.

        Returns:
            True: if an enemy is killed
        """
        for i in self.pellets:
            i.rect.move_ip(horizontalspeed, verticalspeed)
            if i.rect.y < -50:
                i.kill()
            if i.pierce:
                if pygame.sprite.spritecollide(i, self.invaders, True):
                    self.score += 10
                    return True
            else:
                if pygame.sprite.spritecollide(i, self.invaders, True):
                    if random.randint(1, 10) < 3:
                        self.items.add(Item(i.rect.x, i.rect.y))
                    self.score += 10
                    i.kill()
                    return True

    def move_invader_pellets(self, horizontalspeed=0, verticalspeed=0):
        """Moves invaders pellets if there are any

        Args:
            horizontalspeed (int, optional): amount of pixels moved horizontally. Defaults to 0.
            verticalspeed (int, optional): amount of pixels moved vertically. Defaults to 0.
        """
        for i in self.invaderpellets:
            i.rect.move_ip(horizontalspeed, verticalspeed)
            if i.rect.y > 730:
                i.kill()
            else:
                if pygame.sprite.collide_rect(i, self.player):
                    self.player.health -= 1
                    if self.player.health == 0:
                        self.gameover = True
                    i.kill()

    def move_items(self, horizontalspeed=0, verticalspeed=0):
        """Moves items if there are any

        Args:
            horizontalspeed (int, optional): amount of pixels moved horizontally. Defaults to 0.
            verticalspeed (int, optional): amount of pixels moved vertically. Defaults to 0.
        """
        for i in self.items:
            i.rect.move_ip(horizontalspeed, verticalspeed)
            if i.rect.y < -50:
                i.kill()
            if pygame.sprite.collide_rect(i, self.player):
                i.kill()
                self.pierce = True
