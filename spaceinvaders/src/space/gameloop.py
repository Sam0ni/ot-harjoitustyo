import pygame

class Gameloop:
    def __init__(self, map, display):
        self._map = map
        self._clock = pygame.time.Clock()
        self._disp = display
        self._left = False
        self._right = False

    def start(self):
        while True:
            if self._events() == False:
                break
            if self._left:
                self._map.move_player(-5)
            if self._right:
                self._map.move_player(5)
            self._map.move_invaders(2)

            self._render()

            self._clock.tick(60)

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._left = True
                if event.key == pygame.K_RIGHT:
                    self._right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self._left = False
                if event.key == pygame.K_RIGHT:
                    self._right = False
    
    def _render(self):
        self._disp.fill((0,0,0))
        self._map.allsprites.draw(self._disp)
        pygame.display.update()