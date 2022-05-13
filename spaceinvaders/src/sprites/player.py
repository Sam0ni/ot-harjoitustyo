import os
import pygame

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    """Class for player character

    """
    def __init__(self, pos_x=0, pos_y=0):
        """Class constructor, creates the entity. Contains information for x and y position, width and health.

        Args:
            pos_x (int, optional): Position horizontally. Defaults to 0.
            pos_y (int, optional): Position vertically. Defaults to 0.
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player.png")
        )
        self.width = self.image.get_width()

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.health = 3
