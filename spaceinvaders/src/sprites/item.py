import os
import pygame

dirname = os.path.dirname(__file__)


class Item(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player.png")
        )

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
