import pygame


class Menuloop:
    def __init__(self, display, menu):
        pygame.font.init()
        self._clock = pygame.time.Clock()
        self._disp = display
        self._menu = menu
        self._scores = ""
        self._showhighscores = False
        self._startgame = False
        self._quitgame = False

    def start(self):
        while True:
            if self._startgame:
                return True
            if self._quitgame:
                return False
            if self._events() is False:
                break
            if not self._showhighscores:
                self._render()
            else:
                self._renderhighscores()
            self._clock.tick(60)

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self._menu.move_cursor_down()
                if event.key == pygame.K_UP:
                    self._menu.move_cursor_up()
                if event.key == pygame.K_SPACE:
                    if self._menu.go_there() == "highscores":
                        self._scores = self._menu.inithighscores()
                        self._showhighscores = True
                    elif self._menu.go_there():
                        self._startgame = True
                    else:
                        self._quitgame = True
                if event.key == pygame.K_ESCAPE:
                    self._showhighscores = False
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._disp.fill((0, 0, 0))
        self._disp.blit(self._menu.starttext, (600, 300))
        self._disp.blit(self._menu.scorestext, (600, 400))
        self._disp.blit(self._menu.quittext, (600, 500))
        pygame.display.update()

    def _renderhighscores(self):
        self._disp.fill((0, 0, 0))
        counter = 1
        for i in self._scores:
            player = self._menu.font.render(i[0], True, (255,0,0), (0,0,150))
            score = self._menu.font.render(str(i[1]), True, (255,0,0), (0,0,150))
            self._disp.blit(player, (200, counter*50))
            self._disp.blit(score, (350, counter*50))
            counter += 1
        pygame.display.update()
