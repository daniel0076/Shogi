from django.test import TestCase

from Shogi_app.Territory import Territory

class TestTerritory(TestCase):
    def setUp(self):
        self.territory = Territory([{(1, 2): [(3, 2), (1, 3), (0, 2), (2, 1), (1, 4), (2, 3), (0, 3), (0, 1), (2, 2), (1, 1)], (1, 5): [(0, 5)], (2, 4): [(3, 5), (1, 3), (0, 2), (3, 3), (4, 2), (5, 1), (6, 0)], (2, 5): [(1, 6), (1, 4), (2, 6), (3, 5)], (4, 0): [(2, 1)], (4, 3): [(3, 3)], (4, 6): [(3, 6), (3, 7), (3, 5), (4, 7), (4, 5), (5, 6)], (5, 0): [], (5, 2): [(4, 2)], (5, 4): [(4, 4)], (5, 7): [(4, 7)], (5, 8): [(4, 8)], (6, 1): [(5, 1)], (6, 2): [(5, 3), (5, 1)], (7, 1): [(6, 0), (8, 2), (7, 0)], (7, 2): [(6, 3), (8, 3)], (7, 3): [(6, 3), (6, 4), (7, 4), (8, 3)], (8, 0): [(7, 0), (6, 0)], (8, 1): [(6, 0)], (8, 8): [(7, 8), (6, 8)], 'S*': ['7i#', '6i#', '4i#', '3i#', '2i#', '9h#', '5h#', '4h#', '3h#', '1h#', '9g#', '6g#', '5g#', '4g#', '3g#', '2g#', '1g#', '8f#', '6f#', '4f#', '3f#', '7e#', '5e#', '4e#', '2e#', '1e#', '6d#', '4d#', '3d#', '2d#', '1d#', '8c#', '7c#', '3c#', '9b#', '6b#', '5b#', '3b#', '2b#', '1b#']}, {(0, 8): [(1, 8)], (1, 1): [(2, 1)], (2, 0): [], (2, 3): [(3, 3)], (2, 7): [(3, 7)], (2, 8): [(3, 8)], (3, 0): [(4, 0), (2, 1)], (3, 1): [], (3, 2): [(4, 2), (4, 3), (2, 1)], (3, 4): [(4, 4)], (4, 1): [(6, 2), (6, 0)], (7, 7): [(7, 3), (6, 7), (6, 8), (6, 6), (7, 6), (5, 7), (7, 4), (7, 5), (8, 8), (8, 7), (8, 6), (7, 8)], (8, 4): [(8, 5), (8, 3), (7, 4)], 'b*': ['9a#', '8a#', '7a#', '6a#', '5a#', '4a#', '3a#', '2a#', '9b#', '6b#', '5b#', '3b#', '2b#', '1b#', '8c#', '7c#', '3c#', '6d#', '4d#', '3d#', '2d#', '1d#', '7e#', '5e#', '4e#', '2e#', '1e#', '8f#', '6f#', '4f#', '3f#', '9g#', '6g#', '5g#', '4g#', '3g#', '2g#', '1g#', '9h#', '5h#', '4h#', '3h#', '1h#'], 'g*': ['9a#', '8a#', '7a#', '6a#', '5a#', '4a#', '3a#', '2a#', '9b#', '6b#', '5b#', '3b#', '2b#', '1b#', '8c#', '7c#', '3c#', '6d#', '4d#', '3d#', '2d#', '1d#', '7e#', '5e#', '4e#', '2e#', '1e#', '8f#', '6f#', '4f#', '3f#', '9g#', '6g#', '5g#', '4g#', '3g#', '2g#', '1g#', '9h#', '5h#', '4h#', '3h#', '1h#'], 'n*': ['9a#', '8a#', '7a#', '6a#', '5a#', '4a#', '3a#', '2a#', '9b#', '6b#', '5b#', '3b#', '2b#', '1b#', '8c#', '7c#', '3c#', '6d#', '4d#', '3d#', '2d#', '1d#', '7e#', '5e#', '4e#', '2e#', '1e#', '8f#', '6f#', '4f#', '3f#', '9g#', '6g#', '5g#', '4g#', '3g#', '2g#', '1g#'], 'p*': ['7a#', '7c#', '7e#', '4a#', '4d#', '4e#', '4f#', '3a#', '3b#', '3c#', '3d#', '3f#']}])

    def test_territory(self):
        self.assertEqual(self.territory.output_terr(), 
                'GBBBGBGGG/GBGBBGBGW/GWBBGGBGG/GGBBGBBGW/WGBWGBGBB/GBGBGGBWG/BGWBBGWWG/BGGWWWWGG/GGBBGWWWW')
