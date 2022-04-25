import pygame
import scores.scores


class Gameloop:
    def __init__(self, space_map, display):
        self._map = space_map
        self._clock = pygame.time.Clock()
        self._disp = display
        self._left = False
        self._right = False
        self._player_name = ""
        self._save_scores = False

    def start(self):
        while True:
            if self._map.victorious:
                break

            if self._events() is False:
                break
            if self._left:
                self._map.move_player(-5)
            if self._right:
                self._map.move_player(5)
            self._map.move_invaders(self._map.invaderspeed)
            if self._map.move_pellets(0, -3):
                if len(self._map.invaders) == 0:
                    self._map.victorious = True
                self._map.invaderspeed += 0.1
            self._map.move_items(0, 4)
            self._map.shottimer -= 1

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
                    if self._map.shottimer <= 0:
                        self._map.shoot_a_pellet(self._map.player.rect.x, 620)
                        self._map.shottimer = 30
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

    def _start_ending(self):
        while True:
            if self._end_events() is False:
                break
            if self._save_scores:
                scores.save_scores()

    def _end_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._save_scores = True
                    return
                if len(self._player_name) < 3:
                    self._player_name += event.unicode
            elif event.type == pygame.QUIT:
                return False