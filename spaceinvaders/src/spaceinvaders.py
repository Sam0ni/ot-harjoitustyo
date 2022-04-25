import pygame
from space.space import Space
from space.gameloop import Gameloop
from menu.menuloop import Menuloop
from menu.menu import Menu
from database_connection import get_database_connection
from scores.scores import Scores


def main():
    displaywidth = 1280
    displayheight = 720

    disp = pygame.display.set_mode((displaywidth, displayheight))
    pygame.display.set_caption("Space Invaders")

    space_map = Space(displaywidth, displayheight)
    menu = Menu(displaywidth, displayheight)
    score = Scores(get_database_connection())

    pygame.init()
    menuloop = Menuloop(disp, menu)
    loop = Gameloop(space_map, disp)
    if menuloop.start():
        if loop.start():
            pass
    else:
        pass


if __name__ == "__main__":
    main()
