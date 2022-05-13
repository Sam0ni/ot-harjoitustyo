import os
import pygame

dirname = os.path.dirname(__file__)


class Pellet(pygame.sprite.Sprite):
    """Class for Pellets

    """
    def __init__(self, pos_x=0, pos_y=0, piercing=False):
        """Class constructor, creates the entity. Contains information about x and y position and whether or not the pellet is piercing

        Args:
            pos_x (int, optional): Position horizontally. Defaults to 0.
            pos_y (int, optional): Position vertically. Defaults to 0.
            piercing (bool, optional): Whether or not the pellet is piercing. Defaults to False.
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "pellet.png")
        )

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.pierce = piercing
