from django.test import TestCase

from Shogi_app.GameManager import GameManagerSingleton
from Shogi_app.models import UserAccount, UserSettings

class fake_ws():
    def send(a, b):
        pass

class TestGameManager(TestCase):
    def setUp(self):
        pass

    def test_new_game(self):
        ws = fake_ws()
        ret = GameManagerSingleton.new_game({"type": 'single'}, 1, ws)
        self.assertEqual(ret.type, 'single')
        self.assertEqual(ret.user1_id, 1)
        self.assertEqual(ret.user2_id, 1)

        ret = GameManagerSingleton.new_game({"type": 'single'}, 1, ws)
        self.assertIsNone(ret)

        ret = GameManagerSingleton.new_game({"type": 'record'}, 2, ws)
        self.assertEqual(ret.type, 'record')
        self.assertEqual(ret.user1_id, 2)
        self.assertEqual(ret.user2_id, 2)

        ret = GameManagerSingleton.new_game({"type": 'puzzle'}, 3, ws)
        self.assertEqual(ret.type, 'puzzle')
        self.assertEqual(ret.user1_id, 3)
        self.assertEqual(ret.user2_id, 3)
