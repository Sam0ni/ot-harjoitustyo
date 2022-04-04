import unittest
from space.space import Space



class TestLevel(unittest.TestCase):
    def setUp(self):
        self.map = Space(1280, 720)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move(self):
        player = self.map.player

        self.assert_coordinates_equal(player, 1280/2, 720-100)

        self.map.move_player(dx=-100)
        self.assert_coordinates_equal(player, 1280/2 - 100, 720-100)

    def test_cannot_move_beyond_edges(self):
        player = self.map.player

        self.assert_coordinates_equal(player, 1280/2, 720-100)

        self.map.move_player(dx=-1000)
        self.assert_coordinates_equal(player, 1280/2, 720-100)