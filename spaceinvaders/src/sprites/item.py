import os
import pygame

dirname = os.path.dirname(__file__)


class Item(pygame.sprite.Sprite):
    """Class for Items

    """
    def __init__(self, pos_x=0, pos_y=0):
        """Class constructor, creates the entity. Contain information about x and y position.

        Args:
            pos_x (int, optional): Position horizontally. Defaults to 0.
            pos_y (int, optional): Position vertically. Defaults to 0.
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "item.png")
        )

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
