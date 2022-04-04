import pygame
from space.space import Space
from space.gameloop import Gameloop

def main():
    displaywidth = 1280
    displayheight = 720

    disp = pygame.display.set_mode((displaywidth, displayheight))
    pygame.display.set_caption("Space Invaders")

    map = Space(displaywidth, displayheight)

    pygame.init()

    loop = Gameloop(map, disp)
    loop.start()

if __name__ == "__main__":
    main()