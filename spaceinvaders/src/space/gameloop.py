import pygame


class Gameloop:
    def __init__(self, space_map, display):
        self._map = space_map
        self._clock = pygame.time.Clock()
        self._disp = display
        self._left = False
        self._right = False
        self._shottimer = 0
        self._invaderspeed = 1

    def start(self):
        while True:
            if self._events() is False:
                break
            if self._left:
                self._map.move_player(-5)
            if self._right:
                self._map.move_player(5)
            self._map.move_invaders(self._invaderspeed)
            if self._map.move_pellets(0, -3):
                self._invaderspeed += 0.1
            self._map.move_items(0, 4)
            self._shottimer -= 1

            self._render()

            self._clock.tick(60)

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._left = True
                if event.key == pygame.K_RIGHT:
                    self._right = True
                if event.key == pygame.K_UP:
                    if self._shottimer <= 0:
                        self._map.shoot_a_pellet(self._map.player.rect.x, 620)
                        self._shottimer = 30
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self._left = False
                if event.key == pygame.K_RIGHT:
                    self._right = False
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._disp.fill((0, 0, 0))
        self._map.allsprites.draw(self._disp)
        self._map.pellets.draw(self._disp)
        self._map.items.draw(self._disp)
        pygame.display.update()
