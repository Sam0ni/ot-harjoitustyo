import os
import pygame

dirname = os.path.dirname(__file__)


class Pellet(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0, piercing=False):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "pellet.png")
        )

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.pierce = piercing