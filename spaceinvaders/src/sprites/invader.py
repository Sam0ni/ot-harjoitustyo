import os
import pygame

dirname = os.path.dirname(__file__)


class Invader(pygame.sprite.Sprite):
    """Class for Invaders

    """
    def __init__(self, pos_x=0, pos_y=0):
        """Class constructor, creates the entity. Contains information about x and y position.

        Args:
            pos_x (int, optional): Position horizontally. Defaults to 0.
            pos_y (int, optional): Position vertically. Defaults to 0.
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "invader.png")
        )

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
