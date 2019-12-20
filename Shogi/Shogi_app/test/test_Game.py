from django.test import TestCase

from Shogi_app.Game import Game
from Shogi_app.models import GameHistory

class fake_ws():
    def send(self, data):
        pass

class TestGame(TestCase):
    def setUp(self):
        record = GameHistory(date     = "2020-20-20", 
                             duration = "12:12", 
                             user1_id = 3, 
                             user2_id = 5, 
                             init_usi = 'uuuuuuuu', 
                             moves    = 'jjjjjjjj')
        record.save()
        pass

    def test_gmae_data(self):
        ws = fake_ws()
        ret = Game(1, 2, ws, ws)
        self.assertEqual(ret.user1_id, 1)
        self.assertEqual(ret.user2_id, 2)
        self.assertEqual(ret.type, 'proto')
        self.assertEqual(ret.need_save, True)

    def test_send_status(self):
        ws1 = fake_ws()
        ws2 = fake_ws()
        ret = Game(1, 2, ws1, ws2)
        self.assertEqual(ret.send_game_status(), {'content': {'turn': 1, 'round': 0, 'isFinish': False, 'winner': 0, 'usi': 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1', 'validMove': {'9g': ['9f#'], '8g': ['8f#'], '7g': ['7f#'], '6g': ['6f#'], '5g': ['5f#'], '4g': ['4f#'], '3g': ['3f#'], '2g': ['2f#'], '1g': ['1f#'], '2h': ['1h#', '3h#', '4h#', '5h#', '6h#', '7h#'], '9i': ['9h#'], '7i': ['7h#', '6h#'], '6i': ['6h#', '5h#', '7h#'], '5i': ['5h#', '4h#', '6h#'], '4i': ['4h#', '3h#', '5h#'], '3i': ['3h#', '4h#'], '1i': ['1h#']}, 'isCheckmate': False, 'checkmater': [], 'territory': 'GGGGGGGGG/WGWWWWWGW/GGGGGGGGG/WWWWWWWWW/GGGGGGGGG/BBBBBBBBB/GGGGGGGGG/BGBBBBBGB/GGGGGGGGG', 'gameType': 'proto'}, 'type': '[Game] Update Game State'})

