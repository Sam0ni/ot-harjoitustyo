import unittest
from space.space import Space
from menu.menu import Menu
from sprites.item import Item


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.map = Space(1280, 720)
        self.menu = Menu()

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def assert_amount_in_group_equal(self, group, amount):
        after_add_or_kill = len(group)
        self.assertEqual(after_add_or_kill, amount)
    
    def test_can_move(self):
        player = self.map.player

        self.assert_coordinates_equal(player, 1280/2, 720-100)

        self.map.move_player(direct_x=-100)
        self.assert_coordinates_equal(player, 1280/2 - 100, 720-100)

        self.map.move_player(direct_x=+100)
        self.assert_coordinates_equal(player, 1280/2, 720-100)

    def test_cannot_move_beyond_edges(self):
        player = self.map.player

        self.assert_coordinates_equal(player, 1280/2, 720-100)

        self.map.move_player(direct_x=-1000)
        self.assert_coordinates_equal(player, 1280/2, 720-100)

        self.map.move_player(direct_x=+1000)
        self.assert_coordinates_equal(player, 1280/2, 720-100)

    def test_shooting_works(self):
        player = self.map.player

        self.assert_coordinates_equal(player, 1280/2, 720-100)

        self.map.shoot_a_pellet(player.rect.x)
        self.assert_amount_in_group_equal(self.map.pellets, 1)

    def test_pellets_move(self):
        player = self.map.player
        width = player.width
        width = int(width/2)
        self.assert_coordinates_equal(player, 1280/2, 720-100)

        self.map.shoot_a_pellet(player.rect.x)
        self.map.move_pellets(0, -10)
        for i in self.map.pellets:
            
            self.assert_coordinates_equal(i, 1280/2 + width, 720-110)

    def test_pellet_collision_works(self):
        player = self.map.player
        
        self.assert_amount_in_group_equal(self.map.invaders, 64)

        self.map.shoot_a_pellet(player.rect.x + player.width/2 + 40)
        self.map.move_pellets(0, -600)
        
        self.assert_amount_in_group_equal(self.map.invaders, 63)

    def test_menu_start(self):
        press_go = self.menu.go_there()

        self.assertEqual(press_go, True)

    def test_menu_quit(self):
        self.menu.cursor = 3
        press_go = self.menu.go_there()

        self.assertEqual(press_go, False)

    def test_menu_highscore(self):
        self.menu.cursor = 2
        press_go = self.menu.go_there()

        self.assertEqual(press_go, "highscores")

    def test_items_can_spawn(self):
        self.map.items.add(Item(20, 40))
        self.assertEqual(len(self.map.items), 1)

    def test_items_can_move(self):
        self.map.items.add(Item(20, 40))
        self.map.move_items(0, 20)
        for item in self.map.items:
            self.assertEqual(item.rect.y, 60)

    def test_menu_cursor_up(self):
        self.menu.move_cursor_up()
        self.assertEqual(self.menu.cursor, 3)
        self.assertEqual(self.menu.start_color, (0,0,255))
        self.assertEqual(self.menu.quit_color, (255,0,0))
        self.menu.move_cursor_up()
        self.assertEqual(self.menu.cursor, 2)
        self.assertEqual(self.menu.quit_color, (0,0,255))
        self.assertEqual(self.menu.scores_color, (255,0,0))
        self.menu.move_cursor_up()
        self.assertEqual(self.menu.cursor, 1)
        self.assertEqual(self.menu.scores_color, (0,0,255))
        self.assertEqual(self.menu.start_color, (255,0,0))

    def test_menu_cursor_down(self):
        self.menu.move_cursor_down()
        self.assertEqual(self.menu.cursor, 2)
        self.assertEqual(self.menu.start_color, (0,0,255))
        self.assertEqual(self.menu.scores_color, (255,0,0))
        self.menu.move_cursor_down()
        self.assertEqual(self.menu.cursor, 3)
        self.assertEqual(self.menu.scores_color, (0,0,255))
        self.assertEqual(self.menu.quit_color, (255,0,0))
        self.menu.move_cursor_down()
        self.assertEqual(self.menu.cursor, 1)
        self.assertEqual(self.menu.quit_color, (0,0,255))
        self.assertEqual(self.menu.start_color, (255,0,0))
        